from django.db import models

# Create your models here.
class ApiView(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField(null=True)
    stu_class = models.IntegerField(null=True)

    def __str__(self):
        return self.stu_name