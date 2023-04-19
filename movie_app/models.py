from django.db import models

# Create your models here.



class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    name = models.CharField(max_length=40) # максимальная длина строки
    rating = models.IntegerField() # можно без параметров
    # колонку id не создаю, автоматически создастся в тот момент, когда ползуюсь моделями
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return f'{self.name}-{self.rating}%'
