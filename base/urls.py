from django.urls import include, path
from base.views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', TestView.as_view()),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
]
