from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Hamyar, Adapt
from karbar.forms import SignupForm1
from karbar.models import MyUser
from django.shortcuts import render, redirect
from MySite.forms import ContactForm
from .urls import *
from madadju.models import Madadju
from karbar.forms import MessageForm
from modir.models import Admin
from karbar.models import Message
import datetime, random
from hamyar.forms import PaymentForm, GiftForm
from hamyar.models import Payment, Gift


@login_required()
def HamyarHomeView(request):
    return render(request, "hamyar/Hamyar_Home.html")


class HamyarGoalsView(TemplateView):
    template_name = 'hamyar/Hamyar_Goals.html'


class HamyarContactView(TemplateView):
    template_name = 'hamyar/Hamyar_Contact.html'


class HamyarHistoryView(TemplateView):
    template_name = 'hamyar/Hamyar_History.html'


class HamyarChartView(TemplateView):
    template_name = 'hamyar/Hamyar_Chart.html'


class EnserafView(TemplateView):
    template_name = 'hamyar/Enseraf.html'


@login_required()
def EhdaView(request, username):
    myUserList = MyUser.objects.all()
    for myUser in myUserList:
        if myUser.user.username == username:
            break
    madadju = Madadju.objects.get(user=myUser)
    madadkar = madadju.current_madadkar

    if request.method == 'POST':
        form = GiftForm(request.POST)
        content = request.POST.get('content')
        now = datetime.datetime.now()

        myUser = MyUser.objects.get(user=request.user)
        hamyar = Hamyar.objects.get(user=myUser)
        if form.is_valid():
            print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            gift = Gift.objects.create(date=now, madadju=madadju, hamyar=hamyar, content=content, madadkar=madadkar)
            gift.save()
            print(gift.date)
            print(gift.content)
            return render(request, 'hamyar/Ehda_Receipt.html', {'gift': gift})
        else:
            return render(request, 'hamyar/Ehda_Receipt.html')

    if request.method == 'GET':
        form = GiftForm()
        return render(request, 'hamyar/Ehda.html', {'madadju': madadju})


class EhdaReceiptView(TemplateView):
    template_name = 'hamyar/Ehda_Receipt.html'


class LettersBoxView(TemplateView):
    template_name = 'hamyar/Letters_Box.html'


class MadadjooContactView(TemplateView):
    template_name = 'hamyar/Madadjoo_Contact.html'

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

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


@login_required()
def MadadjooListView(request):
    user = request.user
    myUser = MyUser.objects.get(user=request.user)
    myHamyar = Hamyar.objects.get(user=myUser)

    adaptList = Adapt.objects.filter(hamyar=myHamyar)

    madadjuList = []
    for adapt in adaptList:
        madadjuList.append(adapt.madadju)

    return render(request, 'hamyar/Madadjoo_List.html', {'list': madadjuList})


@login_required()
def PayView(request, username):
    myUserList = MyUser.objects.all()
    for myUser in myUserList:
        if myUser.user.username == username:
            break
    madadju = Madadju.objects.get(user=myUser)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        now = datetime.datetime.now()
        value = request.POST.get('value')
        receipt_number = random.randint(10000000, 100000000)

        myUser = MyUser.objects.get(user=request.user)
        hamyar = Hamyar.objects.get(user=myUser)

        kind = request.POST.get('kind')

        if form.is_valid():

            print("---------------------------------------------------------------")
            print(madadju.using)
            print("---------------------------------------------------------------")
            madadju.using += int((int(value) * madadju.percent) / 100)
            print(madadju.using)
            print("---------------------------------------------------------------")
            print(madadju.saving)
            print("---------------------------------------------------------------")
            madadju.saving += int(value) - madadju.using
            print(madadju.saving)
            madadju.save()

            receipt = Payment.objects.create(date=now, value=value, receipt_number=receipt_number,
                                             madadju=madadju, hamyar=hamyar, kind=kind)
            receipt.save()
            return render(request, 'hamyar/Pay_Receipt.html', {'receipt': receipt})
        else:
            return render(request, 'hamyar/Pay_Receipt.html')

    if request.method == 'GET':
        form = PaymentForm()
        return render(request, 'hamyar/Pay.html', {'madadju': madadju})


class PayReceiptView(TemplateView):
    template_name = 'hamyar/Pay_Receipt.html'


@login_required()
def SearchView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mgender = request.POST.get('gender')
            mfromage = request.POST.get('fromage')
            mtoage = request.POST.get('toage')
            mphysical_state = request.POST.get('physical_state')
            mcity = request.POST.get('city')

            Allmadadju = Madadju.objects.all()
            madadjuList = []
            for madadju in Allmadadju:
                if (madadju.gender == mgender and madadju.age >= int(mfromage) and
                            madadju.age <= int(
                            mtoage) and madadju.physical_state == mphysical_state and madadju.user.city == mcity):
                    madadjuList.append(madadju)

            return render(request, 'hamyar/Search_Result.html', {'list': madadjuList})
        else:
            return render(request, 'hamyar/Search.html')


@login_required()
def SerchResultView(request):
    return render(request, 'hamyar/Search_Result.html')


@login_required()
def ModirMessageView(request):
    if request.method == 'GET':
        form = MessageForm()
        return render(request, 'hamyar/Modir_Message.html', {'form': form})

    if request.method == 'POST':
        message = "پیام با موفقیت ارسال شد"
        context = {}
        context['message'] = message
        context['type'] = 'green'
        form = MessageForm(request.POST)
        text = request.POST.get('text')
        user = request.user
        u = MyUser.objects.get(user=user)
        admin = Admin.objects.get()
        admin = admin.user
        # context = {'sender': u, 'text': text, 'receiver': admin}
        # if form.is_valid(): #TODO zeinab
        message = Message.objects.create(sender=u, receiver=admin, text=text)
        message.save()
        return render(request, 'hamyar/Hamyar_Home.html', context)

        # context['form'] = form
        # return render(request, 'hamyar/Modir_Message.html', context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def edit_profile(request):
    user = request.user
    user_form = SignupForm1(instance=user)
    myUser = MyUser.objects.get(user=request.user)
    hamyar = Hamyar.objects.get(user=myUser)
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = SignupForm1(request.POST, instance=request.user)
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
                hamyar.report_method = request.POST.get('report_method')
                myUser.save()
                hamyar.save()
                return render(request, 'hamyar/Hamyar_Home.html')
    return render(request, 'hamyar/Edit_Profile.html', {'user': user, 'myUser': myUser, 'hamyar': hamyar})


@login_required()
def ProfileView(request, username):
    myUserList = MyUser.objects.all()
    for myUser in myUserList:
        if myUser.user.username == username:
            break
    hamyar = Hamyar.objects.get(user=myUser)

    if request.method == 'GET':
        form = MessageForm()
        return render(request, 'hamyar/Profile.html', {'hamyar': hamyar, 'form': form})

    if request.method == 'POST':
        message = "پیام با موفقیت ارسال شد"
        context = {}
        context['message'] = message
        context['type'] = 'green'
        form = MessageForm(request.POST)
        text = request.POST.get('text')
        user = request.user
        u = MyUser.objects.get(user=user)
        # context = {'sender': u, 'text': text, 'receiver': admin}
        # if form.is_valid(): #TODO zeinab
        message = Message.objects.create(sender=u, receiver=myUser, text=text)
        message.save()
        return render(request, 'hamyar/Hamyar_Home.html', context)
