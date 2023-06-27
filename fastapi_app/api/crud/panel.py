from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Panel
from fastapi import HTTPException


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
