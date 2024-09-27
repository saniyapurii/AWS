import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB resource using boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# Specify the table name
table = dynamodb.Table('YourTableName') #your table name :- 'regex'

# Function to insert an item into DynamoDB
def put_item_to_dynamodb(primary_key_value, sort_key_value, additional_attributes):
    try:
        # Create the item data
        item = {
            'PrimaryKey': primary_key_value,  # Replace with your actual primary key attribute :- 'name' : primary_key_value
            'SortKey': sort_key_value  # Replace with your actual sort key (if applicable) :- 'lastname' : sort_key_value
        }
        
        # Add additional attributes to the item
        item.update(additional_attributes)

        # Insert the item using put_item()
        response = table.put_item(Item=item)
        
        # Print success message
        print("PutItem succeeded:", response)
    
    except ClientError as e:
        print(f"Error occurred while putting item into DynamoDB: {e.response['Error']['Message']}")

# Example usage of the function
put_item_to_dynamodb(
    primary_key_value="Saniya",   # Replace with actual primary key value
    sort_key_value="Puri", # Replace with actual sort key value (if applicable)
    additional_attributes={
        'Hobbies': 'Dance and Art',       # Replace with your custom attributes
        'Age': 24
    }
)




# Example usage of script
'''
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('regex') 

def put_item_to_dynamodb(primary_key_value):
    try:
        item = {
            'name': primary_key_value  
        }
        
        # Insert the item using put_item()
        response = table.put_item(Item=item)
        
        # Print success message
        print("PutItem succeeded:", response)
    
    except ClientError as e:
        print(f"Error occurred while putting item into DynamoDB: {e.response['Error']['Message']}")

put_item_to_dynamodb("Saniya")
'''