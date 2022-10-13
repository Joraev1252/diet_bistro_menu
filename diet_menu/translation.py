from modeltranslation.translator import register, TranslationOptions
from diet_menu.models import MenuModel, CategoriesModel


@register(MenuModel)
class MenuTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(CategoriesModel)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['title']