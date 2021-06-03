import boto3
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import TestCase
from assessment.models import UploadEvidence


class UploadEvidenceTestCase(TestCase):
    def setUp(self):
        self.s3 = boto3.resource('s3')
        self.test_user = User.objects.create(
            username='testuser', password='12345')
        self.test_evidence = UploadEvidence.objects.create(
            user=self.test_user,
            upload=SimpleUploadedFile('cool_file.txt', b'this is some sample file content')
        )
        self.temp_uploaded_url = self.test_evidence.upload.url


    def test_evidence_exists(self):
        self.assertIsNotNone(self.test_evidence.id)

    def test_evidence_is_uploaded(self):
        # connect to bucket
        bucket = self.s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        file_found = False
        expected_file_path = "uploads/" + self.test_evidence.upload.name
        # loop over files in bucket and assert that our file has been uploaded
        for file in bucket.objects.all():
            if file.key == expected_file_path:
                file_found = True
        self.assertTrue(file_found)
