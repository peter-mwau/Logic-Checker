from django.db import models

class Records_log(models.Model):
    Prompt = models.CharField(max_length=100)
    Response = models.CharField(max_length=100)
    Time = models.DateTimeField(auto_now_add=True)