import boto3
import configparser

ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')

accesskey = ini['aws']['accesskey']
secretkey = ini['aws']['secretkey']
region = ini['aws']['region']
bucket_name = ini['aws']['bucket_name']

s3 = boto3.client('s3', 
                    aws_access_key_id=accesskey, 
                    aws_secret_access_key= secretkey, 
                    region_name=region)

filename = 'test_upload.csv'

s3.upload_file(filename,bucket_name,filename)
print("uploaded {0}".format(filename))
