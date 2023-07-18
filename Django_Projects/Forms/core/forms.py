from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import Person


class PersonForm(forms.ModelForm):
    MIN_BIRTH_YEAR = 1900
    MAX_BIRTH_YEAR = 2018
    birth_year = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_BIRTH_YEAR), MaxValueValidator(MAX_BIRTH_YEAR)]
    )
    dick_length = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(5), MaxValueValidator(45)]
    )

    class Meta:
        model = Person
        fields = ("full_name", "birth_year", "hobby", "dick_length")

