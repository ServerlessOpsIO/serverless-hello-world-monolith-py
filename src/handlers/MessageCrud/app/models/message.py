'''Message related operations'''
import os

from datetime import datetime
from uuid import uuid4
import boto3

DDB_TABLE_NAME = os.environ.get('DDB_TABLE_NAME')
ddb_res = boto3.resource('dynamodb')
ddb_table = ddb_res.Table(DDB_TABLE_NAME)


def create_message(item: dict) -> dict:
    '''Transform item to put into DDB'''
    dt = datetime.utcnow()
    item['pk'] = str(uuid4())
    item['sk'] = 'v0'
    item['timestamp'] = int(dt.timestamp())

    r = ddb_table.put_item(
        Item=item
    )
    return {'message_id': item['pk']}


def retrieve_message(message_id: str) -> dict:
    '''Get item in DDB'''
    r = ddb_table.get_item(
        Key={
            'pk': message_id,
            'sk': 'v0'
        }
    )
    item = r.get('Item', {})

    return item


def update_message(message_id: str, item: dict) -> dict:
    '''Update item in DDB'''
    attribute_updates = {}
    for key in item.keys():
        attribute_updates[key] = {'Action': 'PUT', 'Value': item.get(key)}

    r = ddb_table.update_item(
        Key={
            'pk': message_id,
            'sk': 'v0'
        },
        AttributeUpdates=attribute_updates
    )
    return r


def delete_message(message_id: str) -> dict:
    '''Delete item in DDB'''
    r = ddb_table.delete_item(
        Key={
            'pk': message_id,
            'sk': 'v0'
        },
    )
    return r

