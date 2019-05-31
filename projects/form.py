from django import forms
from .models import energy

class EnergyForm(forms.ModelForm):

    class Meta:
        model=energy
        fields='__all__'
        widgets = {
            'Month':forms.TextInput(attrs={'placeholder': 'Enter value between 1 to 12'}),
            'Day':forms.TextInput(attrs={'placeholder': 'Enter value between 1 to 31'}),
            'Hour':forms.TextInput(attrs={'placeholder': 'Enter value between 1 to 24'}),
            'Age_lt_5':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 58.163670'}),
            'Age_range_5_to_18':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 151.225543'}),
            'Age_range_18_to_25':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 581.636704'}),
            'Age_range_25_to_65':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 1163.273409'}),
            'Age_gt_65':forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 814.291386'}),
            'Days_of_week':forms.TextInput(attrs={'placeholder': 'Enter value between 1 to 7'}),
            'School_Day':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or  1'}),
            'Cloud_Cover_Fraction': forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Dew_point': forms.TextInput(attrs={'placeholder': 'Enter value between -31.7000 to 24.4000'}),
            'Humidity_Fraction': forms.TextInput(attrs={'placeholder': 'Enter value between 0.14450 to 1'}),
            'Precipitable_Water': forms.TextInput(attrs={'placeholder': 'Enter value between 3 to 45'}),

            'Temperature': forms.TextInput(attrs={'placeholder': 'Enter value between -27 to 50'}),
            'Visibility': forms.TextInput(attrs={'placeholder': 'Enter value between 0 to 34'}),

            'Sector_FOOD_SERVICE':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_Grocery':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_K12_school':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_Lodging':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_office':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_residental':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),
            'Sector_STAND_ALONE_RETAIL':forms.TextInput(attrs={'placeholder': 'Enter value either 0 or 1'}),


        }
    def __init__(self, *args, **kwargs):

            super(EnergyForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
            self.fields['Month'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Day'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Hour'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Age_lt_5'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Age_range_5_to_18'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Age_range_18_to_25'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Age_range_25_to_65'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Age_gt_65'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Days_of_week'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['School_Day'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Cloud_Cover_Fraction'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Dew_point'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Humidity_Fraction'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Precipitable_Water'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Temperature'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Visibility'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_FOOD_SERVICE'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_Grocery'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_K12_school'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_Lodging'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_office'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_residental'].widget.attrs['style'] = 'width:300px; height:40px;'
            self.fields['Sector_STAND_ALONE_RETAIL'].widget.attrs['style'] = 'width:300px; height:40px;'
