import pdb
import boto3

s3 = boto3.resource('s3', endpoint_url="http://localhost:5000")
bucket = s3.Bucket('cyber-health-assets-test')
bucket_contents = bucket.objects.all()

for bucket in bucket_contents:
    print(bucket.key)

pdb.set_trace()
pass
