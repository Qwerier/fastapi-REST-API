from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Employee
from fastapi import HTTPException


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
