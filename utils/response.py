import json
from typing import Union

HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
    'Access-Control-Allow-Credentials': True,
}


def response(status_code: int, body: Union[dict, list] = None):
    res = {
        'headers': HEADERS,
        'statusCode': status_code,
    }

    if body is not None or isinstance(body, list):
        res.update({'body': json.dumps(body)})
    return res