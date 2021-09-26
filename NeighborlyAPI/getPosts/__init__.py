import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://azurecosmoslab2:H4ZCB5LRYpnXVE1wTOMshS6B2zoHQ9tQHfhiHobmnSQ7BMvkyl5H3fPbqIe9erEmDLeYHvfjWx7QgxUqijvwgQ==@azurecosmoslab2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmoslab2@"  # TODO: Update with appropriate MongoDB connection information

        client = pymongo.MongoClient(url)
        logging.info('Past DB URL connection:')
        database = client['NeighborlyMongoDB']
        logging.info('Database reference obtained:')
        collection = database['posts']
        logging.info('Collection reference')
        logging.info(collection)
        logging.info(collection.find())
        result = collection.find({})
        logging.info(result)
        result = dumps(result)
        

        logging.info('Posts dump')
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)