from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""def post_list(request):
    return render(request,'blog/post_list.html', {})
"""    

def home(request):
		return render(request,'blog/home.html')

def translate(request):
		original = request.GET['originaltext']
		 
		return render(request,'blog/translate.html')
		