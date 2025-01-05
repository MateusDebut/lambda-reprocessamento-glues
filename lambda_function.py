from app import app


def lambda_handler(event, context):
    if "httpMethod" in event:
        return app(event)

    return {
        "statusCode": 400,
        "body": '{"error": "Requisição inválida"}',
        "headers": {"Content-Type": "application/json"}
    }
