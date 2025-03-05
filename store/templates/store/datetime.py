
from django.contrib import admin
from django.urls import path
from lab1.views import current_datetime 
urlpatterns = [

path('cdt/', admin.site.urls),
path('cdt/',current_datetime),

]
