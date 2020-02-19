#!/usr/bin/python3
"""
This module initialize the storage instance and reload the objects
"""
from models import base_model
from models import user
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
