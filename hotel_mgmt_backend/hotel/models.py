from django.db import models
import datetime
from datetime import datetime
import pytz

# Option for the idnetities:
Identity_proof = [
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
    ("Voter ID", "Voter ID"),
    ("Driving License", "Driving License")
]

# option for the food
food_category = [
    ("Starter", "Starter"),
    ("Main Course", "Main Course"),
    ("Dessert", "Dessert"),
    ("Snack", "Snack"),
    ("Breakfast", "Breakfast")
]


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    phone_no = models.CharField(max_length=10,blank=False)
    email = models.EmailField(max_length = 254)
    room_no = models.CharField(max_length=50,blank=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField() 
    identity_proof_number = models.CharField(max_length=50,blank=False)
    identity_type = models.CharField(max_length=50,choices=Identity_proof,blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    price = models.IntegerField(blank=False)
    category = models.CharField(max_length=50,choices=food_category) 

    def __str__(self):
        return self.name 

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="order")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name 
    

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_item")
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,related_name="order_item")
    quantity = models.IntegerField() 

    def __str__(self):
        return f"Order {self.order.id} - {self.order.customer.name}"
    
class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="bill")
    total_amount = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.order.customer.name} - {self.total_amount}"