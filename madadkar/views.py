from django.shortcuts import render
from django.views.generic import TemplateView
from MySite.forms import ContactForm
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from madadju.forms import ReportForm
from madadju.models import Madadju
from karbar.models import MyUser
from django.contrib.auth.models import User
import datetime
from karbar.forms import SignupForm2, SignupForm1
from madadkar.models import Madadkar
from django.contrib.auth import authenticate, login as auth_login
from django.views import View
from MySite.forms import MessageForm
from hamyar.models import Hamyar
from karbar.models import Message

def madadkarhome(request):
    return render(request, "madadkar/home.html")


def madadkargoal(request):
    return render(request, "madadkar/Goals.html")


def madadkarhistory(request):
    return render(request, "madadkar/History.html")


def madadkarchart(request):
    return render(request, "madadkar/Chart.html")


class MadadkarContact(TemplateView):
    template_name = 'madadkar/Contact.html'

    def get(self, request, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        text = None
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            form.save()
            text = form.cleaned_data
            form = ContactForm()
            context = {}
            message = "نظر شما با موفقیت ثبت شد"
            context['message'] = message
            context['type'] = 'green'

        args = {'form': form, 'text': text}
        return render(request, 'madadkar/home.html', context)


def madadkarprofile(request):
    return render(request, "madadkar/profile.html")


def editmadadju(request):
    return render(request, "madadkar/edit-madadju.html")


def editneed(request):
    return render(request, "madadkar/editneed.html")


def instantneed(request):
    return render(request, "madadkar/instantneed.html")


def madadjuregister(request):
    return render(request, "madadkar/madadju-register.html")


def managesaving(request):
    return render(request, "madadkar/managesaving.html")


def receipt(request):
    return render(request, "madadkar/receipt.html")

class Report(TemplateView):
    template_name = 'madadkar/report.html'

    def get(self, request, **kwargs):
        form = ReportForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReportForm(request.POST)
        text = None
        id = request.POST.get('text')
        user=User.objects.get(username=id)
        user=MyUser.objects.get(user=user)
        madadju=Madadju.objects.get(user=user)
        date = datetime.datetime.now()
        if(madadju!=None):
            title=request.POST.get('title')
            content=request.POST.get('content')
            report=Report.objects.create(madadju=madadju, content=content, title=title, date=date)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            form.save()
            text = form.cleaned_data
            form = ContactForm()
        context={}
        message = "گزارش شما با موفقیت ثبت شد"
        context['message'] = message
        context['type'] = 'green'
        args = {'form': form, 'text': text}
        return render(request, 'madadju/madadju.html', context)

def seemsg(request):
    return render(request, "madadkar/seemsg.html")


def seereq(request):
    return render(request, "madadkar/seerequests.html")


def success(request):
    return render(request, "madadkar/success.html")


def taaligh(request):
    return render(request, "madadkar/taaligh.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


def madadkarprofile(request):
    user = request.user
    user_form = SignupForm2(instance=user)
    myUser = MyUser.objects.get(user=request.user)
    madadkar = Madadkar.objects.get(user=myUser)
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = SignupForm2(request.POST, instance=request.user)
            # myUser = MyUser.objects.get(user=request.user)
            if user_form.is_valid():
                print("valid")
                user_form.save()
                myUser.user = request.user
                myUser.phone_number = request.POST.get('phone_number')
                myUser.national_id = request.POST.get('national_id')
                myUser.country = request.POST.get('country')
                myUser.city = request.POST.get('city')
                myUser.address = request.POST.get('address')
                myUser.postal_code = request.POST.get('postal_code')
                madadkar.employment_date = request.POST.get('employment_date')
                myUser.save()
                madadkar.save()
                return render(request, 'madadkar/home.html', {'message':"تغییرات با موفقیت ثبت شد"})
            else:
                print(user_form.errors)
    return render(request, 'madadkar/profile.html', {'user': user, 'myUser': myUser, 'madadkar':madadkar})



class MadadkarMadadjuregister(View):
    login_required = True
    template_name = 'madadkar/madadju-register.html'

    def get(self, request, **kwargs):
        form = SignupForm1()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm1(request.POST)
        phone_number = request.POST.get('phone_number')
        national_id = request.POST.get('national_id')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        physical_state = request.POST.get('physical_state')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        context = {'phone_number': phone_number, 'country': country, 'city': city,
                   'postal_code': postal_code, 'address': address, national_id: 'national_id', 'physical_state':physical_state, 'age':age,
                    'grade':grade, 'gender':gender}
        if form.is_valid():
            if len(phone_number) == 11 and phone_number[0:2] == '09':
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                member = MyUser.objects.create(user=user, phone_number=phone_number, country=country, city=city,
                                               postal_code=postal_code, address=address, national_id=national_id)
                member.save()
                madadju = Madadju.objects.create(user=member, gender=gender, grade=grade, age=age, physical_state=physical_state, account=0, saving=0)
                madadju.save()
                context['message'] = "مددجو با موفقیت ساخته شد"
                return HttpResponseRedirect(reverse('madadju-home'))
            else:
                phone_number_error = "شماره تلفن باید 11 رقمی باشد و با 09 آغاز شود."
                context['phone_number_error'] = phone_number_error
        context['form'] = form
        context['type'] = 'signup'
        return render(request, 'madadkar/madadju-register.html', context)




def madadkarviewh(request, username):
    user = User.objects.get(username=username)
    user=MyUser.objects.get(user=user)
    madadkar = Madadkar.objects.get(user=user)

    if request.method == 'GET':
        form = MessageForm()
        return render(request, 'madadkar/madadkar.html', {'madadkar': madadkar, 'form': form})

    if request.method == 'POST':
        message = "پیام با موفقیت ارسال شد"
        context = {}
        context['message'] = message
        context['type'] = 'green'
        user = request.user
        u = MyUser.objects.get(user=user)
        hamyar= Hamyar.objects.get(user=u)
        text=request.POST.get('text')
        hamyar=hamyar.user
        madadkar=madadkar.user
        message=Message.objects.create(sender=hamyar, receiver=madadkar, text=text)
        return render(request, 'hamyar/Hamyar_Home.html', context)

