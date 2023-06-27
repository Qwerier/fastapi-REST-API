from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime, Numeric, Table, UUID
from sqlalchemy.orm import relationship, backref
from uuid import uuid4
from .database import Base

employee_role = Table(
    "employees_roles",
    Base.metadata,
    Column("employee_id", ForeignKey("employees.employee_id")),
    Column("role_id", ForeignKey("roles.role_id"))
)


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    name = Column(String)
    mission = Column(String)
    nuis = Column(String, unique=True)

    employees = relationship('Employee', backref='companies', passive_deletes=True)
    farms = relationship("Farm", backref="companies", passive_deletes=True)
    weathers = relationship("Weather", backref="companies", passive_deletes=True)


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(UUID, ForeignKey("companies.company_id", ondelete="CASCADE"))

    roles = relationship("Role", secondary=employee_role, backref=backref("employees"))


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    name = Column(String)


class Farm(Base):
    __tablename__ = "farms"

    farm_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    location = Column(String)
    area = Column(Float)
    exp_output = Column(Float)
    nr_panels = Column(Integer)
    landscape = Column(String)
    orientation = Column(String)
    company_id = Column(UUID, ForeignKey("companies.company_id", ondelete="CASCADE"))

    panels = relationship("Panel", backref="farms", passive_deletes=True)
    weathers = relationship("Weather", backref="farms", passive_deletes=True)


class Panel(Base):
    __tablename__ = "panels"

    panel_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    height = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    brand = Column(String)
    material = Column(String)

    farm_id = Column(UUID, ForeignKey("farms.farm_id", ondelete="CASCADE"))


class Weather(Base):
    __tablename__ = "weather"

    weather_id = Column(UUID, default=uuid4, primary_key=True, index=True)
    sunrise = Column(DateTime)
    sunset = Column(DateTime)
    temperature = Column(Numeric)
    pressure = Column(Numeric)
    humidity = Column(Numeric)
    clouds = Column(Integer)
    wind_speed = Column(Numeric)
    rain = Column(Numeric)
    snow = Column(Numeric)

    farm_id = Column(UUID, ForeignKey("farms.farm_id", ondelete="CASCADE"))
    company_id = Column(UUID, ForeignKey("companies.company_id", ondelete="CASCADE"))
