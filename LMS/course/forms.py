# Model Forms
from django import forms

from .models import Course, Categorychoice, Levelchoice, TypeChoices



class CourseCreateForm(forms.ModelForm):

    class Meta:

        model = Course
        # fields = ['title', 'description', 'image', 'category', 'level', 'fee', 'offer_fee']
        # fields = '__all__'
        exclude = ['instructor','uuid','active_status',]

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Title',
                'required' : 'required',
            }),

            'image' : forms.FileInput(attrs={
                'class' : 'form-control',
                
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Description',
                'required' : 'required',
            }),
            'fee' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Fee',
                'required' : 'required',
            }),
            'offer_fee' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Course Offer Fee',
            }),
        }

    category = forms.ChoiceField(
        choices=Categorychoice.choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': 'required',
        })
    )
    level = forms.ChoiceField(
        choices=Levelchoice.choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': 'required',
        })
    )
    type = forms.ChoiceField(
        choices=TypeChoices.choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': 'required',
        })
    )

    def clean(self):

        validated_data = super().clean()

        if validated_data.get('fee') and validated_data.get('fee') < 0 :

            self.add_error('fee', 'course fee must be greater than 0')

        if validated_data.get('offer_fee') and validated_data.get('offer_fee') < 0 :

            self.add_error('offer_fee', 'offer fee must be greater than 0')
        
        return validated_data
    
    def __init__(self, *args, **kwargs):
        
        super(CourseCreateForm,self).__init__(*args, **kwargs)

        if not self.instance : 

            self.fields.get('image').widget.attrs['required'] = 'required'



