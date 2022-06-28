#!/usr/bin/env python3
from models.base_model import BaseModel
import models


class Review(BaseModel):
    place_id = str()
    user_id = str()
    text = str()
