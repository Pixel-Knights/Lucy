from django.db import models
from datetime import datetime

class System_config(models.Model):

    config_content = models.CharField(max_length=200,null=False,blank=False)
    config_date= models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.nome


# Create your models here.
