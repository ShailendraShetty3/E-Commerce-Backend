from django.db import models

class User(models.Model):
    # Define your fields here
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


