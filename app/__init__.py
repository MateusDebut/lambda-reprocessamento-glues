def app(event):
    http_method = event["httpMethod"]
    path = event["path"]

    if http_method == "GET" and path == "/clientes":
        return {
            "statusCode": 200,
            "body": '{"message": "Lista de clientes"}',
            "headers": {"Content-Type": "application/json"}
        }

    elif http_method == "POST" and path == "/clientes":
        return {
            "statusCode": 201,
            "body": '{"message": "Cliente criado com sucesso"}',
            "headers": {"Content-Type": "application/json"}
        }

    return {
        "statusCode": 404,
        "body": '{"error": "Recurso não encontrado"}',
        "headers": {"Content-Type": "application/json"}
    }
