
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse('app_blog:blogList'))
