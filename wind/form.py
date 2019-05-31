from django import forms
from .models import Wind

class WindForm(forms.ModelForm):

    class Meta:
        model=Wind
        fields='__all__'
        widgets = {
            'WindSpeed': forms.TextInput(attrs={'placeholder': 'Enter value between 0.200 to 30'}),

        }

    def __init__(self, *args, **kwargs):
        super(WindForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['WindSpeed'].widget.attrs['style'] = 'width:250px; height:40px;'