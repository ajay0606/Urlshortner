from django.urls import path
from infra.views import DemoList, DemoDetail
from . import views

app_name='infra'

urlpatterns = [
    
    path('', DemoList.as_view(), name='demo_list'),
    path('<int:pk>', DemoDetail.as_view(), name='demo_detail'),
    path('about',views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),



]