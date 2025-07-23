import unittest
from weather import Weather

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.weather = Weather("7b987133563f30c2e1d25fdaba64be07")

    def test_known_city_is_entered(self):
        result=self.weather.get_weather("delhi")
        self.assertIn("delhi",result.lower())

    def test_unknown_city_is_entered(self):
        result=self.weather.get_weather("adsfgml")
        self.assertEqual(result,"Not found")

    def test_input_is_case_sensitive(self):
        result1=self.weather.get_weather("delhi")
        result2=self.weather.get_weather("Delhi")
        self.assertEqual(result1.split(":")[0].lower(),result2.split(":")[0].lower())

    def test_input_is_null(self):
        result=self.weather.get_weather("")
        self.assertEqual(result,"Not found")

if __name__=="__main__":
    unittest.main()