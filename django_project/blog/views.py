from django.shortcuts import render
from django.http import HttpResponse


# let pass some dummy data from views to template
posts = [
	{
		'author': 'Corey',
		'title': 'Blog Post1',
		'date_posted': 'August 27,2019'
	},
	{
	'author': 'Jone',
	'title': 'Blog Post2',
	'date_posted': 'August 31,2019'
	},
	{
	'author': 'Alex',
	'title': 'Blog Post3',
	'date_posted': 'August 30,2019'
	}

]

# Create your views here.
def home(request):
	context = {
	'posts': posts,
	'title':"Abhay"
	}
	# return HttpResponse('<h1> Blog Home </h1>')
	# by render
	return render(request, 'blog/home.html', context)

def about(request):
	# return HttpResponse('<h1> Blog about </h1>')
	# by render
	return render(request, 'blog/about.html')
