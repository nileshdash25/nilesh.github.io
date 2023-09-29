from django.urls import path
from Testapp import views
urlpatterns = [
    path('Database/',views.Temp),
    path('LoginForm/',views.LogiN),
]