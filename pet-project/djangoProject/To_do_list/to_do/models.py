from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.tag


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tags")
