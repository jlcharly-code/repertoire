from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip Hop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'

    name = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50, choices=Genre.choices, default=Genre.HIP_HOP)
    biography = models.TextField(max_length=1000) # TextField is better for long text
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2029)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip Hop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'
    title = models.CharField(max_length=200)  # Added this
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL, related_name='listings')
    genre = models.CharField(max_length=50, choices=Genre.choices, default=Genre.HIP_HOP)

    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)  # Optional: auto timestamp

    def __str__(self):
        return f"Listing for {self.band.name if self.band else 'Unknown Band'}"