from django.db import models

# Create your models here.
class Section(models.Model):
  name = models.CharField(max_length=255)
  body = models.TextField()

class Category(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField()
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Topic(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Stage(models.Model):
  pass

class Question(models.Model):
  framework_identifier = models.CharField(max_length=50, unique=True)
  label = models.TextField()
  stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
