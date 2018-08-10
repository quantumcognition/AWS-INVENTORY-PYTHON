import boto3
import botocore
import json
import config
import res.utils as utils


#  ------------------------------------------------------------------------
#
#    RDS 
#
#  ------------------------------------------------------------------------

def get_apigateway_inventory(ownerId, region_name):
    """
        Returns API Gateway inventory

        :param ownerId: ownerId (AWS account)
        :type ownerId: string
        :param region_name: region name
        :type region_name: string

        :return: API Gateway inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/apigateway.html
    """
    config.logger.info('API Gateway inventory, region {}, get_api_inventory'.format(region_name))

    client = boto3.client('apigateway', region_name)
    rds_list = client.get_rest_apis().get('items')

    return rds_list


#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')