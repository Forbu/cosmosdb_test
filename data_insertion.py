"""
In this python module we will insert data into CosmosDB
in async way
"""

import pandas as pd
import os

from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.driver import client
from gremlin_python import statics as g

from gremlin_python.process.anonymous_traversal import traversal

import yaml     

# load remote-secure.yml
with open('remote-secure.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

print("connection config : ", config)

# connect to remote server
connection = DriverRemoteConnection(config['hosts'], 'g',
                                    username=config['username'],
                                    password=config['password'])

g = traversal().withRemote(connection)

print("connection established")

# count the number of vertices
print("Number of vertices : ", g.V().count().next())