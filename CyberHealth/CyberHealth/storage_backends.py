from storages.backends.s3boto3 import S3Boto3Storage

class UploadStorage(S3Boto3Storage):
  location = 'uploads'
  file_overwrite = False
  default_acl = 'private'
  # MAYBE: set this to true by default unless there is an env var to flag to use default AWS space
  #        and only set this env var to false in cloudfoundry
  custom_domain = True    # defaults to True
