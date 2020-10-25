from django.db import models
from django.contrib.auth import get_user_model

from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True)
    description = models.CharField(max_length=100)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(get_user_model(), related_name='company', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'name={self.name}'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, blank=True)

    def __str__(self):
        return f'code={self.code}'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    cat = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64)
    desc = models.CharField(max_length=32)
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    posted = models.DateField(max_length=32)


class Application(models.Model):
    written_username = models.CharField(max_length=32)
    written_phone = models.CharField(max_length=15)
    written_cover_letter = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='applications', on_delete=models.CASCADE)
