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

class Car(Serviceable):
  def __init__(self, engine, battery):
    self.engine = engine
    self.battery = battery

  def needs_Service(self) -> bool:
    return self.engine.needs_service() or self.battery.needs_Service()