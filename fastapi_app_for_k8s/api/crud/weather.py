from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Weather
from fastapi import HTTPException


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
