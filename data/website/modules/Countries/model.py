#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Countries Model class for the SQLMongo project."""

from modules.Shared.database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# http://flask-sqlalchemy.pocoo.org/2.1/models/
class Country(db.Model):

    """Country object model

    This is a Model class, used as a generic data container. It is an extension
    of the SQLAlchemy class, and inherits various common database actions.
    """

    __tablename__ = 'countries'

    
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String(128), unique=True)
    country_abrev = Column(String(128), unique=True)
    country_created = Column(DateTime)


    def __init__(self, country_name="", country_abrev=""):
        self.country_name = country_name
        self.country_abrev = country_abrev
