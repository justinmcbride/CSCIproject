import unittest
import sensing

class TestSensing(unittest.TestCase):
	def setup(self):
		pass

	def test_LightSensor(self):
		self.assertRaises(sensing.SensorPinException, sensing.LightSensor, pin=6)
		self.assertRaises(sensing.SensorPinException, sensing.LightSensor, pin=-1)
		self.assertRaises(sensing.SensorPinException, sensing.LightSensor, pin="not a number")
		self.assertIsInstance(sensing.LightSensor(), sensing.LightSensor)
		self.assertRaises(sensing.SensorNameException, sensing.LightSensor, name=10)

	def test_TempSensor(self):
		self.assertRaises(sensing.SensorPinException, sensing.TemperatureSensor, pin=6)
		self.assertRaises(sensing.SensorPinException, sensing.TemperatureSensor, pin=-1)
		self.assertRaises(sensing.SensorPinException, sensing.TemperatureSensor, pin="not a number")
		self.assertIsInstance(sensing.TemperatureSensor(), sensing.TemperatureSensor)
		self.assertRaises(sensing.SensorNameException, sensing.TemperatureSensor, name=10)

if __name__ == '__main__':
	unittest.main()