import azure.functions as func
import pymongo
import json
import logging
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getAdvertisements trigger function processed a request.')
    try:
        url = "mongodb://azurecosmoslab2:H4ZCB5LRYpnXVE1wTOMshS6B2zoHQ9tQHfhiHobmnSQ7BMvkyl5H3fPbqIe9erEmDLeYHvfjWx7QgxUqijvwgQ==@azurecosmoslab2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmoslab2@"
        logging.info("connected")
        client = pymongo.MongoClient(url)
        database = client['NeighborlyMongoDB']
        collection = database['advertisements']
        logging.info("after collection")
        result = collection.find({})
        print("result"+result)
        
        print("----------result--------")
        result = dumps(result)
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

