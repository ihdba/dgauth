from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home:index')


def login(request):
    ctx = {}
    ctx['title'] = 'Login'
    
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'ctx': ctx})
    elif request.method =='POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            ctx['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'ctx': ctx})
        else:
            auth_login(request, user)
            return redirect('home:index')
        

    
def signup(request):
    ctx = {}
    ctx['title'] = 'Sign Up'
    if request.method == 'GET':
        ctx['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'ctx': ctx})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            ctx['form'] = form
            return render(request, 'accounts/signup.html', {'ctx': ctx})


