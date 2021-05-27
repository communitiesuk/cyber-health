from django.db import models
from django.contrib.auth.models import User


class OrganisationType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class OrganisationRegion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    # Domain name length: The maximum length of each label is 63 characters, and a full
    # domain name can have a maximum of 253 characters
    # https://www.nic.ad.jp/timeline/en/20th/appendix1.html#:~:text=Format%20of%20a%20domain%20name,
    # a%20maximum%20of%20253%20characters.
    domain_name = models.CharField(max_length=253)

    organisation_type = models.ForeignKey(
        OrganisationType, on_delete=models.CASCADE)
    organisation_region = models.ForeignKey(
        OrganisationRegion, on_delete=models.CASCADE)
    organisation_users_info = models.ManyToManyField(User, through='OrganisationUser')

    def __str__(self):
        return self.name


class OrganisationUser(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    user_organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_info', 'user_organisation']]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

