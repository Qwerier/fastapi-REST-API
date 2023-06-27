from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Company
from fastapi import HTTPException


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
