from django.db import models

class DataEntry(models.Model):
    REGION = models.CharField(max_length=100)
    PROVINCE = models.CharField(max_length=100)
    MUNICIPALITY = models.CharField(max_length=100)
    BARANGAY = models.CharField(max_length=100)
    HH_ID = models.CharField(max_length=50)
    ENTRY_ID = models.CharField(max_length=50, unique=True)
    FIRST_NAME = models.CharField(max_length=100)
    MIDDLE_NAME = models.CharField(max_length=100, blank=True, null=True)
    LAST_NAME = models.CharField(max_length=100)
    EXT_NAME = models.CharField(max_length=10, blank=True, null=True)
    BIRTHDAY = models.DateField()
    AGE = models.IntegerField()
    AGE_ON_EDUC = models.IntegerField()
    SEX = models.CharField(max_length=10)
    MEMBER_STATUS = models.CharField(max_length=50)
    RELATION_TO_HH_HEAD = models.CharField(max_length=100)
    CIVIL_STATUS = models.CharField(max_length=50)
    GRANTEE = models.BooleanField()
    HH_SET = models.CharField(max_length=50)
    SOLOPARENT = models.BooleanField()
    IPAFFILIATION = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"