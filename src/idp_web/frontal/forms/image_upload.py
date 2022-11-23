from django import forms

class ImageUploadForm(forms.Form):
    file_name = forms.CharField(max_length=50)
    file = forms.FileField(
            label='Select a file',
            help_text='max. 42 megabytes'
        )
    file_type = forms.IntegerField()
