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

from job_offer.forms import MyUserCreationForm, ApplicationForm, MyCompanyForm, MyVacancyForm
from job_offer.models import Specialty, Company, Vacancy, Application


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
        header = 'Вакансии'
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
            'form': ApplicationForm
        })

    def post(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            application = Application.objects.create(
                written_username=form_data['written_username'],
                written_phone=form_data['written_phone'],
                written_cover_letter=form_data['written_cover_letter'],
                vacancy=vacancy,
                user=User.objects.get(username=request.user)
            )
            return redirect('send', vacancy_id)
        return render(request, 'job_offer/vacancy.html', {'form': form.errors})


class SentView(View):
    def get(self, request, vacancy_id):
        return render(request, 'job_offer/sent.html', context={
            'vacancy_id': vacancy_id,
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
        try:
            Company.objects.get(owner=request.user)
            return render(request, 'job_offer/company-edit.html', {'form': MyCompanyForm})
        except Company.DoesNotExist:
            Company.objects.create(
                name='i',
                logo='',
                employee_count=0,
                location='00',
                description='',
                owner=request.user
            )
            return render(request, 'job_offer/company-create.html')

    def post(self, request):
        form = MyCompanyForm(request.POST)
        mycompany = Company.objects.get(owner=request.user)
        mycompany.delete()
        if form.is_valid():
            form_data = form.cleaned_data
            mycompany = Company.objects.create(
                name=form_data['name'],
                logo='/static/random_logo.png',
                employee_count=form_data['employee_count'],
                location=form_data['location'],
                description=form_data['description'],
                owner=request.user
            )
            return redirect('mycompany')
        return render(request, 'job_offer/company-edit.html', {'form': form.errors})


class MyCompanyVacanciesView(View):
    def get(self, request):
        mycompany_vacancies = Vacancy.objects.filter(company=Company.objects.get(owner=request.user))
        return render(request, 'job_offer/vacancy-list.html', context={
            'mycompany_vacancies': mycompany_vacancies,
        })


class MyCompanyCreateVacancyView(View):
    def get(self, request):
        return render(request, 'job_offer/vacancy-edit.html', {'form': MyVacancyForm})

    def post(self, request):
        form = MyVacancyForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            vacancy = Vacancy.objects.create(
                title=form_data['name'],
                company=Company.objects.get(owner=request.user),
                cat=Specialty.objects.get(code=form_data['cat']),
                salary_from=form_data['salary_from'],
                salary_to=form_data['salary_to'],
                published=form_data['published'],
                skills=form_data['skills'],
                desc=form_data['desc']
            )
            vacancy.save()
            return redirect('/')
        return render(request, 'job_offer/vacancy-edit.html', {'form': form.errors})


class MyCompanySingleVacancyView(View):
    def get(self, request, vacancy_id):
        return render(request, 'job_offer/vacancy-edit.html', {'vacancy_id': vacancy_id, 'form': MyVacancyForm})


    def post(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        vacancy.delete()
        form = MyVacancyForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_vacancy = Vacancy.objects.create(
                title=form_data['title'],
                cat=form_data['cat'],
                company=Company.objects.get(owner=request.user),
                skills=form_data['skills'],
                salary_from=form_data['salary_from'],
                salary_to=form_data['salary_to'],
                published=form_data['published']
            )
            return redirect('mycompany_all_vacancies')
        return render(request, 'job_offer/vacancy-edit.html', {'form': form.errors})


class MySignupView(CreateView):
    form_class = MyUserCreationForm
    success_url = 'login'
    template_name = 'login_templates/register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_templates/login.html'
