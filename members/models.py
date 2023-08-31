from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    put_date = models.DateTimeField()
    
    def str (self):
        return self.title
    