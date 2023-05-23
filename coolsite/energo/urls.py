from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news/', EnergoNews.as_view(), name='news'),
    path('disclosure/', disclosure, name='disclosure'),
    path('activity/', activity, name='activity'),
    path('documents/', documents, name='documents'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', NewsCategory.as_view(), name='category'),
]