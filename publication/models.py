from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    food_type = models.TextField(max_length=3000)
    rest_pic = models.FileField(upload_to='')
    def __str__(self):
        return self.restaurant_name

class Review(models.Model):
    writer = models.CharField(max_length=40, default="anonymous")
    pub_date = models.DateTimeField(default=timezone.now)
    stars_nums = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=stars_nums)
    detail = models.TextField(max_length=4000, default="Type here your review.")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.restaurant.restaurant_name   