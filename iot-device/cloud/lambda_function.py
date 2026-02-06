def lambda_handler(event, context):
    print("Received IoT Data:", event)
    return {
        "statusCode": 200,
        "body": "Data processed successfully"
    }
