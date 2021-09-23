import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://azurecosmoslab2:H4ZCB5LRYpnXVE1wTOMshS6B2zoHQ9tQHfhiHobmnSQ7BMvkyl5H3fPbqIe9erEmDLeYHvfjWx7QgxUqijvwgQ==@azurecosmoslab2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmoslab2@"  
            client = pymongo.MongoClient(url)
            database = client['NeighborMongoDB']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )