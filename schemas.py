#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional
from pydantic import BaseModel

# Impement Validations & credentials
class UserRequestModel(BaseModel):
    username: str
    email: str  # Optional[str] = None

class UserResonseModel(UserRequestModel):
    id: int
