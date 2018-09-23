from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'photo']
        # 필드에 대해서 오류가 없을경우 form_valid가 호출된다