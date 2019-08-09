from django.urls import path,re_path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name ='vote')
    # 重构代码
    path('', views.IndexView, name='index'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('showStudent/', views.queryStudent, name='queryStudent'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('randomStu/', views.randomStu, name='randomStu'),
    # re_path(r'^get_valid_img.png/', views.get_valid_img,name='get_valid_img'),

]
