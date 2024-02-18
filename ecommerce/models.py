from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Social(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    platform = models.CharField(max_length=15)
    platform_user = models.CharField(max_length=15)

    def __str__(self):
        return self.uid


class Cart(models.Model):
    id= models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    status = models.CharField(max_length=15)
    created_at = models.CharField(max_length=15)
    updated_at = models.CharField(max_length=15)

    def __str__(self):
        return self.id
    

class Order(models.Model):
    id= models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.CharField(max_length=15)

    def __str__(self):
        return self.id
    

class Credential(models.Model):
    provider_id = models.CharField(max_length=15)
    provider_key = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.provider_id