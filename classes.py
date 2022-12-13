#abstract classe
from abc import ABC, abstractmethod

class Serviceable(ABC):
  @abstractmethod
  def needs_Service(self) -> bool:
    pass

class Engine(Serviceable):
  pass

class Battery(Serviceable):
  pass

class TireSet(Serviceable):
  pass

class Car(Serviceable):
  def __init__(self, engine, battery, tire_set):
    self.engine = engine
    self.battery = battery
    self.tire_set = tire_set

  def needs_Service(self) -> bool:
    return self.engine.needs_Service() or self.battery.needs_Service() or self.tire_set.needs_Service()