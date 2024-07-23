import os
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError

def connect_to_s3_and_load_data():
    # Get the credentials from environment variables
    aws_access_key_id = os.getenv('aws_access_key_id')
    aws_secret_access_key = os.getenv('aws_secret_access_key')
    bucket = os.getenv('bucket')
    region = os.getenv('region')
    key = os.getenv('key')

    # Check if the credentials are available
    if aws_access_key_id is None or aws_secret_access_key is None or bucket is None or region is None or key is None:
        print("Error: Missing credentials")
        return

    # Create a session using the credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )

    # Create a S3 resource using the session
    s3 = session.resource('s3')

    # Try to download the file
    try:
        s3.Bucket(bucket).download_file(key, 'data.csv')
    except NoCredentialsError:
        print("Error: No credentials found")
        return

    # Load the data into a pandas DataFrame
    df = pd.read_csv('data.csv')

    # Print the top 5 rows of the DataFrame
    print(df.head(5))

    # Print data extraction successful
    print("Data extraction successful")

# Call the function
connect_to_s3_and_load_data()