from django.db import models


class Header(models.Model):
    publication_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('Published in')
    def __str__(self):
        return self.publication_title

class Grade(models.Model):
    grade = models.ForeignKey(Header, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    stars_qty = models.IntegerField(default=0)
    def __str__(self):
        return self.description
    