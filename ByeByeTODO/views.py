from django.shortcuts import render, redirect
from typing import Dict
from .models import List
from .forms import ListForm


def index(request) -> render:
    """
    http://127.0.0.1:8000/
    ページトップを作成
    """
    return render(request, 'index.html', {})


def login(request) -> render:
    """
    http://127.0.0.1:8000/
    ログインを作成
    """
    #return render(request, 'accounts/registration/login.html', {})
    return redirect('registration/login.html')


def home(request) -> render:
    """
    http://127.0.0.1:8000/
    ページホームを作成
    """
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request) -> render:
    """
    http://127.0.0.1:8000/about/
    ページ説明を作成
    """
    context: Dict[str, str] = {'first_name': 'Kiuchi',
                               'last_name': 'Koichi'}
    return render(request, 'about.html', context)
