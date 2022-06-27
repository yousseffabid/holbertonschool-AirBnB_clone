from imp import reload
from engine import file_storage

storage = file_storage()
reload(storage)
