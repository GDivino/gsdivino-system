from django.db import models
from datetime import datetime

# Create your models here.
class FamMember(models.Model):
    name = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Dish(models.Model):
    meal_choices = [
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner")
    ]
    name = models.ForeignKey(FamMember, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(blank=True, null=True)
    meal = models.CharField(max_length=300, choices=meal_choices, null=True)
    objects = models.Manager()

    def __str__(self):
        return "{} for {} on {}".format(self.meal, self.name, self.date)

class Laundry(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.ForeignKey(FamMember, on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    def __str__(self):
        return "{}: {}".format(self.date, self.name)

class Aircon(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.ForeignKey(FamMember, on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    def __str__(self):
        return "{}: {}".format(self.date, self.name)

class WishList(models.Model):
    name = models.ForeignKey(FamMember, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    item = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="WishList", null=False, blank=True)
    link = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return "{}({}): {}. for {}. link: {}. {}".format(self.item, self.price, self.desc, self.name, self.link, self.image)

class Schedule(models.Model):
    place = models.CharField(max_length=300)
    event = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} for {} on {}. Link: {}".format(self.place, self.event, self.date)

class Bill(models.Model):
    status_list = [
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid")
    ]
    name = models.CharField(max_length=300)
    status = models.CharField(max_length=300, choices=status_list)
    price = models.FloatField(max_length=300)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.status, self.price)