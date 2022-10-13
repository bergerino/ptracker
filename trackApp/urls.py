from django.urls import path
from . import views

urlpatterns = [
    path('usop', views.track1, name='track1'),
    path('us', views.track2, name='track2'),
    path('ps', views.track3, name='track3'),
    path('dt', views.track4, name='track4'),
    path('fungujes', views.fungujes, name='fungujes'),
    path('', views.index, name='index')
]