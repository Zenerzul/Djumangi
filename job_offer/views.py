from django.http import Http404
from django.shortcuts import render
from django.views import View

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
            header = Specialty.objects.get(code=specialization)
            return render(request, 'job_offer/vacancies.html', context={
                'vacancies': sorted_vacancies,
                'header': header,
            })
        except Specialty.DoesNotExist:
            raise Http404



class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return render(request, 'job_offer/vacancy.html', context={
                'vacancy_data': vacancy,
            })
        except Vacancy.DoesNotExist:
            raise Http404


class CompanyView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
            return render(request, 'job_offer/company.html', context={
                'company_data': company,
            })
        except Company.DoesNotExist:
            raise Http404
