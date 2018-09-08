from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    # category와 shop을 1:N의 관계로
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    comment = models.TextField()
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.creator

# class Order(models.Model):
#     pass
