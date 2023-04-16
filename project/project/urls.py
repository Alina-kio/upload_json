from django.contrib import admin
from django.urls import path
from format.views import MyModelView
from format import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', MyModelView.as_view(), name='data'),
    path('data/<int:pk>', views.JsonItemView.as_view({
        'get': 'retrieve',
    })),
]
