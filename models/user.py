#!/usr/bin/env python3
from models.base_model import BaseModel
import models


class User(BaseModel):
    email = str()
    password = str()
    first_name = str()
    last_name = str()
