from models.engine.file_storage import FileStorage

globalClasses = ('BaseModel', 'User', 'State',
                 'Amenity', 'City', 'Place', 'Review')
storage = FileStorage()
storage.reload()
