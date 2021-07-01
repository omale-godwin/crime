from django.db import models
from django.contrib.auth.models import User

from datetime  import datetime
from django.db.models.fields import CharField

from django.db.models.query_utils import PathInfo
# Create your models here.



class Evident(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    dates = models.CharField( max_length=200, default=datetime.now, blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    uuid = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return str(self.uuid)

class Weakness(models.Model):
    uuid = models.CharField(max_length=200, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    regnumber = models.CharField(max_length=200, blank=True, null=True)
    dats = models.DateTimeField(blank=True, default=datetime.now, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.uuid
)

class Report(models.Model):
    user_report = models.ForeignKey(Evident, on_delete=models.DO_NOTHING, blank=True, null=True)
    user_weakness = models.ForeignKey(Weakness, on_delete=models.DO_NOTHING, blank=True, null=True)  
    name = models.CharField(max_length=200)
    regnumber = models.CharField(max_length=200)
    dats = models.DateTimeField(blank=True, default=datetime.now)
    email = models.EmailField(max_length=200)
    casetype = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    emergency = models.BooleanField()
    def __str__(self):
        return self.regnumber


