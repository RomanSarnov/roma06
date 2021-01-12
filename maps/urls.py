from django.urls import path
from maps.views import AddCoordsView, MapsView, CoordsView

urlpatterns = [
    path('', MapsView.as_view(), name='maps'),
    path('add-coords/', AddCoordsView.as_view(), name='add-coords'),
    path('coords/', CoordsView.as_view(), name='coords')
]
