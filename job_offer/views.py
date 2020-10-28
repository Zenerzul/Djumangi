from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.decorators.http import require_POST
# from job_offer.forms import UserRegisterForm
from job_offer.forms import UserRegisterForm, UserLoginForm
from job_offer.models import Specialty, Company, Vacancy


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        return render(request, 'job_offer/index.html', context={
            'specialties': specialties,
            'companies': companies
        })


class AllVacanciesView(View):
    def get(self, request):
        all_vacancies = Vacancy.objects.all()
        header = 'Все вакансии'
        return render(request, 'job_offer/vacancies.html', context={
            'vacancies': all_vacancies,
            'header': header
        })


class AllCompaniesView(View):
    def get(self, request):
        all_companies = Company.objects.all()
        header = 'Компании'
        return render(request, 'job_offer/companies.html', context={
            'companies': all_companies,
            'header': header
        })


class VacancyBySpecialisationView(View):
    def get(self, request, specialization):
        try:
            sorted_vacancies = Vacancy.objects.filter(cat__code=specialization)
            specialty = Specialty.objects.get(code=specialization)
        except Specialty.DoesNotExist:
            raise Http404
        return render(request, 'job_offer/vacancies.html', context={
            'vacancies': sorted_vacancies,
            'header': specialty,
        })


class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            raise Http404
        return render(request, 'job_offer/vacancy.html', context={
            'vacancy': vacancy,
        })


class CompanyView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            raise Http404
        return render(request, 'job_offer/company.html', context={
            'company': company,
        })


class MyCompanyView(View):
    def get(self, request):
        return render(request, 'job_offer/company.html')
        # try:
        #     my_company = Company.objects.get(id=company_id)
        # except Company.DoesNotExist:
        #     raise Http404
        # return render(request, 'job_offer/company.html')
        # context={
        #     'company': my_company,
        # })


class MyCompanyVacanciesView(View):
    def get(self, request):
        my_company_vacancies = Vacancy.objects.all()
        header = 'Наши вакансии'
        return render(request, 'job_offer/vacancies.html', context={
            'vacancies': my_company_vacancies,
            'header': header
        })


class MyCompanySingleVacancyView(View):
    def get(self, request, vacancy_id):
        try:
            my_vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            raise Http404
        return render(request, 'job_offer/vacancy.html', context={
            'vacancy': my_vacancy,
        })


class MySignupView(View):
    def get(self, request):
        return render(request, 'login_templates/register.html', {'form': UserRegisterForm})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )
            return redirect('/')
        return render(request, 'login_templates/register.html', {'form': form.errors})


class MyLoginView(View):
    def get(self, request):
        return render(request, 'login_templates/login.html', {'form': UserLoginForm})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            return redirect('/')
        return render(request, 'login_templates/login.html', {'form': form.errors})
