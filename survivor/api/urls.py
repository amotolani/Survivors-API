from django.urls import path
from .views import PassengerList, PassengerDetail, Ping


urlpatterns = [
    path('people', PassengerList.as_view(), name='List of Passengers'),
    path('people/<uuid>', PassengerDetail.as_view(), name='Passenger Details'),
    path('', Ping.as_view(), name='Ping'),
]

