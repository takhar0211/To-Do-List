from django.db import models


# If you wrote  'class Employee' Then it would just be a normal Python class, not connected to the database.
# models.Model = "Make this class a database table."

class tasks(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name