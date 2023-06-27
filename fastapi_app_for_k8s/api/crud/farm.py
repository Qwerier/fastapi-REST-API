from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Farm
from fastapi import HTTPException


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
