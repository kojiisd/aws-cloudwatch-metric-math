import json
import datetime
import boto3
import os

client = boto3.client('cloudwatch')

def run(event, context):
    start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
    end_time = datetime.datetime.utcnow()
    period = 300
    
    response = client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/DynamoDB',
                    'MetricName': 'ProvisionedReadCapacityUnits',
                    'Dimensions': [
                        {
                            'Name': 'TableName',
                            'Value': 'CapacityUnitsTest'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
                'Unit': 'Count'
            },
            'Label': 'CalculationResult',
            'ReturnData': True
        },
        {
            'Id': 'm2',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/DynamoDB',
                    'MetricName': 'ConsumedReadCapacityUnits',
                    'Dimensions': [
                        {
                            'Name': 'TableName',
                            'Value': 'CapacityUnitsTest'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
                'Unit': 'Count'
            },
            'Label': 'CalculationResult',
            'ReturnData': True
        },
        {
            'Id': 'calculationResult',
            'Expression': 'm1/m2',
            'Label': 'CalculationResult',
            'ReturnData': True
        }
    ],
    StartTime=start_time,
    EndTime=end_time
)

    print(response)
    return 'Success'
