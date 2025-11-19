from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

followers = db.Table(
    "followers",
    db.Column("user_from_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("user_to_id", db.Integer, db.ForeignKey("users.id"))
)

class User(db.Model):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)

    posts: Mapped[List["Post"]]= relationship(back_populates="user")
    comments: Mapped[List["Comment"]]= relationship(back_populates="user")

    #no se como establecer la relationship con la tabla followers de arriba sacando los dos user from id y user to id de aqui.

    
class Post(db.Model):
    __tablename__= "posts"   
    id: Mapped[int] = mapped_column(primary_key=True)
    

    user_id:Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"), nullable=False)
    user: Mapped["User"]= relationship(back_populates="posts")
    medias: Mapped[List["Media"]]= relationship(back_populates="post")
    comment: Mapped[List["Comment"]]= relationship(back_populates="post")

    

class Media(db.Model):
    __tablename__= "medias"
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)#aqui nose como poner el enum en mapped con Enum me da error al migrar
    
    post_id:Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"), nullable=False)
    post:Mapped["Post"]= relationship(back_populates="medias")


class Comment(db.Model):
    __tablename__= "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    

    author_id:Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"), nullable=False)
    user: Mapped["User"]= relationship(back_populates="comments")

    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"), nullable=False)
    post: Mapped["Post"]= relationship(back_populates="comment")
