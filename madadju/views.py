from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from madadju.models import Madadju
from karbar.models import Message, MyUser
from modir.models import Admin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from MySite.forms import ContactForm, MessageForm


def madadjuhome(request):
    return render(request, 'madadju/madadju.html')


def madadjugoal(request):
    return render(request, 'madadju/madadju-goals.html')


def madadjuhistory(request):
    return render(request, "madadju/madadju-history.html")


def madadjuchart(request):
    return render(request, "madadju/madadju-chart.html")


class MadadjuContact(TemplateView):
    template_name = 'madadju/madadju-contact.html'

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
        context={}
        message = "نظر شما با موفقیت ثبت شد"
        context['message'] = message
        context['type'] = 'green'
        args = {'form': form, 'text': text}
        return render(request, 'madadju/madadju.html', context)

@login_required
def madadkarchange(request):
    print("salam")
    context={}
    print(request.user)
    if request.POST.get('submit') == 'تائید':
        print("hi")
        user=MyUser.objects.get(user=request.user)
        user=Madadju.objects.get(user=user)
        user=user.user
        admin=Admin.objects.get()
        print(type(admin.user))
        admin=admin.user
        text='لطفا مددکار مرا تغییر دهید'
        message=Message.objects.create(text=text, sender=user, receiver=admin)
        message.save()
        message="درخواست شما جهت بررسی به مدیر فرستاده شد"
        context['message'] = message
        context['type'] = 'green'
        return render(request,"madadju/madadju.html",context)
    return render(request, "madadju/madadkarchange.html")


def madadjuprofile(request):
    return render(request, "madadju/profile.html")


class MadadjuMsg(TemplateView):
    template_name = 'madadju/sendmsg.html'

    def get(self, request, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        message = "پیام با موفقیت ارسال شد"
        context={}
        context['message'] = message
        context['type'] = 'green'
        form = MessageForm(request.POST)
        sender = request.user
        text = request.POST.get('text')
        user = request.user
        u = MyUser.objects.get(user=user)
        madadju = Madadju.objects.get(user=u)
        receiver = madadju.current_madadkar
        receiver = receiver.user
        #context = {'sender': u, 'text': text, 'receiver': receiver}
        if form.is_valid():
            message = Message.objects.create(sender=u, receiver=receiver, text=text)
            message.save()
            return render(request,'madadju/madadju.html',context)

        context['form'] = form
        return render(request, self.template_name, context)


class MadadjuMsg2(TemplateView):
    template_name = 'madadju/sendmsg2.html'

    def get(self, request, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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
        #context = {'sender': u, 'text': text, 'receiver': admin}
        if form.is_valid():
            message = Message.objects.create(sender=u, receiver=admin, text=text)
            message.save()
            return render(request, 'madadju/madadju.html', context)

        context['form'] = form
        return render(request, self.template_name, context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))