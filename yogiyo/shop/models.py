from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.urls import reverse
from jsonfield import JSONField


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category_detail", args=[self.pk])
    


class Shop(models.Model):
    # category와 shop을 1:N의 관계로
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()  # PostgreSQL의 JSONField와 다르다.

    def __str__(self):
        return self.name

    @property
    def address(self):
        # meta(JSONField)에 받은 address를 불러오기만 하겠다.
        return self.meta.get('address')


class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()

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
