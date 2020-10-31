from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from job_offer.views import MainView, AllVacanciesView, VacancyView, VacancyBySpecialisationView, CompanyView, \
    AllCompaniesView, MySignupView, MyLoginView, MyCompanyView, MyCompanySingleVacancyView, \
    MyCompanyVacanciesView, SentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),

    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', MySignupView.as_view(), name='register'),

    path('vacancies/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:specialization>', VacancyBySpecialisationView.as_view(),
         name='vacancy_by_specialisation'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<vacancy_id>/send', SentView.as_view(), name='send'),

    path('companies/<int:company_id>', CompanyView.as_view(), name='company'),
    path('companies/', AllCompaniesView.as_view(), name='all_companies'),

    path('mycompany/', MyCompanyView.as_view(), name='my company'),
    path('mycompany/vacancies', MyCompanyVacanciesView.as_view(), name='my company all vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>', MyCompanySingleVacancyView.as_view(),
         name='my company single vacancy'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
