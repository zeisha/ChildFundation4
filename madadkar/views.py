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
from karbar.forms import SignupForm2
from madadkar.models import Madadkar


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
        message = "نظر شما با موفقیت ثبت شد"
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