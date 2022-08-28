from django.db import models
from .user import User

# CREATE TABLE `Contacts` (
#   `user_one` id,
#   `user_two` id,
#   `accepted` boolean
# );

class Contact(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    userList = models.CharField(max_length=255)
    accepted = models.BooleanField()