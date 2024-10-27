from django.urls import path
from hero import views
urlpatterns=[
    path("1",views.func1),
    path("2",views.func2),
    path("3",views.func3)
    
]