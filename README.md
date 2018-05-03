# K-means for Geo-location Clustering in Spark

### This is a final group project for CSE427S (SP18) - Cloud Computing with Big Data Applications

We have implemented K-means algorithm for Euclidean and Great Circle distance measurement. Our algorithm iteratively updates the location of k-cluster centroids until it converges to α = 0.1 km, where α is converging distance. We processed our data on Amazon EMR. For the detailed result and full report, please refer to [Final write-up.pdf](https://github.com/SamanthaSHan/geocluster-kmeans-pyspark/blob/master/Final%20Write-up.pdf)

------

#### [kmeans.py](https://github.com/SamanthaSHan/geocluster-kmeans-pyspark/blob/master/kmeans.py)

This is a driver that parses an input file and processes it. It takes following 4 command line arguments

    <input_path> <output_path> <distance_measure> <k>
where `input_path` is the path to the input data (e.g. home/cloudera/cse427/final_project/dbpedia), `output_path` is the path where output data should be saved, `distance_measure` is either “euclidean” or “greatcircle” (case-insensitive), and `k` is an integer larger than 0.

#### [point\_utils.py](https://github.com/SamanthaSHan/geocluster-kmeans-pyspark/blob/master/point_utils.py)


This is a collection of helper functions used in **kmeans.py** 

------
#### Contributors

* Samantha Han (samantha.han@wustl.edu)
* Hakkyung Lee (hakkyung@wustl.edu)
* Skylar Nam (nam@wustl.edu)
* Zefang Tang (zefang@wustl.edu)
