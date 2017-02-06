from django.db import models

class Parent(models.Model):

    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname

class Child(models.Model):

    class Meta:
        # fix pluralisation on admin site so it doesn't
        # say 'childs'
        verbose_name_plural = "children"

    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()

    parent = models.ForeignKey(Parent)

    def __str__(self):
        return self.firstname
