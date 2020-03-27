from math import radians, cos, sin, asin, sqrt, atan2, degrees
import sys

# Based on the haversine formula
def haversine(lat1, lon1, lat2, lon2):
    
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r
    
def bearing(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    y = sin(lon2 - lon1) * cos(lat2)
    x = (cos(lat1) * sin(lat2)) - (sin(lat1) * cos(lat2) * cos(lon2 - lon1))
    return degrees(atan2(y , x))

def main():
    if len(sys.argv) != 5:
        print("The function requires exactly 4 inputs. \nEast longitudes are positive and North latitudes are positive. \nPlease input in the format: " + sys.argv[0] + " latitude1 longitude1 latitude2 longitude2")
    else:
        print("Coordinates entered: (" + sys.argv[1] + "," + sys.argv[2] + ") , (" + sys.argv[3] + "," + sys.argv[4] + ")")
        print("Distance: " + str(haversine(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])))
        print("Bearing: " + str(bearing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])))
    
if __name__ == '__main__':
    main ()
