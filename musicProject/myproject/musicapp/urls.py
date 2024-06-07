from django.urls import path
from .views import get_artist_classify_data, index, category_artists, detail_view, artist_list_view

urlpatterns = [
    path('api/artist_classify_data/', get_artist_classify_data, name='artist_classify_data'),  # 参数为请求路径，函数名，取名
    path('', index, name='index'),
    path('category/<str:category_name>/', category_artists, name='category_artists'),
    path('detail/', detail_view, name='detail'),
    path('artist_list/<str:category_name>', artist_list_view, name='artist_list')
]