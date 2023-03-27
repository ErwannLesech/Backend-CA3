from django import forms
from .models import Motorcycle

# This file defines a form to create a new 
# Motorcycle object using the Django forms library.

class CreateNewMotorcycle(forms.ModelForm):
    # The Meta class specifies the model and fields that the form should 
    # include. In this case, the model is Motorcycle and the fields 
    # are motorcycle_text, motorcycle_brand, motorcycle_description, 
    # and pub_date.
    class Meta:
        model = Motorcycle
        fields = ['motorcycle_text', 'motorcycle_brand', 'motorcycle_description', 'pub_date']

    #Each field corresponds to a field in the Motorcycle model and is 
    # defined using the CharField or DateTimeField classes. The label parameter 
    # provides a user-friendly label for the field. The max_length parameter 
    # specifies the maximum length of the field.

    motorcycle_text = forms.CharField(label="Motorcycle Name", max_length=200)
    motorcycle_brand = forms.CharField(label="Brand", max_length=20)
    motorcycle_description = forms.CharField(label="Description", max_length=200)
    pub_date = forms.DateTimeField(label="Date Published")

# possible extension with review model

"""class CreateNewReview(forms.ModelForm):
    class Meta:
        model = MotorcycleReview
        fields = ['name', 'review_text', 'pub_date']
        labels = {
            'name': 'Name:',
            'review_text': 'Review:',
            'pub_date': 'Date Published:'
        }
    name = forms.CharField(label="Name", max_length=200)
    review_text = forms.CharField(label="Review", max_length=200)
    pub_date = forms.DateTimeField(label="Date Published")"""