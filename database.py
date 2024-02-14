#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# peewee is the ORM
from peewee import *
from config import PASSWORD

database = MySQLDatabase('fastapi2',
                         user='root',
                         password=PASSWORD,
                         host='localhost',
                         port=3306)

class User(Model):
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'