from django.db import models


# CREATE TABLE `Languages` (
#   `id` int,
#   `name` varchar(255)
# );

class Languages (models.Model):
    name = models.CharField(max_length=255)