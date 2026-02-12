from django.db import models


# If you wrote  'class Employee' Then it would just be a normal Python class, not connected to the database.
# models.Model = "Make this class a database table."

class tasks(models.Model):
    task_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_name