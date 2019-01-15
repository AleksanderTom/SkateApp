from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from SkateApp.forms import UserForm, LoggingInForm, EditProfileForm, AddPostForm, EditPostForm
from SkateApp.models import UserProfile, Image


class HomePageView(View):
    def get(self, request):
        try:
            username = request.session['username']
            if username:
                return render(request, 'Homepage.html', {'username': username})
        except:
            return render(request, 'Homepage.html', {})


class UserFormView(View):
    def get(self, request):
        try:
            username = request.session['username']
            if username:
                return render(request, 'Register.html', {'msg_logged': 'You need to log off to register new user.'})
        except:
            form = UserForm()
            return render(request, 'Register.html', {'form': form.as_p()})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            all_users = User.objects.all()
            username_inp = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']

            for user in all_users:
                if username_inp.lower() == user.username.lower():
                    msg = 'User already exists.'
                    return render(request, 'Register.html', {'msg': msg, 'form': form.as_p()})

            if len(username_inp) == "":
                return render(request, 'Register.html', {'msg': 'Please enter your username.', 'form': form.as_p()})

            if password != re_password:
                return render(request, 'Register.html', {'msg': 'Given passwords does not match.', 'form': form.as_p()})

            User.objects.create_user(username=username_inp, email=email, password=password)
            user = User.objects.get(username=username_inp)
            UserProfile.objects.create(user_id=user.id)
            msg_suc = 'Your account has been created.'
            return render(request, 'Register.html', {'msg_suc': msg_suc})
        msg = 'Check inputs once again.'
        return render(request, 'Register.html', {'form': form.as_p(), 'msg': msg})


class LoginUser(View):
    def get(self, request):
        form = LoggingInForm()
        try:
            username = request.session['username']
            if username:
                return render(request, "Login.html", {'form': form.as_p(), 'username': username})
        except:
            return render(request, "Login.html", {'form': form.as_p()})

    def post(self, request):
        form = LoggingInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                msg = 'Logged In.'
                request.session['username'] = username
                return render(request, "LoggedIn HP.html", {'form': form.as_p(), 'msg': msg, 'username': username})
        msg = 'Incorrect password or username'
        return render(request, "Login.html", {'form': form.as_p(), 'msg': msg})


class Logout(View):
    def get(self, request):
        if request.session['username']:
            del request.session['username']
        logout(request)
        return redirect(reverse('login'))


class UserAccView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = EditProfileForm()
        if request.session['username']:
            username = request.session['username']
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user_id=user.id)
            images = Image.objects.filter(owner=user_profile)
            return render(request, "UserPanel.html",
                          {'form': form.as_p(), 'username': username, 'user': user, 'images': images})

    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.session['username'])
            user_profile = UserProfile.objects.get(user_id=user.id)
            user_profile.avatar = request.FILES['avatar']
            user_profile.save()

            msg = 'Avatar saved.'
            return render(request, 'UserPanel.html', {'msg': msg})


class SoloSkateView(View):

    def get(self, request):
        try:
            username = request.session['username']
            if username:
                return render(request, 'SoloSkate.html', {'username': username})
        except:
            return render(request, 'SoloSkate.html', {})


class MiniForumView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        images = Image.objects.all()
        print(images)
        users_all = User.objects.all()
        print(users_all)
        profiles = UserProfile.objects.all()
        print(profiles)
        form = AddPostForm()
        try:
            username = request.session['username']
            if username:
                user = User.objects.get(username=username)
                user_profile = UserProfile.objects.get(user=user.id)

                ctx = {
                    'username': username,
                    'user': user,
                    'user_profile': user_profile,
                    'profiles': profiles,
                    'users_all': users_all,
                    'images': images,
                    'form': form.as_p()
                }

                return render(request, 'MiniForum.html', ctx)
        except:
            username = request.session['username']
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=user.id)

            ctx = {
                'username': username,
                'user': user,
                'user_profile': user_profile,
                'profiles': profiles,
                'users_all': users_all,
                'images': images,
                'form': form.as_p()
            }
            for image in images:
                print(image.image.url)
            return render(request, 'MiniForum.html', ctx)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            rating = form.cleaned_data['rating']
            description = form.cleaned_data['description']
            image = request.FILES['image']
            owner = User.objects.get(username=request.session['username'])
            user_profile = UserProfile.objects.get(user_id=owner.id)

            Image.objects.create(title=title, rating=rating, description=description, image=image, owner=user_profile)

            msg = 'Post added.'
            return render(request, 'MiniForum.html', {'msg': msg})


class EditPostView(View):
    def get(self, request, id):
        form = EditPostForm()
        image = Image.objects.get(pk=id)
        if request.session['username']:
            username = request.session['username']
            return render(request, 'Edit_Post.html', {'image': image, 'form': form, 'username': username})
        return render(request, 'Edit_Post.html', {'image': image, 'form': form})

    def post(self, request, id):
        form = EditPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = Image.objects.get(pk=id)
            image.title = form.cleaned_data['title']
            image.rating = form.cleaned_data['rating']
            image.description = form.cleaned_data['description']
            image.image = request.FILES['image']
            image.save()
            return redirect(reverse('user_acc'))


class DeletePostView(View):
    def get(self, request, id):
        image = Image.objects.get(pk=id)
        image.delete()
        return redirect(reverse('user_acc'))


class AddWarnView(View):
    def get(self, request, id):
        print(id)
        user_profile = UserProfile.objects.get(pk=id)
        if user_profile.warn == 5:
            gen_user = User.objects.get(pk=user_profile.user_id)
            gen_user.delete()
            return HttpResponse('User exceeded max number of warns, deleted.')
        user_profile.warn += 1
        user_profile.save()
        return redirect(reverse('mini_forum'))
