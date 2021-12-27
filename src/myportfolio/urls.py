from django.urls import path
from . views import experiences, index, send_message
urlpatterns = [
    path('', index, name="index"),
    path('contact/', send_message, name="send_message"),
    path('experience/', experiences, name="experiences"),



]