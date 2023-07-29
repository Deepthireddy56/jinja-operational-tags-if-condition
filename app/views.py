from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'Name':'DEEPTHI', 'Age': 21}
    return render(request,'data_render.html',context=d)
def condition1(request):
    d={'a':10,'b':20}
    return render(request,'condition1.html',context=d)
def condition2(request):
    d={'a':100,'b':200}
    return render(request,'condition2.html',context=d)
def condition3(request):
    d={'a':5000,'b':1390,'c':30}
    return render(request,'condition3.html',context=d)
def condition4(request):
    d={'a':10000,'b':20009,'c':304570,}
    return render(request,'condition4.html',context=d) 