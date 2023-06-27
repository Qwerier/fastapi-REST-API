from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime as dt


#                               COMPANY SCHEMAS
class CompanyBase(BaseModel):
    name: str
    mission: str
    nuis: str


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class Company(CompanyBase):
    company_id: UUID

    class Config:
        orm_mode = True


#        EMPLOYEE SCHEMAS
class EmployeeBase(BaseModel):
    name: str
    company_id: UUID


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    employee_id: UUID

    class Config:
        orm_mode = True


#                                   ROLE SCHEMAS

class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass


class Role(RoleBase):
    role_id: UUID

    class Config:
        orm_mode = True


# MIXED CLASS
class EmployeeRole(BaseModel):
    employee_id: UUID
    role_id: UUID


#                                   FARM SCHEMAS
class FarmBase(BaseModel):
    location: str
    area: float
    exp_output: float
    nr_panels: int
    landscape: str
    orientation: str

    company_id: UUID


class FarmCreate(FarmBase):
    pass


class FarmUpdate(FarmBase):
    pass


class Farm(FarmBase):
    farm_id: UUID

    class Config:
        orm_mode = True


#                               PANEL SCHEMAS
class PanelBase(BaseModel):
    height: int
    width: int
    depth: int
    brand: str
    material: str

    farm_id: UUID


class PanelCreate(PanelBase):
    pass


class PanelUpdate(PanelBase):
    pass


class Panel(PanelBase):
    panel_id: UUID

    class Config:
        orm_mode = True


#                        WEATHER SCHEMAS

class WeatherBase(BaseModel):
    farm_id: UUID
    company_id: UUID


class WeatherCreate(WeatherBase):
    pass


class WeatherUpdate(WeatherBase):
    sunrise: dt
    sunset: dt
    temperature: float
    pressure: float
    humidity: float
    clouds: int
    wind_speed: float
    rain: float
    snow: float


class Weather(WeatherUpdate):
    weather_id: UUID

    class Config:
        orm_mode = True
