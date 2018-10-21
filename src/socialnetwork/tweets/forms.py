from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.Textarea(
                attrs={"placeholder":"Tweet","class":"form-control"}
                ))
    class Meta:
        model = Tweet
        fields = [
                    #"user",
                    "content"
                 ]
