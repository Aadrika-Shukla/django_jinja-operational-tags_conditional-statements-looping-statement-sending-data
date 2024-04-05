from django.shortcuts import render
def send_data(request):
    return render(request,'send_data.html',context={'name':'Aadrika','age':22})

def conditions(request):
    d={'a':100,'b':200,'c':300}
    '''you can declare dictionary above and provide that value to context attribute'''
    return render(request,'conditions.html',context=d)

def looping(request):
    d={'name':'Aadrika'}
    '''you can declare dictionary above and provide that dictionary name as 3 rd argument to render function'''
    return render(request,'looping.html',d)

   

# Create your views here.
