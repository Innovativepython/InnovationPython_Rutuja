from django.db import models


class Blogger(models.Model):
    title = models.CharField(max_length = 30) #title of the blog
    name = models.CharField(max_length = 20) # Name of blogger or author
    email = models.EmailField() # email address of the blogger
    comment = models.TextField() # comment


    def __str__(self):
        return '{} by {}'.format(self.title, self.name)
