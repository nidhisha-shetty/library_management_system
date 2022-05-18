from django import forms
from .models import Lib

class DateInput(forms.DateInput):
    input_type = 'date'

class Libraryform(forms.ModelForm):
	class Meta:
		model = Lib
		fields=[
			
			'book_name',
			
		]
		widgets = {
            'dob': DateInput(),
        }