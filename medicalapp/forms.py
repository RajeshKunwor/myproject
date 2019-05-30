from .models import *
from mptt.forms import TreeNodeChoiceField
from django import forms

class MedicineCategoryForm(forms.Form):

    category = TreeNodeChoiceField(queryset=MedicineCatetory.objects.all()
                                   , level_indicator=u'+--')
    name = forms.CharField(max_length=100)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = MedicineCatetory
        fields = '__all__'