from math import degrees, radians, sin, cos, sqrt, asin, atan2

# Radius of the Earth, in km
EARTH_RADIUS = 6371

class LatLonPoint:
    def __init__(self, lat, lon):
        self.lat = float(lat)
        self.lon = float(lon)

class CartesianPoint:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

# Convert (lat, lon) to (x, y, z)
def latLonToCartesian(point):
    latRad = radians(point.lat)
    lonRad = radians(point.lon)
    
    x = EARTH_RADIUS * cos(latRad) * cos(lonRad)
    y = EARTH_RADIUS * cos(latRad) * sin(lonRad)
    z = EARTH_RADIUS * sin(latRad)
    
    return CartesianPoint(x, y, z)

# Convert (x, y, z) to (lat, lon)
def cartesianToLatLon(point):
    lat = degrees(asin(point.z / EARTH_RADIUS))
    lon = degrees(atan2(point.y, point.x))
    
    return LatLonPoint(lat, lon)

# Based on distanceMeasure, calculate the distances from a point to the centroids
# Return the index of the centroid closest to the point
def closestPoint(point, centroids, distanceMeasure):
    minDist = float("inf")
    closest = -1
    for idx, centroid in centroids.items():
        if distanceMeasure == "greatcircle":
            dist = greatCircleDistance(point, centroid)
        else:
            dist = euclideanDistance(point, centroid)
        if dist < minDist:
            minDist = dist
            closest = idx
            
    return closest

# Add two CartesianPoints
def addPoints(a, b):
    return CartesianPoint(a.x + b.x, a.y + b.y, a.z + b.z)

# Return a new centroid by calculating the mean of points in the cluster
# sumPoints: CartesianPoint representing the sum of the points in the cluster
# numPoints: number of points in the cluster
def dividePoints(sumPoints, numPoints):
    result = CartesianPoint(sumPoints.x / numPoints, sumPoints.y / numPoints, sumPoints.z / numPoints)
    return cartesianToLatLon(result)

# Return the Euclidean distance between two LatLonPoints
def euclideanDistance(a, b):
    aCart = latLonToCartesian(a)
    bCart = latLonToCartesian(b)
    
    return sqrt((aCart.x - bCart.x)**2 + (aCart.y - bCart.y)**2 + (aCart.z - bCart.z)**2)

# Return the great circle distance between two LatLonPoints
def greatCircleDistance(p1, p2):
    lat_diff = radians(p2.lat) - radians(p1.lat)
    lon_diff = radians(p2.lon) - radians(p1.lon)    
    
    a = (sin(lat_diff/2))**2 + cos(radians(p1.lat)) * cos(radians(p2.lat)) * (sin(lon_diff/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return EARTH_RADIUS * c


