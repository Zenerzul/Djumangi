from django.contrib import admin
from django.urls import path

from job_offer.views import MainView, AllVacanciesView, VacancyView, VacancyBySpecialisationView, CompanyView, \
    AllCompaniesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:specialization>', VacancyBySpecialisationView.as_view(), name='vacancy_by_specialisation'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name='vacancy'),
    path('companies/', AllCompaniesView.as_view(), name='all_companies'),
]
