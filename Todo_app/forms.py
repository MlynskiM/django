from django import forms

CONTENT_CHOICES= [
    ('shopping', 'Shopping'),
    ('school', 'School'),
    ('work', 'Work'),
    ('self_teach', 'Self-Teach'),
    ]

class NameForm(forms.Form):
    content = forms.CharField(label='Category', max_length=100, widget=forms.Select(choices=CONTENT_CHOICES))
    task = forms.CharField(label='To Do', max_length=100)

