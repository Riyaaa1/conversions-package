import unittest
from src import length
from src import temperature

class TesttempConversions(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(temperature.celsius_to_fahrenheit(37),98.6,'Conversion is wrong')

    def test_celsius_to_kelvin(self):
        self.assertEqual(temperature.celsius_to_kelvin(37),310.15,"Conversion is wrong.")

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(temperature.fahrenheit_to_celsius(-40),-40.0,"Conversion is wrong.")

    def test_kelvin_to_celsius(self):
        self.assertEqual(temperature.kelvin_to_celsius(273.15),0.0,"Conversion is wrong.")

class TestlengthConversions(unittest.TestCase):
    def test_cm_to_m(self): 
        length_obj = length.Length(100)
        self.assertEqual(length_obj.cm_to_m(),1.0,"Conversion is wrong")
        
    def test_cm_to_km(self):
        length_obj = length.Length(100000)
        self.assertEqual(length_obj.cm_to_km(),1.0,"Conversion is wrong")

    def test_m_to_cm(self):
        length_obj = length.Length(1)
        self.assertEqual(length_obj.m_to_cm(),100,"Conversion is wrong")
        
    
    def test_m_to_km(self):
        length_obj = length.Length(1000)
        self.assertEqual(length_obj.m_to_km(),1.0,"Conversion is wrong")
   
    def test_km_to_cm(self):
        length_obj = length.Length(1)
        self.assertEqual(length_obj.km_to_cm(),100000,"Conversion is wrong")
    

if __name__ == "__main__":
    unittest.main()