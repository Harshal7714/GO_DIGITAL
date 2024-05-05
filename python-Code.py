import boto3
import pymysql
from botocore.exceptions import NoCredentialsError

def read_data_from_s3(bucket_name, file_name):
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='GO-DIGITAL-bucket', Key='Data-set.csv')
        data = response['Body'].read().decode('latin-1', errors='replace')
        return data
    except NoCredentialsError as e:
        print("AWS credentials not found:", e)
        return None

def push_to_rds(data):
    try:
        
        connection = pymysql.connect(host='db.cp0yay242i6r.us-east-1.rds.amazonaws.com',
                                     user='admin1',
                                     password='admin123',
                                     database='db')
        
        with connection.cursor() as cursor:
            
            sql = "INSERT INTO your_table (column_name) VALUES (%s)"
            cursor.execute(sql, (data,))
        
        connection.commit()
        print("Data pushed to RDS successfully")
    except Exception as e:
        print("Error pushing data to RDS:", e)

def push_to_glue_database(data):
    try:
        
        print("Data pushed to Glue Database")
    except Exception as e:
        print("Error pushing data to Glue Database:", e)

if __name__ == "__main__":
    
    bucket_name = 'GO-DIGITAL-bucket'
    file_name = 'Data-set.csv'
    data = read_data_from_s3(bucket_name,file_name)
    
    if data:
        
        push_to_rds(data)
    else:
        
        push_to_glue_database(data)
