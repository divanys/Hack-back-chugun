from typing import List
from configs.database_config import db
from configs.descriptors import Descriptor
from configs.api_settings import api_settings


__all__: List[str] = ["Descriptor", "db", "api_settings"]
