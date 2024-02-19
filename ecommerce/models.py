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
    platform = models.CharField(max_length=15, blank=True, null=True)
    platform_user = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.uid
    
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    created_at = models.DateField()
    updated_at = models.DateField()


    def __str__(self):
        return self.id

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=15)
    summary = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    discount_type= models.CharField(max_length=15)
    discount_value= models.FloatField(blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.id
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)
    created_at = models.DateField()

    def __str__(self):
        return self.id


class Cart(models.Model):
    id= models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    status = models.CharField(max_length=15)
    created_at = models.CharField(max_length=15)
    updated_at = models.CharField(max_length=15)

    def __str__(self):
        return self.id
    
class CartItems(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.CharField(max_length=15)   

    def __str__(self):
        return self.cart_id
    

class Order(models.Model):
    id= models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.CharField(max_length=15)

    def __str__(self):
        return self.id
    
class Order_Lines(models.Model):
    id= models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.id
    

class Credential(models.Model):
    provider_id = models.CharField(max_length=15)
    provider_key = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.provider_id