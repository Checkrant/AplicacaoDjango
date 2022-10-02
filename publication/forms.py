from .models import Grade
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["writer","stars","detail"]
