from django.urls import path
from .views import CookieStandList, CookieStandgDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandgDetail.as_view(), name="cookie_stand_detail"),
]
