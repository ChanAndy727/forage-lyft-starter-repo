from classes import Engine

class CapuletEngine(Engine):
  def __init__(self, curr_mileage: int, last_serv_mileage: int):
    self.curr_mileage = curr_mileage
    self.last_serv_mileage = last_serv_mileage

  def needs_Service(self) -> bool:
    return (self.curr_mileage - self.last_serv_mileage) > 30000

class WilloughbyEngine(Engine):
  def __init__(self, curr_mileage: int, last_serv_mileage: int):
      self.curr_mileage = curr_mileage
      self.last_serv_mileage = last_serv_mileage

  def needs_Service(self) -> bool:
    return (self.curr_mileage - self.last_serv_mileage) > 60000

class SternmanEngine(Engine):
  def __init__(self, warning_light_on: bool):
    self.warning_light_on = warning_light_on

  def needs_Service(self) -> bool:
    return self.warning_light_on