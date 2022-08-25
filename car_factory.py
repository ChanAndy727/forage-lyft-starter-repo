from classes import Car
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from batteries import NubbinBattery, SpindlerBattery
from datetime import date

class CarFactory:
  @classmethod
  def create_calliope(cls, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    return Car(
      engine=CapuletEngine(current_mileage, last_service_mileage),
      battery=SpindlerBattery(last_service_date, current_date))

  @classmethod
  def create_glissade(cls, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    return Car(
      engine=WilloughbyEngine(current_mileage, last_service_mileage),
      battery=SpindlerBattery(last_service_date, current_date))

  @classmethod
  def create_palindrome(cls, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    return Car(
      engine=SternmanEngine(warning_light_on),
      battery=SpindlerBattery(last_service_date, current_date))

  @classmethod
  def create_rorschach(cls, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    return Car(
      engine=WilloughbyEngine(current_mileage, last_service_mileage),
      battery=NubbinBattery(last_service_date, current_date))

  @classmethod
  def create_thovex(cls, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    return Car(
      engine=CapuletEngine(current_mileage, last_service_mileage),
      battery=NubbinBattery(last_service_date, current_date))

