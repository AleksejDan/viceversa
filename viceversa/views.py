from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	word_split = user_text.split()
	count_words = len(word_split)
	return render(request, 'reverse.html', {'usertext':user_text, 'reversetext':reversed_text, 'count_view':count_words})