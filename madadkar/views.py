from django.shortcuts import render
from django.views.generic import TemplateView
from MySite.forms import ContactForm


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

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


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


def report(request):
    return render(request, "madadkar/report.html")


def seemsg(request):
    return render(request, "madadkar/seemsg.html")


def seereq(request):
    return render(request, "madadkar/seerequests.html")


def success(request):
    return render(request, "madadkar/success.html")


def taaligh(request):
    return render(request, "madadkar/taaligh.html")
