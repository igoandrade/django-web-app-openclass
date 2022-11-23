from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.TextField(default='')
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)],
        default=2000
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHONG = 'C'
        MISCELLANEOUS = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.TextField(default='')
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)],
        default=2000
    )
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=50)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"
