from django.core.cache import cache

from django.db.models import Count
from .models import *



menu = [
        {'title': 'Расписание', 'url_name': 'schedule'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Новости', 'url_name': 'news'}
        ]


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = cache.get('cats')
        # if not cats:
        #     cats = Category.objects.annotate(Count('women'))
        #     cache.set('cats', cats, 60)
        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
        context['menu'] = user_menu
        # context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context