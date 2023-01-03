from django import forms
from .models import user_signup,book_issue,contactus

class u_signup(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'

class issue_book(forms.ModelForm):
    class Meta:
        model=book_issue
        fields='__all__'

class contact(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'