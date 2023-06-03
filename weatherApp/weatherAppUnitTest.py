import unittest
from weatherApp import get_lat_lon_by_city

class TestClass(unittest.TestCase):
    def test_latlon(self):
        lat_lon_dict = get_lat_lon_by_city('Boston','MA','USA')
        print(lat_lon_dict)
        



