from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
  bio_display_agreement = models.BooleanField(default=False,blank=True)
  comment_delete = models.BooleanField(default=False,blank=True)
  discription = models.TextField(default='', blank=True)

  def __str__(self):
    return str(self.user.username) + ' Profile'

  def save(self,*args,**kwargs):
    super().save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300 :
      output_size=(300,300)
      img.thumbnail(output_size)
      img.save(self.image.path)
