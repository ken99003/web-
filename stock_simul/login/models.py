from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=255,
                               null=False)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)


class userData(models.Model):
  account = models.CharField(max_length=20,)
  password = models.CharField(max_length=30,
                              null=False)
  secPassword = models.CharField(max_length=30,
                                 null=False)