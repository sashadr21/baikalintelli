from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField


# Create your models here.
class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    academic_title = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"


class Relation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sience_theme = models.ForeignKey(SienceTheme, on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} {self.sience_theme}"


class SienceTheme(models.Model):
    title = models.TextField()
    slug = models.TextField()
    description = models.TextField()
    is_public = models.BooleanField()
    uri_pic = models.TextField()

    def __str__(self):
        return f"{self.title}"

class SchemaTableSection(models.Model):
    name = models.CharField()
    description = models.TextField()
    Json_field = models.JSONField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)


class LocalSienceTheme(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    parent = models.ForeignKey()
    description = models.TextField()
    content = models.TextField()
    date_series_start = models.DateField()
    geographical_position = models.TextField()
    is_show = models.BooleanField()

class DataSienceCollection(models.Model):
    local_theme=models.TextField()
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    date_series_start = models.DateField()
    date_series_end = models.DateField()
    content = models.TextField()
    geographical_position = models.TextField()
    scheme = models.ForeignKey(SchemaTableSection, on_delete=models.CASCADE)


class JSONCollection(models.Model):
    parent = models.ForeignKey(DataSienceCollection,on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    JSON_data = models.JSONField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.owner.name}"

class T_Relation(models.Model):
    theme = models.ForeignKey(SienceTheme,on_delete=models.CASCADE)
    local_theme = models.ForeignKey(LocalSienceTheme,on_delete=models.CASCADE)
    level = models.IntegerField()



