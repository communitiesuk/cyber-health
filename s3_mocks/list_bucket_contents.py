import boto3

s3 = boto3.resource('s3', endpoint_url="http://localhost:5000")

for bucket in s3.Bucket('cyber-health-assets-test').objects.all():
    print(bucket.key)