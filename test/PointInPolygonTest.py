import unittest
import geopandas as gpd
import PointInPolygon as pnp

### TEST

class FunctionsTest(unittest.TestCase):

  def testGeo2Array(self):
    geodf = gpd.read_file('./test/test.geojson')
    geoarray = pnp.Geo2Array([geodf['geometry'].values[0]],150)
    length = len(geoarray)
    self.assertEqual(length, 54)
    print('Geo convert to array is correct')
    
  def testPointOnBorder(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(5,7)
    result = pnp.PointInPolygon(t2, t1)
    self.assertTrue(result)
    print('Point on border is correct')
  
  def testPointInPolygon(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(5,6)
    result = pnp.PointInPolygon(t2, t1)
    self.assertTrue(result)
    print('Point inside of polygon is correct')

  def testPointOutPolygon(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(4,7)
    result = pnp.PointInPolygon(t2, t1)
    self.assertFalse(result)
    print('Point outside of polygon is correct')
