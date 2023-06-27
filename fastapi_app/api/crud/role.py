from sqlalchemy.orm import Session
from .. import schemas
from uuid import UUID
from ..models import Role
from fastapi import HTTPException


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
