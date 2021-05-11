from django.db import models
from django.contrib.auth.models import User
from assessment import models as assessment_models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=35)

    def __str__(self):
        return self.user.email


# class OrganisationUser(models.Model):
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     user_organisation = models.ForeignKey(assessment_models.Organisation, on_delete=models.CASCADE)

