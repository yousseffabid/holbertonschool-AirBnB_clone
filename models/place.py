#!/usr/bin/env python3
from models.base_model import BaseModel
import models


class Place(BaseModel):
    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list(str())
