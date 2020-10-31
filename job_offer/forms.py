from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from job_offer.models import Application, Company, Vacancy


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = {'written_username', 'written_phone', 'written_cover_letter'}
        labels = {
            'written_username': 'Вас зовут:',
            'written_phone': 'Ваш телефон:',
            'written_cover_letter': 'Сопроводительное письмо:',
        }

    fields_order = {
        'written_username',
        'written_phone',
        'written_cover_letter',
        }


class MyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = {'name', 'logo', 'employee_count', 'location', 'description'}
        labels = {
            'name': 'Название компании',
            'logo': 'Логотип',
            'employee_count': 'Количество сотрудников',
            'location': 'География',
            'description': 'Информация о компании'
        }


class MyVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = {'title', 'cat', 'skills', 'salary_from', 'salary_to', 'posted', 'desc'}
        labels = {
            'title': 'Название вакансии',
            'cat': 'Специализация',
            'skills': 'Требуемые навыки',
            'salary_from': 'Зарплата от',
            'salary_to': 'Зарплата до',
            'posted': 'Опубликовано',
            'desc': 'Описание вакансии'
        }
