from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""def post_list(request):
    return render(request,'blog/post_list.html', {})
"""    

def home(request):
		return render(request,'blog/home.html')

def translate(request):
		original = request.GET['originaltext'].lower()
		
		translation = ''

		for word in original.split():
			if word[0] in ['a','e','i','o','u']:
				#vowel
				translation += word
				translation += 'vowel'
			else:
				#consonant
				translation += word
				translation += 'consonant'		

		return render(request,'blog/translate.html',{'original':original,'translation':translation})
		