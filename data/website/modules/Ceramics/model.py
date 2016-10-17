#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Ceramics Model class for the SQLMongo."""

from modules.Shared.database import mongo
from mongoengine import Document
from mongoengine import StringField, IntField


class Ceramic(mongo.Document):

    """Ceramic object model

    This is a Document class, used as a generic data container. It is an extension
    of the MongoEngine class, and inherits various common database actions.
    """
    
    

    ceramic_type = StringField(max_length=128, required=True)
    ceramic_ware = StringField(max_length=128, required=True)
    ceramic_form = StringField(max_length=128, required=True)
    ceramic_reg_id = IntField(max_length=128, required=True)
    date_period = StringField(max_length=128, required=True)
    excavated_from = StringField(max_length=128, required=True)



