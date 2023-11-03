from django.contrib.auth.models import User
from django.db import models
from djongo import models
import uuid
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return str(self.name)

def generate_item_number():
    return str(uuid.uuid4())[:8].replace('-', '').upper()

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    item_number= models.CharField(max_length=8, unique=True, default= generate_item_number)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    published_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='new')
   
    def __str__(self):
        return str(self.name)