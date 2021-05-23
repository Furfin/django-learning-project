from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(default=None, upload_to='post_pics')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
    def save(self,*args,**kwargs):
        
        if not self.image:
            super().save()
        else:
            super().save()
            
            img = Image.open(self.image.path)

            if img.height > 800 or img.width > 800 :
                output_size=(600,600)
                img.thumbnail(output_size)
                img.save(self.image.path)
        

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,default=None)
    author = models.CharField(max_length=50 ,default='anonimus')
    def __str__(self):
        return self.content

    