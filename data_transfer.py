#!/usr/bin/env python
from data import vacancies, companies, specialties
from job_offer.models import Company, Vacancy, Specialty

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
