
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/
    url(r'^mainboard/$', views.mainboard, name='mainboard'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # insert into wishList
    url(r'^insertwishlist/$', views.insertwishlist, name='insertwishlist'),
    url(r'^search/$', views.search, name='search'),
    url(r'^deletepost/$', views.deletepost, name='deletepost'),
    url(r'^searchupdate/$', views.searchupdate, name='searchupdate'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profileupdate/$', views.profileupdate, name='profileupdate'),
    url(r'^autocomplete/', views.autocomplete, name='autocomplete'),
]
