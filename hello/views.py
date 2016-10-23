from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse(u'qiangdaxs')

def post_list(request):
    return render(request, 'hello/post_list.html', {})