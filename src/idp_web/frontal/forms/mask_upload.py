from django import forms

class MaskUploadForm(forms.Form):
    file_name = forms.CharField(max_length=50, label='File name',
            help_text='Also include the file format.')
    file = forms.FileField(
            label='Select a file',
            help_text='max. 42 megabytes'
        )
    file_type = forms.IntegerField()