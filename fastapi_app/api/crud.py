from sqlalchemy.orm import Session
from . import schemas
from uuid import UUID
from .models import Company, Employee, Farm, Panel, Weather, Role
from fastapi import HTTPException

from .weatherapi import weather_data

"""         COMPANY CODE SECTION          """


def get_company_by_id(company_id: UUID, db: Session):
    company = db.query(Company).filter(Company.company_id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


def get_company_by_nuis(nuis: str, db: Session):
    return db.query(Company).filter(Company.nuis == nuis).first()


def get_company_employees(company_id: UUID, db: Session):
    return db.query(Employee).filter(Employee.company_id == company_id).all()


def get_company_farms(company_id: UUID, db: Session):
    return db.query(Farm).filter(Farm.company_id == company_id).all()


def get_company_weathers(company_id: UUID, db: Session):
    return db.query(Weather).filter(Weather.company_id == company_id).all()


def get_companies(db: Session):
    return db.query(Company).all()


def create_company(company: schemas.CompanyCreate, db: Session):
    if get_company_by_nuis(company.nuis, db):
        raise HTTPException(status_code=409, detail="Company already exists")
    db_company = Company(**vars(company))

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


def update_company(company_id: UUID, company: schemas.CompanyUpdate, db: Session):
    if db.query(Company).filter(Company.company_id == company_id).update(vars(company)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Company not found")


def delete_company(company_id: UUID, db: Session):
    company = get_company_by_id(company_id, db)
    db.delete(company)
    db.commit()


"""         EMPLOYEE CODE SECTION        """


def get_employee_by_id(employee_id: UUID, db: Session):
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


def get_employee_by_name(name: str, db: Session):
    return db.query(Employee).filter(Employee.name == name).all()


def get_employees(db: Session):
    return db.query(Employee).all()


def get_employee_roles(employee_id: UUID, db: Session):
    return db.query(Role).filter(Role.employees.any(employee_id=employee_id)).all()


def create_employee(employee: schemas.EmployeeCreate, db: Session):
    db_emp = Employee(**vars(employee))

    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def link_employee_to_role(link: schemas.EmployeeRole, db: Session):
    db_emp = get_employee_by_id(link.employee_id, db)
    db_role = get_role_by_id(link.role_id, db)

    db_emp.roles.append(db_role)
    db.commit()


def update_employee(employee_id: UUID, employee: schemas.EmployeeUpdate, db: Session):
    if db.query(Employee).filter(Employee.employee_id == employee_id).update(vars(employee)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


def delete_employee(employee_id: UUID, db: Session):
    employee = get_employee_by_id(employee_id, db)
    db.delete(employee)
    db.commit()


"""             ROLE CODE SECTION           """


def get_role_by_id(role_id: UUID, db: Session):
    role = db.query(Role).filter(Role.role_id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


def get_roles(db: Session):
    return db.query(Role).all()


def create_role(role: schemas.RoleCreate, db: Session):
    db_role = Role(**vars(role))

    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def update_role(role_id: UUID, role: schemas.RoleUpdate, db: Session):
    if db.query(Role).filter(Role.role_id == role_id).update(vars(role)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Role not found")


def delete_role(role_id: UUID, db: Session):
    role = get_role_by_id(role_id, db)
    db.delete(role)
    db.commit()


"""             FARM  CODE SECTION SECTION      """


def get_farm_by_id(farm_id: UUID, db: Session):
    farm = db.query(Farm).filter(Farm.farm_id == farm_id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm


def get_farms(db: Session):
    return db.query(Farm).all()


def get_farm_panels(farm_id: UUID, db: Session):
    return db.query(Panel).filter(Panel.farm_id == farm_id).all()


def get_farm_weathers(farm_id: UUID, db: Session):
    return db.query(Weather).filter(Weather.farm_id == farm_id).all()


def create_farm(farm: schemas.FarmCreate, db: Session):
    db_farm = Farm(**vars(farm))
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm


def update_farm(farm_id: UUID, farm: schemas.FarmUpdate, db: Session):
    if db.query(Farm).filter(Farm.farm_id == farm_id).update(vars(farm)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Farm not found")


def delete_farm(farm_id: UUID, db: Session):  # it deletes it based on the id of the farm
    farm = get_farm_by_id(farm_id, db)
    db.delete(farm)
    db.commit()


"""             PANEL CODE SECTION           """


def get_panel_by_id(panel_id: UUID, db: Session):
    panel = db.query(Panel).filter(Panel.panel_id == panel_id).first()
    if not panel:
        raise HTTPException(status_code=404, detail="Panel not found")
    return panel


def get_panels(db: Session):
    return db.query(Panel).all()


def create_panel(panel: schemas.PanelCreate, db: Session):
    db_panel = Panel(**vars(panel))
    db.add(db_panel)
    db.commit()
    db.refresh(db_panel)
    return db_panel


def update_panel(panel_id: UUID, panel: schemas.PanelUpdate, db: Session):
    if db.query(Panel).filter(Panel.panel_id == panel_id).update(vars(panel)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Panel not found")


def delete_panel(panel_id: UUID, db: Session):
    panel = get_panel_by_id(panel_id, db)
    db.delete(panel)
    db.commit()


"""              WEATHER CODE SECTION                 """


def get_weather_by_id(weather_id: UUID, db: Session):
    weather = db.query(Weather).filter(Weather.weather_id == weather_id).first()
    if not weather:
        raise HTTPException(status_code=404, detail="Weather not found")
    return weather


def get_weathers(db: Session):
    return db.query(Weather).all()


def create_weather(weather: schemas.WeatherCreate, city: str, db: Session):
    response = weather_data(city)
    db_weather = Weather(**response, farm_id=weather.farm_id, company_id=weather.company_id)

    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def update_weather(weather_id: UUID, weather: schemas.WeatherUpdate, db: Session):
    if db.query(Weather).filter(Weather.weather_id == weather_id).update(vars(weather)):
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Weather not found")


def delete_weather(weather_id: UUID, db: Session):
    weather = get_weather_by_id(weather_id, db)
    db.delete(weather)
    db.commit()
