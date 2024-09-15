from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    roll_no = models.IntegerField(unique=True, null=False)  # Roll number should be unique
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default="")  # Use CharField for phone numbers to handle different formats
    email = models.EmailField(unique=True, null=False)  # Added email field
    date_of_birth = models.DateField(null=True, blank=True)  # Optional DOB
    add_date = models.DateField(auto_now_add=True)  # Auto-set the date when the student is added
    gender = models.CharField(max_length=10, null=True, blank=True)  # Added gender field

    def clean(self):
        if not (1000 <= self.roll_no <= 9999):
            raise ValidationError("Roll number must be exactly 4 digits.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.roll_no}"
