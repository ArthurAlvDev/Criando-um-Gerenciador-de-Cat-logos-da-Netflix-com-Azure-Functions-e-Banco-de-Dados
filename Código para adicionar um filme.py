import logging
import azure.functions as func
import json
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = "https://<sua-conta-cosmos-db>.documents.azure.com:443/"
    key = "<sua-chave-cosmos-db>"

    client = CosmosClient(url, credential=key)
    database_name = 'NetflixCatalog'
    container_name = 'Movies'
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    try:
        req_body = req.get_json()
        movie = {
            'id': req_body.get('id'),
            'title': req_body.get('title'),
            'description': req_body.get('description'),
            'genre': req_body.get('genre')
        }

        container.create_item(body=movie)

        return func.HttpResponse(
            json.dumps(movie),
            mimetype="application/json",
            status_code=201
        )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
