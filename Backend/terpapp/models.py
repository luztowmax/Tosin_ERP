from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from customers.models import Customer 
from inventory.models import Product



class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('ThenEmail field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff, True')
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects =UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Product(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    barcode = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def total_price(self):
        return self.quantity * self.product.price

    def save(self, *args, **kwargs):
        if not self.total:
            self.total = self.total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} - {self.customer.name}'
