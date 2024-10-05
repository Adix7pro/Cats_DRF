from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    CAT_TYPE_CHOICE = [
        ('male','Erkak'),
        ('female','Ayol'),
        ('kitten','Kichik'),
    ]

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    age = models.IntegerField()
    body = models.TextField()
    photo = models.ImageField(upload_to='images/',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cat_type = models.CharField(max_length=10,choices=CAT_TYPE_CHOICE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/" + str(self.id) + "/"

    class Meta:
        ordering = ["-id"]