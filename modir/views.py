from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views import generic

from datetime import date

from MySite.forms import ContactForm
from karbar.forms import SignupForm1, SignupForm2
from karbar.models import MyUser
from hamyar.models import Hamyar, PaymentFoundation, Payment
from madadkar.models import Madadkar
from madadju.models import Madadju
from .models import Admin
from .forms import DeleteUserForm


class AdminGoalsView(TemplateView):
    login_required = True
    template_name = 'modir/Admin_Goals.html'


class AdminHomeView(TemplateView):
    login_required = True
    template_name = 'modir/Admin_Home.html'


class AdminContactView(TemplateView):
    login_required = True
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
    login_required = True
    template_name = 'modir/Admin_History.html'


class AdminChartView(TemplateView):
    login_required = True
    template_name = 'modir/Admin_Chart.html'


class AdminHamyarRegisterView(View):
    login_required = True
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
    login_required = True
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


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
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
    login_required = True
    template_name = 'modir/PaymentsReport.html'

    context_object_name = 'all_payments'

    def get_queryset(self):
        return PaymentFoundation.objects.all()


class PaymentMadadjuView(generic.ListView):
    login_required = True
    template_name = 'modir/PaymentsMadadjuReports.html'

    context_object_name = 'all_payments'

    def get_queryset(self):
        return Payment.objects.all()


class ChooseUserEditView(generic.ListView):
    login_required = True
    template_name = 'modir/users_edit.html'

    context_object_name = 'all_users'

    def get_queryset(self):
        return MyUser.objects.all()


class UserEditView(generic.DetailView):
    login_required = True
    model = MyUser
    template_name = 'modir/edit_detail.html'


@login_required
def edit_profile(request, pk):
    myUser = MyUser.objects.get(pk=pk)
    print(myUser)
    user = User.objects.get(username=myUser.user.username)
    print(user)
    if request.method == 'POST':
        print('hiii')
        user_form = SignupForm2(request.POST, instance=user)
        if user_form.is_valid():
            print("valid")
            user_form.save()
            myUser.phone_number = request.POST.get('phone_number')
            myUser.national_id = request.POST.get('national_id')
            myUser.country = request.POST.get('country')
            myUser.city = request.POST.get('city')
            myUser.address = request.POST.get('address')
            myUser.postal_code = request.POST.get('postal_code')
            myUser.save()
            try:
                modir = Admin.objects.get(user=myUser)
                modir.save()
            except Admin.DoesNotExist:
                try:
                    madadkar = Madadkar.objects.get(user=myUser)
                    madadkar.save()
                except Madadkar.DoesNotExist:
                    try:
                        madadju = Madadju.objects.get(user=myUser)
                        madadju.save()
                    except Madadju.DoesNotExist:
                        hamyar = Hamyar.objects.get(user=myUser)
                        hamyar.save()

            return render(request, 'modir/edit_detail.html', {'user': user, 'myUser': myUser, pk: pk})
    return render(request, 'modir/edit_detail.html', {'user': user, 'myUser': myUser, pk: pk})


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

            return render(request, 'modir/Search_Result.html', {'list': madadjuList})
        else:
            return render(request, 'modir/Search.html')


@login_required()
def SerchResultView(request):
    return render(request, 'modir/Search_Result.html')
