'''Message operation routes'''
from json import dumps as jsondump

from flask import Blueprint, jsonify, request

from app import models

message = Blueprint('message', __name__)


@message.route('/message', methods=['POST'])
def create_message():
    '''Create message'''
    item = request.get_json(force=True)
    message_id = models.message.create_message(item)
    response = {
        'success': True,
        'message': message_id
    }
    status_code = 200
    return jsonify(response), status_code


@message.route('/message/<message_id>', methods=['GET'])
def retrieve_message(message_id):
    '''Retrieve message'''
    response = models.message.retrieve_message(message_id)
    status_code = 200
    return jsondump(response, cls=models.DecimalEncoder), status_code


@message.route('/message/<message_id>', methods=['PUT'])
def update_message(message_id):
    '''Update message'''
    item = request.get_json(force=True)
    models.message.update_message(message_id, item)
    response = {'success': True}
    status_code = 200
    return jsonify(response), status_code


@message.route('/message/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    '''Delete message'''
    models.message.delete_message(message_id)
    response = {'success': True}
    status_code = 200
    return jsonify(response), status_code


