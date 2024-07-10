from django.shortcuts import render

# Create your views here.
# create post_list function, take a reques as a argument/parameter
def post_list(request):
    # return the request
    return render(request, 'blog/post_list.html', {})