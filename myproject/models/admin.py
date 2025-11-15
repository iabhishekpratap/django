from django.contrib import admin

# Register your models here.


from .models import Student  # Import the Student model you just made

# Tell the admin site to show the Student model
admin.site.register(Student)