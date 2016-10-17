from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

CODE_TEXT_LENGTH = 100
SHORT_TEXT_LENGTH = 500
LONG_TEXT_LENGTH = 2000

class References(models.Model):
	title = models.CharField(null=False, max_length=CODE_TEXT_LENGTH)
	description = models.CharField(max_length=LONG_TEXT_LENGTH)
	location = models.CharField(max_length=CODE_TEXT_LENGTH)
	complexity = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

