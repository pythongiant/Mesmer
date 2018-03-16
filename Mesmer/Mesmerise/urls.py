from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.start,name="start"),
    path('signAction',views.SignAction,name="signupAction"),
    path('home',views.home,name="wall"),
    path('post',views.Post,name="postAction")
]

