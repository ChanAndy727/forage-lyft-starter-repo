from calendar import c
from classes import Battery
from datetime import date

class SpindlerBattery(Battery):
  def __init__(self, last_serv_date: date, curr_date: date):
    self.last_serv_date = last_serv_date
    self.curr_date = curr_date

  def needs_Service(self) -> bool:
    serv_thresh = 365 * 2
    time_since_serv = self.curr_date - self.last_serv_date
    return time_since_serv.days > serv_thresh

class NubbinBattery(Battery):
  def __init__(self, last_serv_date: date, curr_date: date):
    self.last_serv_date = last_serv_date
    self.curr_date = curr_date

  def needs_Service(self) -> bool:
    serv_thresh = 365 * 4
    time_since_serv = self.curr_date - self.last_serv_date
    return time_since_serv.days > serv_thresh
