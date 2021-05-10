import numpy as np
from shapely.geometry import mapping

def Geo2Array(geo, skip=0):
    result = []
    for item in geo:
        all_coords = mapping(item)["coordinates"]
        array = np.array(all_coords)
        while (len(array) == 1):
            array = array[0]
        result+=list(array)
        if skip != 0:
            result = result[0::skip]
    return result

def minValue(data, index):
    return min(data, key = lambda t: t[index])

def maxValue(data, index):
    return max(data, key = lambda t: t[index])

def PointInPolygon(point, polygon):
    minX = minValue(polygon, 0)[0]
    minY = minValue(polygon, 1)[1]
    maxX = maxValue(polygon, 0)[0]
    maxY = maxValue(polygon, 1)[1]
    x = point[0]
    y = point[1]
    if x > maxX or x < minX or y > maxY or x < minY:
        return False
    sumAngle = 0
    i = 0
    j = len(polygon)-1
    inside = False
    while i < len(polygon):
        if x==polygon[i][0] and y==polygon[i][1]:
                return True
        if(((polygon[i][1] > y) != (polygon[j][1] > y)) and ( x <= (polygon[j][0]-polygon[i][0])*(y-polygon[i][1])/(polygon[j][1]-polygon[i][1])+polygon[i][0])):
            if inside:
                inside = False
            else:
                inside = True
        j = i
        i += 1
    return inside
