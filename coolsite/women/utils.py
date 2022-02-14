from django.db.models import Count

from women.models import Category
from .constants import MENU, DEFAULT_MAX_ITEM_ON_PAGE


def get_menu_info():
    return MENU


class DataMixin:
    paginate_by = DEFAULT_MAX_ITEM_ON_PAGE

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))  # all not empty categories

        context['menu'] = get_menu_info()
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0  # if not on the current page - make the button clickable
        return context

