import pdb
import boto3

s3 = boto3.resource('s3', endpoint_url="http://localhost:5000")
try:
    bucket = s3.Bucket('cyber-health-assets-test')
    bucket_contents = bucket.objects.all()

    for file in bucket_contents:
        print(file.key)

    pdb.set_trace()
    pass
except s3.meta.client.exceptions.NoSuchBucket as err:
    print(err)
    print("Fake Bucket not found - try e.g. running tests")
