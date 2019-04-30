from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark

class BookmarkList(ListView):
    model = Bookmark
    #_list

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'
    #_form

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'
    #_from

class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'  #혼자 _confirm_delete기 때문에
    success_url = '/'
    #_confirm_delete

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'
    # _detail
