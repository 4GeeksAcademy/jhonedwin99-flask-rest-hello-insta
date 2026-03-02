from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Usuarios(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    seguidores: Mapped[List["Seguidores"]] = relationship(
        back_populates="usuarios")
    post: Mapped[List["Post"]] = relationship(back_populates="usuarios")
    comments: Mapped[List["Post"]] = relationship(back_populates="usuarios")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Seguidores:
class Seguidores(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    seguidor_id: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    seguido_id: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuarios: Mapped["Usuarios"] = relationship(back_populates="seguidores")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Post:
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    id_user: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    comments: Mapped[List["Comments"]] = relationship(back_populates="post")
    media: Mapped[List["Media"]] = relationship(back_populates="post")

    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuarios: Mapped["Usuarios"] = relationship(back_populates="post")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# Tabla Comments:
class Comments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    id_author: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    id_post: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# Tabla Media:


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    url: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    id_post: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="media")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }