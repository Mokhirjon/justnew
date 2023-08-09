from django.urls import path
from .views import TwerkALLView,DetailTwerksView,CreateTwerkView,UpdateTWerksView,DeleteTwerksView
urlpatterns=[path('get_all/',TwerkALLView.as_view()),
    path('get_by_index/<int:twerk_id>',DetailTwerksView.as_view()),
    path('create/',CreateTwerkView.as_view()),
    path('update/<int:twerk_id>/',UpdateTWerksView.as_view()),
    path ('delete/<int:twerk_id>/',DeleteTwerksView.as_view())
             ]