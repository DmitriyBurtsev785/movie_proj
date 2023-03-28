from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=40) # максимальная длина строки
    rating = models.IntegerField # можно без параметров
    # колонку id не создаю, автоматически создастся в тот момент, когда ползуюсь моделями