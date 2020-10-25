#!/usr/bin/env python
import datetime
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from job_offer.data import vacancies, companies, specialties
from job_offer.models import Company, Vacancy, Specialty


if __name__ == '__main__':
    Specialty.objects.all().delete()
    Company.objects.all().delete()
    Vacancy.objects.all().delete()

    for company_data in companies:
        company = Company.objects.create(**company_data)

    for specialty_data in specialties:
        specialty = Specialty.objects.create(**specialty_data)

    for vacancy_data in vacancies:
        specialty = Specialty.objects.get(code=vacancy_data['cat'])
        company = Company.objects.get(name=vacancy_data['company'])
        vacancy = Vacancy.objects.create(title=vacancy_data['title'],
                                         cat=specialty,
                                         company=company,
                                         salary_from=vacancy_data['salary_from'],
                                         salary_to=vacancy_data['salary_to'],
                                         desc=vacancy_data['desc'],
                                         posted=vacancy_data['posted'],
                                         skills=vacancy_data['skills'])
