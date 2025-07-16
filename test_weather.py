import unittest
from weather import weather

class WeatherTest(unittest.TestCase):
    def test_known_city_is_entered(self):
        result=weather("delhi")
        self.assertIn("Delhi:",result)

    def test_unknown_city_is_entered(self):
        result=weather("abc")
        self.assertEqual(result,"not found")

    def test_input_is_case_sensitive(self):
        result=weather("Delhi")
        self.assertIn("Delhi:",result)

    def test_input_is_null(self):
        result=weather(None)
        self.assertEqual(result, "Not found")

if __name__=="__main__":
    unittest.main()

    

    
