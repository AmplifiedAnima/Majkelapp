from django.urls import path
from . import views


urlpatterns = [
path ('', views.home, name="home"),
path ('home', views.home, name="home"),

path ('login/', views.loginPage, name="login"),
path ('logout/', views.logoutUser, name="logout"),
path ('register/', views.registerPage, name="register"),
path ('profilepage/<str:pk>/',views.profilepage, name="profilepage"),
path ('profiles/', views.profiles ,name="profiles"),

path ('trainingprograms', views.trainingprograms, name="trainingprograms"),
path ('addtrainingunit/', views.addtrainingunit,name="addtrainingunit"),
path ('trainingplan/<str:pk>/', views.trainingplan,name="trainingplan" ),
path ('deletetraining/<str:pk>', views.deletetraining, name="deletetraining"),

path ('trainingsheet/<str:pk>/', views.trainingsheet,name="trainingsheet"),

path ('pliktest',views.pliktest,name="pliktest"),

path ('dictionary/', views.dictionary, name="dictionary"),
path ('word/<str:pk>',views.word,name="word"),
path ('addword', views.addword, name="addword"),
path ('wordform/<str:pk>', views.updateword , name="wordform"), 
path ('deleteword/<str:pk>', views.deleteword, name="deleteword"),
]