from django.urls import path
from . import views

app_name = "learning_logs"  # Чтобы django отличал этот файл urls.py от других
urlpatterns = [  # список страниц, которые можно запрашивать из приложения learning_logs (например)
    path("", views.index, name="index"), # path('url', функция, имя index чтобы корректно на неё ссылаться)
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
