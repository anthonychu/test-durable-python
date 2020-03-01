import logging
import json

import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    city = context.get_input()
    result = yield context.call_activity('HelloActivity', city)
    return result

main = df.Orchestrator.create(orchestrator_function)