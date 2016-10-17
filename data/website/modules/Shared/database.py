"""
.. module:: sqlmongo databases
    :platform: Unix
    :synopsis: Globally shared database connection
.. moduleauthor:: Lydia Dwyer
"""

from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine


db = SQLAlchemy()
mongo = MongoEngine()


"""
This is a shared database variable. It gets imported into all other Classes,
then initialized later with the Flask App.
"""
