import unittest

from tires import CarriganTires, OctoprimeTires

class TestCarriganTires(unittest.TestCase):
  def setUp(self):
    self.carrigan_tires_need_service = CarriganTires((0.7, 0.8, 1, 0.7))
    self.carrigan_tires_no_service = CarriganTires((0.1, 0.2, 0.3, 0.4))

  def test_need_service(self):
    self.assertTrue(self.carrigan_tires_need_service.needs_service())

  def test_no_service(self):
    self.assertFalse(self.carrigan_tires_no_service.needs_service())

class TestOctoprimeTires(unittest.TestCase):
  def setUp(self):
    self.octoprime_tires_need_service = OctoprimeTires((0.8, 0.9, 0.9, 1))
    self.octoprime_tires_no_service = OctoprimeTires((0.7, 0.8, 0.7, 0.7))

  def test_need_service(self):
    self.assertTrue(self.octoprime_tires_need_service.needs_service())

  def test_no_service(self):
    self.assertFalse(self.octoprime_tires_no_service.needs_service())
