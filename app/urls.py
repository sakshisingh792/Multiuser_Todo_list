from django.contrib import admin
from django.urls import path
from app.views import home ,Login,Signup,add_todo,signout,delete_todo,change_todo


urlpatterns = [
    path("",home,name="home"),
    path("login",Login,name="login",),
    path("signup",Signup,name="signup"),
    path("add-todo",add_todo,name='add-todo'),
    path("delete-todo/<int:id>",delete_todo,name='delete_todo'),
    path("change-status/<int:id>/<str:status>",change_todo,name='delete_todo'),
    
    path("logout/",signout,name="logout")
]