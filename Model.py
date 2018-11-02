from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Idiom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    idiom_id = db.Column(db.Integer, db.ForeignKey('idiom.id'), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class IdiomSchema(ma.Schema):
    id = fields.Integer(required=True)
    text = fields.String(required=True)
