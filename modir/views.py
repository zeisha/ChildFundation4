from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views import generic

from datetime import date

from MySite.forms import ContactForm
from karbar.forms import SignupForm1
from karbar.models import MyUser
from hamyar.models import Hamyar, PaymentFoundation, Payment
from madadkar.models import Madadkar
from madadju.models import Madadju
from .models import Admin
from .forms import DeleteUserForm


class AdminGoalsView(TemplateView):
    template_name = 'modir/Admin_Goals.html'


class AdminHomeView(TemplateView):
    template_name = 'modir/Admin_Home.html'


class AdminContactView(TemplateView):
    template_name = 'modir/Admin_Contact.html'

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


class AdminHistoryView(TemplateView):
    template_name = 'modir/Admin_History.html'


class AdminChartView(TemplateView):
    template_name = 'modir/Admin_Chart.html'


class AdminHamyarRegisterView(View):
    template_name = 'modir/Hamyar_Register.html'

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
        report_method = request.POST.get('report_method')
        context = {'phone_number': phone_number, 'report_method': report_method, 'country': country, 'city': city,
                   'postal_code': postal_code, 'address': address, national_id: 'national_id'}
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
                hamyar = Hamyar.objects.create(user=member, report_method=report_method)
                hamyar.save()
                # return HttpResponseRedirect(reverse('hamyar-home'))
                message = "با موفقیت ثبت نام کردید. اکنون میتوانید وارد سایت شوید"
                context = {}
                context['message'] = message
                context['type'] = 'green'
                return render(request, 'MySite/Home.html', context)
            else:
                phone_number_error = "شماره تلفن باید 11 رقمی باشد و با 09 آغاز شود."
                context['phone_number_error'] = phone_number_error
        context['form'] = form
        context['type'] = 'signup'
        return render(request, 'modir/Hamyar_Register.html', context)


class AdminMadadkarRegisterView(View):
    template_name = 'modir/Madadkar_Register.html'

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
        employment_date = date.today().isoformat()
        context = {'phone_number': phone_number, 'employment_date': employment_date, 'country': country, 'city': city,
                   'postal_code': postal_code, 'address': address, national_id: 'national_id'}
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
                madadkar = Madadkar.objects.create(user=member, employment_date=employment_date)
                madadkar.save()
                return HttpResponseRedirect(reverse('madadkar-home'))
            else:
                phone_number_error = "شماره تلفن باید 11 رقمی باشد و با 09 آغاز شود."
                context['phone_number_error'] = phone_number_error
        context['form'] = form
        context['type'] = 'signup'
        return render(request, 'modir/Madadkar_Register.html', context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


# class UserDeleteView(TemplateView):
#     template_name = 'modir/Admin_delete.html'
#
#     def get(self, request, **kwargs):
#         form = DeleteUserForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = DeleteUserForm(request.POST)
#         context = {}
#         messages = None
#         print(form)
#         if form.is_valid():
#             print('hiii')
#             form.save()
#             username = form.cleaned_data.get('username')
#             print(MyUser.objects.all())
#             try:
#                 u = MyUser.objects.get(username=username)
#                 print(u)
#                 try:
#                     Admin.objects.get(user=u)
#                     messages = 'شما نمی‌توانید مدیر را حذف کنید.'
#                     context['messages'] = messages
#                     context['type'] = 'red'
#                     return HttpResponseRedirect(reverse('admin-delete'))
#                 except Admin.DoesNotExist:
#                     messages = "کاربر با موفقیت حذف شد."
#                     context['messages'] = messages
#                     context['type'] = 'green'
#                     try:
#                         madadkar = Madadkar.objects.get(user=u)
#                         madadkar.delete()
#                         return HttpResponseRedirect(reverse('admin-delete'))
#                     except Madadkar.DoesNotExist:
#                         try:
#                             madadju = Madadju.objects.get(user=u)
#                             madadju.delete()
#                             return HttpResponseRedirect(reverse('admin-delete'))
#                         except Madadju.DoesNotExist:
#                             hamyar = Hamyar.objects.get(user=u)
#                             hamyar.delete()
#                             return HttpResponseRedirect(reverse('admin-delete'))
#             except:
#                 message = "چنین کاربری پیدا نشد."
#                 context['messages'] = messages
#                 context['type'] = 'red'
#             context['form'] = form
#         return render(request, 'modir/admin_delete.html', context)


def delete_user(request):
    context = {}
    message = None
    if request.method == 'POST':
        if request.POST.get('submit') == 'حذف':
            form = DeleteUserForm(request.POST)
            username = request.POST['username']
            try:
                user = User.objects.get(username=username)
                u = MyUser.objects.get(user=user)
                try:
                    Admin.objects.get(user=u)
                    message = 'شما نمی‌توانید مدیر را حذف کنید.'
                    context['messag'] = message
                    type = 'red'
                except Admin.DoesNotExist:
                    context['message'] = message
                    try:
                        madadkar = Madadkar.objects.get(user=u)
                        message = "کاربر با موفقیت حذف شد."
                        type = 'green'
                        madadkar.delete()
                        u.delete()
                        user.delete()
                    except Madadkar.DoesNotExist:
                        try:
                            madadju = Madadju.objects.get(user=u)
                            message = "کاربر با موفقیت حذف شد."
                            type = 'green'
                            madadju.delete()
                            u.delete()
                            user.delete()
                            return HttpResponseRedirect(reverse('admin-delete'))
                        except Madadju.DoesNotExist:
                            print(Hamyar.objects.all())
                            hamyar = Hamyar.objects.get(user=u)
                            type = 'green'
                            message = "کاربر با موفقیت حذف شد."
                            hamyar.delete()
                            u.delete()
                            user.delete()
            except:
                message = "چنین کاربری پیدا نشد."
                type = 'red'
            print(message)
            context['message'] = message
            context['type'] = type
            context['form'] = form

    return render(request, 'modir/admin_delete.html', context)


class PaymentView(generic.ListView):
    template_name = 'modir/PaymentsReport.html'

    context_object_name = 'all_payments'

    def get_queryset(self):
        return PaymentFoundation.objects.all()


class PaymentMadadjuView(generic.ListView):
    template_name = 'modir/PaymentsMadadjuReports.html'

    context_object_name = 'all_payments'

    def get_queryset(self):
        return Payment.objects.all()
