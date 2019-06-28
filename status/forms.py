from django import forms
from status.models import Status
from django.contrib.auth.models import User


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = (
            'user',
            'content',
            'image',
        )

    # To limit the length of a content
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content
    
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Content or image is reauired.')
        return super().clean(*args, **kwargs)
