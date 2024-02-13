from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Social(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, default=...)
    platform = models.CharField(max_length=15)
    platform_user = models.CharField(max_length=15)

    def __str__(self):
        return self.user_id

