from django import forms

from .models import Prayer


class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ["title", "content"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter prayer title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Write your prayer here...',
                'rows': 4
            }),
        }
