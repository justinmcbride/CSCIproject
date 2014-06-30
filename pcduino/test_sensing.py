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

	def test_Brightness(self):
		obj = sensing.LightSensor()
		self.assertEquals(obj.brightness(4096), 100.0)
		self.assertEquals(obj.brightness(0), 0.0)
		self.assertEquals(obj.brightness(3245), 79.2236328125)
		self.assertEquals(obj.brightness(-1), -0.0244140625)
		self.assertEquals(obj.brightness(4097), 100.0244140625)

	def test_getAverageLight(self):
		obj = sensing.LightSensor()
		obj._history  = [1, 2, 3, 4, 5]
		self.assertEquals(obj.getAverageofReadings(), 3)
		obj._history  = []
		self.assertRaises(sensing.NoHistoryException, obj.getAverageofReadings)
		obj._history  = [1, 2, 3, 4, 5, 6, 7]
		self.assertEquals(obj.getAverageofReadings(), 4)

	def test_getAverageTemp(self):
		obj = sensing.TemperatureSensor()
		obj._history  = [1, 2, 3, 4, 5]
		self.assertEquals(obj.getAverageofReadings(), 3)
		obj._history  = []
		self.assertRaises(sensing.NoHistoryException, obj.getAverageofReadings)
		obj._history  = [1, 2, 3, 4, 5, 6, 7]
		self.assertEquals(obj.getAverageofReadings(), 4)

	def test_dataUpload(self):
		sensing.ApiURI = "https://dsp-csci-project.cloud.dreamfactory.com:443/rest/mongodb/test"
		data = {"test" : "object"}
		self.assertTrue(sensing.sendData(data))


if __name__ == '__main__':
	unittest.main()
