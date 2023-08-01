from django.urls import path 
from .views import ImageList, ImageDetail, CounterList, CounterDetail, LogoutView, ReportList, ReportDetail, UserList, UserDetail
urlpatterns = [
    path('images', ImageList.as_view()),
    path('images/<int:id>', ImageDetail.as_view()),
    path('counters', CounterList.as_view()),
    path('counters/<int:id>', CounterDetail.as_view()),
    path('reports', ReportList.as_view()),
    path('reports/<int:id>', ReportDetail.as_view()),
    path('users', UserList.as_view()),
    path('users/<int:id>', UserDetail.as_view()),
    path('logout/',LogoutView.as_view(), name ='logout'),

]