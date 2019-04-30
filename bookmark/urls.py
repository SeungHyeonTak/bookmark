from django.urls import path
from .views import BookmarkList, BookmarkCreate, BookmarkDelete, BookmarkDetail, BookmarkUpdate

app_name = "bookmark"
urlpatterns = [

    path("create/", BookmarkCreate.as_view(), name='create'),
    #숫자로 컨버팅이 가능해야한다.
    path("delete/<int:pk>/", BookmarkDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BookmarkUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", BookmarkDetail.as_view(), name='detail'),
    path("", BookmarkList.as_view(), name='index'),
]