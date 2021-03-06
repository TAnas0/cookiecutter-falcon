# -*- coding: utf-8 -*-
"""
Docker settings file
"""
# Local imports
# Third-party imports
{% if cookiecutter.use_mongodb == "y" %}
import pymongo
{% endif %}{% if cookiecutter.use_redisdb == "y" %}
from redis import StrictRedis
{% endif %}

# Local imports
from .base import *  # Needs to be removed


{% if cookiecutter.use_mongodb == "y" %}
MONGO_DB = pymongo.MongoClient('mongodb')
{% endif %}{% if cookiecutter.use_redisdb == "y" %}
REDIS_DB = StrictRedis('redisdb')
{% endif %}
