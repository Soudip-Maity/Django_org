from . import views
from django.urls import path
urlpatterns = [
    path('', views.employee,name="employee"),
    path('post/', views.post_page,name="post_page"),
    path('post/create/', views.link_create,name="link_create"),
    path('<int:link_id>/edit/', views.link_edit,name="link_edit"),
    path('<int:link_id>/delete/', views.link_delete, name="link_delete"),
    path('registration/', views.registration,name="registration"),
    


]