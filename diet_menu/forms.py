from django import forms
from .models import MenuModel, CategoriesModel, VisitorsModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = ['title_en', 'title_ru', 'title_uz', 'description_en', 'description_ru', 'description_uz']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoriesModel
        fields = ['title_en', 'title_ru', 'title_uz']


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = VisitorsModel
        fields = ['views']
