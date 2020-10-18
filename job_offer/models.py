from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    employee_count = models.IntegerField()

    def __str__(self):
        return f'name={self.name}'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)

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
