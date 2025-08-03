from django.shortcuts import render

# Create your views here.

def homeview(request):
    posts = [
        {'title': 'My First Post', 'date': 'August 3, 2025', 'content': 'Hello, this is my first blog post!'},
        {'title': 'Learning Django', 'date': 'August 4, 2025', 'content': 'Today I learned how to use Django templates.'},
    ]
    return render(request, 'template_engine/index.html', {'posts': posts})