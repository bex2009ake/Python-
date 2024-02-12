from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img')
    author = models.CharField(max_length=150)


    def __str__(self):
        return self.title


class ToDo(models.Model):
    title = models.CharField(max_length = 200)
    desc = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complate = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']