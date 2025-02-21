import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/malaria_vision_ai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False