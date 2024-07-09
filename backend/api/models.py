from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) # with the arg, we tell it to automatically populate instead of having the user type something in
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
          # * break down of line 9:
          # models as it will come from a model, 
          # foreignKey as it will come from a different data source
          # user as it will come from that data source
          # on delete as we want it to delete all the notes this user has
          # related name as we want a name on the user to reference all of its notes 

  def __str__(self):
    return self.title