from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Review

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20)
    #role = forms.ChoiceField(choices=User.ROLES)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1,6)]),
            'text': forms.Textarea(attrs={'rows':4}),
        }
