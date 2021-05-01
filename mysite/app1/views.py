from django.shortcuts import render, redirect
from .models import *
from .forms import *

keyvalue = 0
# Create your views here.
def registerasnewuser(request):

    registerform = register()
    return render(request, 'registerform.html', {'registerform': registerform})

def registersave(request):

    global keyvalue

    if request.method == 'POST':
        registerform = register(request.POST)
        # print("2")
        keyvalue = 0
        if registerform.is_valid():

            if len(request.POST["password"]) < 8:

                keyvalue = 0
                return render(request, 'registerform.html', {'registerform': registerform, 'error': 'Password should be minimum of 8 characters', 'keyvalue': keyvalue})

            if request.POST["password"] != request.POST["password_again"]:

                keyvalue = 0
                return render(request, 'registerform.html', {'registerform': registerform, 'error': 'Passwords Dont Match', 'keyvalue': keyvalue})

            request.session['username'] = request.POST['username']
            request.session['emailID'] = request.POST['emailID']
            user = newuser(username = registerform.cleaned_data['username'], emailID = registerform.cleaned_data['emailID'], password = registerform.cleaned_data['password'])
            user.save()
            # print("HI")
            return redirect('success')
        
        else:
            return render(request, 'registerform.html', {'registerform': registerform})

def loginuser(request):
    global keyvalue
    keyvalue = 0
    user = newuser.objects.all()
    print(user)
    loginform = login()
    return render(request, 'loginform.html', {'loginform': loginform, 'keyvalue': keyvalue})


def loginuserget(request):

    

    if request.method == "POST":
        # print("2")
        loginform = login(request.POST)

        # username = request.POST["username"]
        # password = request.POST["password"]


        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            data = newuser.objects.filter(username = username, password = password)
            if data:
                request.session['username'] = username
                global session
                session = request.session
                # print("...^^")

                global keyvalue
                keyvalue = 0
                return redirect('success')

            if username not in newuser.objects.values_list('username', flat = True):
                return render(request, 'loginform.html', {'error1': "Username Does Not Exists", 'loginform': loginform})
            
            if password not in newuser.objects.values_list('password', flat = True):
                return render(request, 'loginform.html', {'error2': "Password Does Not Exists", 'loginform': loginform})
            
            user = newuser.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'loginform.html', {'error3': 'Username password mismatch', 'loginform': loginform})

                    else:
                        return redirect('success')
            # print(username)
            return render(request, 'loginform.html', {'username': username})

def success(request):
    return render(request, 'inde.html')

def logout(request):
    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('login')
