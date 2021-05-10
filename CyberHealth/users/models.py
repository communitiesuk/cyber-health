from django.db import models
from django.contrib.auth.models import AbstractUser
from assessment import models as assessment_models


class User(AbstractUser):
    organisations = models.ManyToManyField(assessment_models.Organisation, through='OrganisationUser')


class OrganisationUser(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    user_organisation = models.ForeignKey(assessment_models.Organisation, on_delete=models.CASCADE)

