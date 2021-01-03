from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_category = models.CharField(max_length=20)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date inserted')
    s_type = models.CharField(default="undone",max_length=20)

    def __str__(self):
        return self.task_text
