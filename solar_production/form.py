from django import forms
from .models import solar

class SolarForm(forms.ModelForm):

    class Meta:
        model=solar
        fields='__all__'
        widgets = {
            'Solar_Elevation':forms.TextInput(attrs={'placeholder': 'Enter value between -69.228767 to 69.360406'}),
            'Cloud_Cover_Fraction':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Dew_Point':forms.TextInput(attrs={'placeholder': 'Enter value between -27.20 to 40'}),
            'Humidity_Fraction':forms.TextInput(attrs={'placeholder': 'Enter value between 0.14450 to 1'}),
            'Precipitation':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 41.1'}),
            'Pressure':forms.TextInput(attrs={'placeholder': 'Enter value between 958.400 to 1011.200'}),
            'Temperature':forms.TextInput(attrs={'placeholder': 'Enter value between -23 to 50'}),
            'Visibility':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 16.0930'}),
            'WindSpeed': forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 18.500'}),

        }

    def __init__(self, *args, **kwargs):

            super(SolarForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
            self.fields['Solar_Elevation'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Cloud_Cover_Fraction'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Dew_Point'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Humidity_Fraction'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Precipitation'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Pressure'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Temperature'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['Visibility'].widget.attrs['style'] = 'width:350px; height:40px;'
            self.fields['WindSpeed'].widget.attrs['style'] = 'width:350px; height:40px;'