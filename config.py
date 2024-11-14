# app/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://fastapi_crossangry:ebb8edb23c3384f71d5005f25a09ed1a9ba80575@sxr81.h.filess.io/fastapi_crossangry"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
