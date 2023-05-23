from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О компании', 'url_name': 'about'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        #{'title': 'Раскрытие информации', 'url_name': 'disclosure'},
        #{'title': 'Направленная деятельность', 'url_name': 'activity'},
        #{'title': 'Документы', 'url_name': 'documents'},
        #{'title': 'Контакты', 'url_name': 'contacts'},
        #{'title': 'Войти', 'url_name': 'login'},
        {'title': 'Добавить новость', 'url_name': 'add_page'}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = cache.get('cats')
        # if not cats:
        cats = Category.objects.annotate(Count('news'))
            # cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(4)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
