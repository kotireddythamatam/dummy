from django.db import models

# Create your models here.
class Registration_Model(models.Model):

    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    email_id=models.EmailField()
    password=models.CharField(max_length=10)
    conform_password=models.CharField(max_length=10)
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __dir__(self):
        return self.first_name
