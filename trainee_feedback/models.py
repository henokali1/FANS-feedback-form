from django.db import models

class TraineeFeedback(models.Model):
    questionOne = models.CharField(max_length=3)
    questionTwo = models.CharField(max_length=17)
    questionThree = models.CharField(max_length=17)
    questionFour = models.CharField(max_length=17)
    questionFive = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

