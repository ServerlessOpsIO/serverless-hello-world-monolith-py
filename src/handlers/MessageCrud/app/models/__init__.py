#!/usr/bin/env python
'''Shared code'''
from decimal import Decimal
import json

class DecimalEncoder(json.JSONEncoder):
    '''Convert decimal values returned by boto3 DDB deserializer'''
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

