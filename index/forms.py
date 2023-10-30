from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your name',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Enter your name"',
                'class': 'common-input mb-20 form-control',
                }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your email',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Enter your email"',
                'class': 'common-input mb-20 form-control',
                'pattern': '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$'
                }
        )
    )
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your subject',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Enter your subject"',
                'class': 'common-input mb-20 form-control',
                }
        )
    )
    message = forms.CharField(
        required=True,  
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter your message',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Enter your message"',
                'class': 'common-textarea form-control',
                }
        ),
    )

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']