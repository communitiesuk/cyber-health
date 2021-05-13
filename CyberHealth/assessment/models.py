from django.db import models
from django.utils.text import slugify


class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class PathwayGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    intro_text = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # If a slug is entered ensure it's formatted correctly
        if self.slug:
            self.slug = slugify(self.slug)

        # If blank, create slug from name
        else:
            self.slug = slugify(self.name)
        super(PathwayGroup, self).save(*args, **kwargs)


class Pathway(models.Model):
    long_name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=80, unique=True, blank=True)
    intro_text = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    pathway_group = models.ForeignKey(PathwayGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.long_name

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.short_name = self.long_name

        # If a slug is entered ensure it's formatted correctly
        if self.slug:
            self.slug = slugify(self.slug)

        # If blank, create slug from short name
        else:
            self.slug = slugify(self.short_name)

        super(Pathway, self).save(*args, **kwargs)
