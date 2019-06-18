import logging
from dataclasses import dataclass, field
from typing import List

from sqlalchemy.exc import IntegrityError

from apigateway.auth.models import Permission, Role, RolePermission
from apigateway.database import db


logger = logging.getLogger(__name__)


@dataclass
class PermissionDao:
    name: str
    service: str

    def __repr__(self):
        return f"{self.service}.{self.name}"


@dataclass
class RoleDao:
    name: str
    permissions: List[PermissionDao] = field(default_factory=list)

    def __repr__(self):
        return f"{self.name}"

    def get_permission_ids(self):
        if permissions:
            return [Permission.query.filter(Permission.name == permission.name, Permission.service == permission.service).one().id for permission in self.permissions]


permissions = [
    PermissionDao('check_fund', 'stock-checker'),
    PermissionDao('add_entry', 'changelog-backend')
]

roles = [
    RoleDao(name="staff", permissions=[
        *permissions
    ]),
    RoleDao(name="admin")
]


def generate_permissions():
    for permission in permissions:
        new_permission = Permission(name=permission.name, service=permission.service)
        try:
            db.session.add(new_permission)
            db.session.commit()
        except IntegrityError:
            logger.info(f"Role {permission} already exists")
            db.session.rollback()


def generate_roles():
    for role in roles:
        new_role = Role(name=role.name)
        try:
            db.session.add(new_role)
            db.session.commit()
        except IntegrityError:
            logger.info(f"Role {role} already exists")
            db.session.rollback()
        for permission_id in role.get_permission_ids():
            new_role = Role.query.filter(Role.name == new_role.name).one()
            try:
                db.session.add(RolePermission(role_id=new_role.id, permission_id=permission_id))
                db.session.commit()
            except IntegrityError:
                logger.info(f"Role {role} with permission {permission_id} already exists")
                db.session.rollback()
