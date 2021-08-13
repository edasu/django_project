from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#default argument wil allow you to change the date later on
#when we want to create updated date then we use 'auto_now=True',
#'auto_now_add=True' that whould et post the currrent date time only then this object created
#but whit this you cannot ever update the date time you created
#when we delete the user wee will delte the post they post as well on_delete= models.CASCADE
    def __str__(self):
        return self.title
