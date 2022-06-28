#!/usr/bin/env python3
from models.base_model import BaseModel
import models


class City(BaseModel):
    state_id = str()
    name = str()
