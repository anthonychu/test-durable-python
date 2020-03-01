import logging

import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("HelloOrchestrator", None, "Seattle")
    return client.create_check_status_response(req, instance_id)