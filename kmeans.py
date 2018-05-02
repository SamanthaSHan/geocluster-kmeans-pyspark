import sys
from pyspark import SparkContext
from point_utils import *

if __name__ == "__main__":
    sc = SparkContext()

    # convergeDist is set to 0.1 as stated in the project guidelines
    convergeDist = float(0.1)
    iterationDist = float("inf")

    # Validate command line arguments
    if len(sys.argv) != 5:
        print "usage: python " + sys.argv[0] + " <input_path> <output_path> <distance_measure> <k>\n"
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    distanceMeasure = sys.argv[3].lower()
    if distanceMeasure != "euclidean" and distanceMeasure != "greatcircle":
        print "distance_measure must be either \"Euclidean\" or \"GreatCircle\"\n"
        sys.exit(1)

    k = int(sys.argv[4])
    if k < 1:
        print "k should be larger than 0\n"
        sys.exit(1)


    # Parse data
    filtered_data = sc.textFile("file:/" + input_file_path)
    latlon = filtered_data.map(lambda x: x.split(",")) \
    .map(lambda x: [LatLonPoint(x[0], x[1]), x[2:]]).cache()

    # Use a sample of points as the initial centroids
    centroids = latlon.map(lambda x: x[0]).takeSample(False, k, 1)
    centroids = dict(zip(range(0, k), centroids))


    while iterationDist > convergeDist:
        # Map each point to a key-value pair, where the key is the closest centroid
        closest = latlon.map(lambda point: (closestPoint(point[0], centroids, distanceMeasure), point))

        # Count the number of points in each centroid
        numPoints = closest.countByKey()

        # Calculate the new centroids using the sum of the points and the number of points in the centroid
        newMeans = closest.map(lambda (closest, point): (closest, latLonToCartesian(point[0]))) \
        .reduceByKey(addPoints) \
        .map(lambda (centroid, sumPoints): (centroid, dividePoints(sumPoints, numPoints[centroid])))

        # Calculate the distances between the old and new centroids
        if distanceMeasure == "greatcircle":
            distances = newMeans.map(lambda (idx, mean): greatCircleDistance(centroids[idx], mean))
        else:
            distances = newMeans.map(lambda (idx, mean): euclideanDistance(centroids[idx], mean))

        # Use the sum of the distances between old and new centroids as the convergeDist measure
        iterationDist = distances.sum()

        # Update centroids to the new means
        centroids = newMeans.collectAsMap()


    # Save the list of points and their clusters to a file
    closest.map(lambda (closest, point): str(closest) + "," + str(point[0].lat) + "," + str(point[0].lon) + "," + ",".join(s.encode("utf-8", "ignore") for s in point[1])) \
    .saveAsTextFile("file:/" + output_file_path)

    # Print the final centroids
    for idx, centroid in centroids.items():
        print str(idx) + "," + str(centroid.lat) + "," + str(centroid.lon)

    # Calculate the mean distance between points and their nearest centroid
    if distanceMeasure == "greatcircle":
        distsFromCentroid = closest.map(lambda (closest, point): greatCircleDistance(centroids[closest], point[0]))
    else:
        distsFromCentroid = closest.map(lambda (closest, point): euclideanDistance(centroids[closest], point[0]))
    print distsFromCentroid.mean()
