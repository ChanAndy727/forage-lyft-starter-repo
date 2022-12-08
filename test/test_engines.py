import unittest

from engines import CapuletEngine, WilloughbyEngine, SternmanEngine

class TestCapuletEngine(unittest.TestCase):
  def setUp(self) -> None:
    self.capulet_need_service = CapuletEngine(31000, 0)
    self.capulet_no_service = CapuletEngine(1000, 30)

  def test_need_service(self):
    self.assertTrue(self.capulet_need_service.needs_Service())

  def test_no_service(self):
    self.assertFalse(self.capulet_no_service.needs_Service())

class TestWilloughbyEngine(unittest.TestCase):
  def setUp(self) -> None:
    self.willoughby_need_service = WilloughbyEngine(61000, 0)
    self.willoughby_no_service = WilloughbyEngine(19000, 30)

  def test_need_service(self):
    self.assertTrue(self.willoughby_need_service.needs_Service())

  def test_no_service(self):
    self.assertFalse(self.willoughby_no_service.needs_Service())

class TestSternmanEngine(unittest.TestCase):
  def setUp(self) -> None:
    self.sternman_need_service = SternmanEngine(31000, 0)
    self.sternman_no_service = SternmanEngine(1000, 30)

  def test_need_service(self):
    self.assertTrue(self.sternman_need_service.needs_Service())

  def test_no_service(self):
    self.assertFalse(self.sternman_no_service.needs_Service())

if __name__ == "__main__":
  unittest.main()