from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Bookmark
from rest_framework.generics import ListCreateAPIView
from .serializers import *

# Create your views here.
class ApiBookmarkList(ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class ApiBookmarkDetail(ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkListView(ListView):
    # model 을 넣어주고, templeat 를 넣어주지 않아도.
    # 모델명 이름으로 유추하여 템플릿 화면을 만들어 사용한다.
    model = Bookmark
    #3개만 표현
    paginate_by = 3


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    #어디서 만들어지고
    success_url = reverse_lazy('list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    print(model)
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    #어디서 지워지냐..
    success_url = reverse_lazy('list')