import os
import json

with open('/etc/flaskersonconfig.json') as config_file:
	config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    BASIC_AUTH_USERNAME = config.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = config.get('BASIC_AUTH_PASSWORD')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
