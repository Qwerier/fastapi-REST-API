from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from . import models, schemas
from .database import SessionLocal, engine
from .crud.company import *
from .crud.employee import *
from .crud.farm import *
from .crud.panel import *
from .crud.role import *
from .crud.weather import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/companies", response_model=list[schemas.Company])
def read_companies(db: Session = Depends(get_db)):
    return get_companies(db)


@app.post("/companies", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return create_company(company, db)


@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: UUID, db: Session = Depends(get_db)):
    return get_company_by_id(company_id, db)


@app.get("/companies/{company_id}/employees", response_model=list[schemas.Employee])
def read_company_employees(company_id: UUID, db: Session = Depends(get_db)):
    return get_company_employees(company_id, db)


@app.get("/companies/{company_id}/farms", response_model=list[schemas.Farm])
def read_company_farms(company_id: UUID, db: Session = Depends(get_db)):
    return get_company_farms(company_id, db)


@app.get("/companies/{company_id}/weathers", response_model=list[schemas.Weather])
def read_company_weathers(company_id: UUID, db: Session = Depends(get_db)):
    return get_company_weathers(company_id, db)


@app.put("/companies/{company_id}", status_code=200)
def update_company(company_id: UUID, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    update_company(company_id, company, db)
    return {"Messsage": "Company updated"}


@app.delete("/companies/{company_id}", status_code=204)
def delete_company(company_id: UUID, db: Session = Depends(get_db)):
    delete_company(company_id, db)


@app.get("/employees", response_model=list[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return get_employees(db)


@app.post("/employees", response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(emp, db)


@app.post("/employees/link/roles")
def link_employee_to_role(link: schemas.EmployeeRole, db: Session = Depends(get_db)):
    link_employee_to_role(link, db)
    return {"Message": "Role added to employee"}


@app.get("/employees/{employee_id}/roles", response_model=list[schemas.Role])
def read_employee_roles(employee_id: UUID, db: Session = Depends(get_db)):
    return get_employee_roles(employee_id, db)


@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: UUID, db: Session = Depends(get_db)):
    return get_employee_by_id(employee_id, db)


@app.put("/employees/{employee_id}", status_code=200)
def update_employee(employee_id: UUID, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    update_employee(employee_id, employee, db)
    return {"Message": "Employee updated"}


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: UUID, db: Session = Depends(get_db)):
    delete_employee(employee_id, db)


@app.get("/roles", response_model=list[schemas.Role])
def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)


@app.get("/roles/{role_id}", response_model=schemas.Role)
def read_role(role_id: UUID, db: Session = Depends(get_db)):
    return get_role_by_id(role_id, db)


@app.post("/roles", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return create_role(role, db)


@app.put("/roles/{role_id}", status_code=200)
def update_role(role_id: UUID, role: schemas.RoleUpdate, db: Session = Depends(get_db)):
    update_role(role_id, role, db)
    return {"Message": "Role updated"}


@app.delete("/roles/{role_id}", status_code=204)
def delete_role(role_id: UUID, db: Session = Depends(get_db)):
    delete_role(role_id, db)


@app.get("/farms", response_model=list[schemas.Farm])
def read_farms(db: Session = Depends(get_db)):
    return get_farms(db)


@app.post("/farms", response_model=schemas.Farm)
def create_farm(farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    return create_farm(farm, db)


@app.get("/farms/{farm_id}", response_model=schemas.Farm)
def read_farm(farm_id: UUID, db: Session = Depends(get_db)):
    return get_farm_by_id(farm_id, db)


@app.get("/farms/{farm_id}/panels", response_model=list[schemas.Panel])
def read_farm_panels(farm_id: UUID, db: Session = Depends(get_db)):
    return get_farm_panels(farm_id, db)


@app.get("/farms/{farm_id}/weathers", response_model=list[schemas.Weather])
def read_farm_weathers(farm_id: UUID, db: Session = Depends(get_db)):
    return get_farm_weathers(farm_id, db)


@app.delete("/farms/{farm_id}", status_code=204)
def delete_farm(farm_id: UUID, db: Session = Depends(get_db)):
    delete_farm(farm_id, db)


@app.put("/farms/{farm_id}", status_code=200)
def update_farm(farm_id: UUID, farm: schemas.FarmUpdate, db: Session = Depends(get_db)):
    update_farm(farm_id, farm, db)
    return {"Message": "Farm updated"}


@app.get("/panels", response_model=list[schemas.Panel])
def read_panel(db: Session = Depends(get_db)):
    return get_panels(db)


@app.post("/panels", response_model=schemas.Panel)
def create_panel(panel: schemas.PanelCreate, db: Session = Depends(get_db)):
    return create_panel(panel, db)


@app.get("/panels/{panel_id}", response_model=schemas.Panel)
def read_panel(panel_id: UUID, db: Session = Depends(get_db)):
    return get_panel_by_id(panel_id, db)


@app.put("/panels/{panel_id}", status_code=200)
def update_panel(panel_id: UUID, panel: schemas.PanelUpdate, db: Session = Depends(get_db)):
    update_panel(panel_id, panel, db)
    return {"Message": "Panel updated"}


@app.delete("/panels/{panel_id}", status_code=204)
def delete_panel(panel_id: UUID, db: Session = Depends(get_db)):
    delete_panel(panel_id, db)


@app.get("/weather", response_model=list[schemas.Weather])
def read_weathers(db: Session = Depends(get_db)):
    return get_weathers(db)


@app.post("/weather/{city}", response_model=schemas.Weather)
def create_weather(weather: schemas.WeatherCreate, city: str, db: Session = Depends(get_db)):
    return create_weather(weather, city, db)


@app.get("/weather/{weather_id}", response_model=schemas.Weather)
def read_weather(weather_id: UUID, db: Session = Depends(get_db)):
    return get_weather_by_id(weather_id, db)


@app.put("/weather/{weather_id}", status_code=200)
def update_weather(weather_id: UUID, weather: schemas.WeatherUpdate, db: Session = Depends(get_db)):
    update_weather(weather_id, weather, db)
    return {"Message": "Weather updated"}


@app.delete("/weather/{weather_id}", status_code=204)
def delete_weather(weather_id: UUID, db: Session = Depends(get_db)):
    delete_weather(weather_id, db)
