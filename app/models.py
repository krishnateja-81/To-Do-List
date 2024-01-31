from django.db import models

# Create your models here.


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    # requriedTime = models.IntegerField()
    # created = models.
    
    def __str__(self):
        
        return self.title
