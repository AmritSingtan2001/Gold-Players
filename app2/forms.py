from django import forms
from app.models import *
from about.models import *
from careers.models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AboutUSForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutUSForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'


class OrganizationSettingForm(forms.ModelForm):
    class Meta:
        model = OrganizationSetting
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrganizationSettingForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'


class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectiveForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'


class OfficeForm(forms.ModelForm):
    class Meta:
        model= Office
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(OfficeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'




class CareerCategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(CareerCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'


class CareerForm(forms.ModelForm):
    class Meta:
        model= Careers
        fields= '__all__'
        widgets = {
            'valid_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Enter valid date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CareerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'
            


''' testimonials '''
class TestimonialsForm(forms.ModelForm):
    class Meta:
        model= Testimonials
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(TestimonialsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'
            



# class MainCategorieForm(forms.ModelForm):
#     class Meta:
#         model = MainCategorie
#         fields = '__all__'

# class SubCategorieForm(forms.ModelForm):
#     class Meta:
#         model = SubCategorie
#         fields = '__all__'




# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = '__all__'

# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = '__all__'

# class HorizontalAdsForm(forms.ModelForm):
#     class Meta:
#         model = HorizontalAds
#         fields = '__all__'

# class HorizontalAdsForm(forms.ModelForm):
#     class Meta:
#         model = HorizontalAds
#         fields = '__all__'

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = ContactUs
#         fields = '__all__'
        
# class AboutUSForm(forms.ModelForm):
#     class Meta:
#         model = AboutUS
#         fields = '__all__'


# class PopUpAdsForm(forms.ModelForm):
#     class Meta:
#         model = PopUpAds
#         fields ='__all__'

# class VerticleAdsForm(forms.ModelForm):
#     class Meta:
#         model = VerticleAds
#         fields ='__all__'


# # class RadioStreamForm(forms.ModelForm):
# #     class Meta:
# #         model = RadioStream
# #         fields ='__all__'

# from django.forms.models import inlineformset_factory


# class FeatureForm(forms.ModelForm):
#     class Meta:
#         model = Feature
#         fields = ['title', 'description']  # Add any other fields you want to include in the form

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image']  # Add any other fields you want to include in the form

# ImageFormSet = inlineformset_factory(Feature, Image, form=ImageForm, extra=1)
        

