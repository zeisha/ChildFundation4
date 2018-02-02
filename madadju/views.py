from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from madadju.models import Madadju
from karbar.models import Message, MyUser
from modir.models import Admin
from django.urls import reverse

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

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def madadkarchange(request):
    if (request.GET.get('mybtn')):
        user = request.user
        user = MyUser.objects.get(user=user)
        user = Madadju.objects.get(user=user)
        admin = Admin.objects.all()
        text = 'لطفا مددکار مرا تغییر دهید'
        print("hi")
        user=request.user
        user=MyUser.objects.get(user=user)
        user=Madadju.objects.get(user=user)
        admin=Admin.objects.all()
        text='لطفا مددکار مرا تغییر دهید'
        Message.objects.create(text=text, sender=user, receiver=admin)
    return render(request, "madadju/madadkarchange.html")


def madadjuprofile(request):
    return render(request, "madadju/profile.html")


class MadadjuMsg(TemplateView):
    template_name = 'madadju/sendmsg.html'

    def get(self, request, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        sender = request.user
        text = request.POST.get('text')
        user = request.user
        u = MyUser.objects.get(user=user)
        madadju = Madadju.objects.get(user=u)
        receiver = madadju.current_madadkar
        receiver = receiver.user
        context = {'sender': u, 'text': text, 'receiver': receiver}
        if form.is_valid():
            message = Message.objects.create(sender=u, receiver=receiver, text=text)
            message.save()
            return HttpResponseRedirect(reverse('hamyar-home'))

        context['form'] = form
        return render(request, self.template_name, context)
