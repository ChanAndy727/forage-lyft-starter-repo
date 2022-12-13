from classes import TireSet

from collections import Sequence

class CarriganTires(TireSet):
  def __init__(self, tires_wear: Sequence):
    self.tires_wear = tires_wear

  def needs_service(self) -> bool:
    return any(
      [wear_value >= 0.9 for wear_value in self.tires_wear])

class OctoprimeTires(TireSet):
  def __init__(self, tires_wear: Sequence):
      self.tires_wear = tires_wear

  def needs_service(self) -> bool:
      return sum(self.tires_wear) >= 3