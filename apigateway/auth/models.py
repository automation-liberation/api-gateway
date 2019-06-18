from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from apigateway.database import db


class RolePermission(db.Model):
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permission.id'), primary_key=True)


class Role(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    role_permissions = relationship('RolePermission', backref='role', primaryjoin=id == RolePermission.role_id)


class Permission(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    service = Column(String)
    role_permissions = relationship('RolePermission', backref='permission', primaryjoin=id == RolePermission.permission_id)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role', primaryjoin=role_id == Role.id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        return self.role.name == 'admin'
