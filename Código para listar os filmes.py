import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = "https://<sua-conta-cosmos-db>.documents.azure.com:443/"
    key = "<sua-chave-cosmos-db>"

    client = CosmosClient(url, credential=key)
    database_name = 'NetflixCatalog'
    container_name = 'Movies'
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    movies = list(container.read_all_items())

    return func.HttpResponse(
        json.dumps(movies),
        mimetype="application/json",
        status_code=200
    )
