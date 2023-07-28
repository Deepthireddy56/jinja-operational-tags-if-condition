from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'Name':'DEEPTHI', 'Age': 21}
    return render(request,'data_render.html',context=d)