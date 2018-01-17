from django.conf.urls import url,include
from appone import views

app_name = 'appone'

urlpatterns = [
    url(r"^about/$", views.about,name="about"),
    url(r"^projects/$", views.proj,name="proj"),
url(r"^projects/flat", views.flat,name="flat"),
url(r"^projects/mansion", views.mansion,name="mansion"),
url(r"^projects/house", views.house,name="house")
]