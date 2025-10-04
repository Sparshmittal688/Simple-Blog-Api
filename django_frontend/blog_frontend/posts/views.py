from django.shortcuts import render, redirect
from .forms import PostForm
import requests

FASTAPI_URL = "http://127.0.0.1:8000/posts"

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Send data to FastAPI
            response = requests.post(FASTAPI_URL, json=data)
            if response.status_code == 200 or response.status_code == 201:
                return redirect('success')  # redirect to success page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def success(request):
    return render(request, 'success.html')

