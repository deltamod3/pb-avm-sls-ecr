import json

from utils.predict_price import get_price
from utils.response import response


def handler(event, context):
    request = json.loads(event.get('body'))
    price = float(get_price(request))
    
    return response(
        status_code=200,
        body={
            'price': price,
            'data': request,
        })
