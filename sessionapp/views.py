from django.shortcuts import render

# Create your views here.

#set
def set_session(request):
    request.session['name'] = 'Apurba'
    request.session['lname'] = 'Puja'
    request.session.set_expiry(0)
    #request.session.set_expiry(900)
    return render(request, 'session/setsession.html')
#get
def get_session(request):
    #s_name = request.session['name'] 
    s_name = request.session.get('name', default='guest')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')
    return render(request, 'session/getsession.html', {'name':s_name, 'keys':keys, 'items':items, 'age':age })
#del
def del_session(request):
    #if 'name' in request.session:
        #del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'session/delsession.html')

