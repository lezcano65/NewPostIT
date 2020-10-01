from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm

from apps.user.forms import LoginForm, registernota, registerUser
from apps.user.models import nota
from apps.user.views import mostrar_notas

from .forms import changeUsernameForm, changeEmailForm
from django.contrib import messages


def indexPage(request):
    try:
        if request.method == "POST":
            log_in = LoginForm(request.POST)
            model_username = request.POST.get('username')
            model_password = request.POST.get('password')
            if (model_username != None) and (model_password != None):
                if log_in.is_valid():
                    user = authenticate(username=model_username,
                                        password=model_password)
                    login(request, user)
                    messages.success(request, 'User name is: '+model_username)
                    current_user = request.user
                    user = User.objects.get(username=model_username)
                    if login:
                        return mostrar_notas(request)
                    else:
                        return redirect('index')
                else:
                    messages.success(request, 'data error :')
                    return redirect('index')
            else:
                print("")
                return redirect('index')
    except AttributeError:
        return redirect('index')
    newUser = registerUser(request.POST)
    model = User
    if newUser.is_valid():
        model.username = newUser.cleaned_data["username"]
        model.email = newUser.cleaned_data["email"]
        model.password1 = newUser.cleaned_data["password1"]
        model.password2 = newUser.cleaned_data["password2"]
        if (type(model.password) != int) and (model.password != model.email) and (model.password != model.username) and (len(model.password1) > 7) and (model.password1 == model.password2):
            grabar = User(username=model.username, email=model.email,
                          password=model.password1)
            grabar.save()
            user = User.objects.get(username=model.username)
            user.is_staff = True
            user.is_active = True
            user.set_password(model.password1)
            user.save()
            return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})
            messages.success(
                request, 'New user create whit name '+model.username)
        else:
            print("error en el formulario")
    else:
        newUser = registerUser()
        log_in = LoginForm()
    return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required
def settingsUser(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    ctx = {"user": user}
    return render(request, 'login/settings.html', ctx)


def changeEmail(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeEmailForm(request.POST)
        model_email = request.POST.get("email")
        model_email2 = request.POST.get('email2')
        model_email3 = request.POST.get('email3')
        if model_email == user.email:
            grabar = User(id=user.id, username=user.username, email=model_email2,
                          password=user.password)
            if (model_email != (model_email2 == model_email3)):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.save()
                username = user.username
                password = user.password
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    return mostrar_notas(request)
                return redirect('home')
            else:
                print("email no coincide o es igual al email viejo")
                return redirect('changeEmail')
        else:
            print("formulario invalido")
            return redirect('changeEmail')
    else:
        newUser = changeEmailForm()
    return render(request, "login/changeEmail.html", {'User': newUser})


@login_required
def changePass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            print('Your password was successfully updated!')
            return redirect('home')
        else:
            print('Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/changePass.html', {
        'form': form
    })


@login_required
def changeUsername(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeUsernameForm(request.POST)
        model_username = request.POST.get("username")
        model_username2 = request.POST.get('username2')
        model_username3 = request.POST.get('username3')
        if model_username == user.username:
            grabar = User(id=user.id, username=model_username2, email=user.email,
                          password=user.password)
            if (model_username != (model_username2 == model_username3)):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.save()
                username = user.username
                password = user.password
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    return mostrar_notas(request)
                return redirect('home')
            else:
                print("username no coincide o es igual al viejo")
                return redirect('changeUsername')
        else:
            print("formulario invalido")
            return redirect('changeUsername')
    else:
        newUser = changeUsernameForm()
    return render(request, "login/changeUsername.html", {'User': newUser})
