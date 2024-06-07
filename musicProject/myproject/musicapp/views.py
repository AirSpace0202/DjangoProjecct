import json
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArtistClassify, ArtistFan

def get_artist_classify_data(request):
    data = ArtistClassify.objects.all().values('artist_classify', 'artist_name', 'category_id')
    print(data)

    result = [{'category_id': entry['category_id'],
               'artist_classify': entry['artist_classify'].replace('/', '-'),
               'artist_name': entry['artist_name']} for entry in data]

    return JsonResponse(result, safe=False)

@login_required
def index(request):
    # 获取 artist_classify 数据以传递给模板
    artists = ArtistClassify.objects.all().values('artist_classify')
    artists_list = list(artists)
    artists_json = json.dumps(artists_list)
    return render(request, 'index.html', {'artists': artists_json})

def category_artists(request, category_name):
    category_name = category_name.strip()
    print(f"Accessing category: {category_name}")

    # 修改查询条件，根据 artist_classify 获取 artists
    artists = ArtistClassify.objects.filter(artist_classify=category_name).values('artist_name')
    artist_names = [artist['artist_name'] for artist in artists]

    # 获取这些歌手的粉丝数量
    artist_fans = ArtistFan.objects.filter(artist_name__in=artist_names).values('artist_name', 'fan_cnt')

    if not artist_fans:
        print(f"No artists found for category: {category_name}")
        raise Http404("找不到歌手数据")

    artists_list = list(artist_fans)
    artists_json = json.dumps(artists_list)

    print(f"Returning {len(artists_list)} artists for the category.")
    return render(request, 'category_artists.html', {'category_name': category_name, 'artists': artists_json})

def detail_view(request):
    classify_data = ArtistClassify.objects.all().values('artist_classify')
    classify_list = list(classify_data)
    classify_json = json.dumps(classify_list)
    return render(request, 'detail.html', {'classify_data': classify_json})

def artist_list_view(request, category_name):
    artists = ArtistClassify.objects.filter(artist_classify=category_name).values('artist_name')
    if not artists.exists():
        raise Http404("No artists found")
    artists_list = list(artists)
    return render(request, 'artist_list.html', {'category_name': category_name, 'artists': artists_list})