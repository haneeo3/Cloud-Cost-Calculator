import json
import boto3
from datetime import datetime, timezone

def lambda_handler(event, context):
    client = boto3.client('ce', region_name='us-east-1')
    
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    
    response = client.get_cost_and_usage(
        TimePeriod={'Start': today, 'End': today},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    
    cost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:770854396539:Default_CloudWatch_Alarms_Topic',
        Subject='Daily AWS Cost',
        Message=f'Today\'s AWS cost is ${cost}'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Daily cost sent: ${cost}')
    }
