import uuid

from django.db import models


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="employees", null=True, default="employees/employee")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
