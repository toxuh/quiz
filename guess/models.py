from django.db import models


class Theme(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

class Description(models.Model):
    def __str__(self):
        return self.text

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    text = models.TextField()

class Word(models.Model):
    def __str__(self):
        return self.word

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    word = models.CharField(max_length=20)