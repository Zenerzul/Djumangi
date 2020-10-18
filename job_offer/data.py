""" Вакансии """


vacancies = [
    {'title': 'Разработчик на Python', 'cat': 'backend', 'company': 'staffingsmarter', 'salary_from': '100000',
     'salary_to': '150000', 'posted': '2020-03-11', 'desc': 'Потом добавим',
     'skills': 'Знание SQL, Django, NumpPy, Pandas'},
    {'title': 'Разработчик в проект на Django', 'cat': 'backend', 'company': 'swiftattack', 'salary_from': '80000',
     'salary_to': '90000', 'posted': '2020-03-11', 'desc': 'Потом добавим',
     'skills': 'Знание SQL, Django, HTML, CSS, основы JS'},
    {'title': 'Разработчик на Swift в аутсорс компанию', 'cat': 'backend', 'company': 'swiftattack',
     'salary_from': '120000', 'salary_to': '150000', 'posted': '2020-03-11', 'desc': 'Потом добавим',
     'skills': 'Опыт работы в среде разработки минимум 3 года'},
    {'title': 'Мидл программист на Python', 'cat': 'backend', 'company': 'workiro', 'salary_from': '80000',
     'salary_to': '90000', 'posted': '2020-03-11', 'desc': 'Потом добавим',
     'skills': 'Опыт в области обработки данных при помощи Python. Знание библиотек Matplotlib, NumpPy, Pandas'},
    {'title': 'Питонист в стартап', 'cat': 'backend', 'company': 'primalassault', 'salary_from': '120000',
     'salary_to': '150000', 'posted': '2020-03-11', 'desc': 'Потом добавим',
     'skills': 'Без опыта работы. Уверенное владение Python3 и желание учиться новому!'}
]


""" Компании """


companies = [
    {'name': 'workiro', 'location': 'Токио', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 15000, 'logo': '/static/logo1.png'},
    {'name': 'rebelrage', 'location': 'Лондон', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 3000, 'logo': '/static/logo2.png'},
    {'name': 'staffingsmarter', 'location': 'Барселона', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 16000, 'logo': '/static/logo3.png'},
    {'name': 'evilthreath', 'location': 'Милан', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 11000, 'logo': '/static/logo4.png'},
    {'name': 'hirey', 'location': 'Москва', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 20000, 'logo': '/static/logo5.png'},
    {'name': 'swiftattack', 'location': 'Нью Йорк', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 12500, 'logo': '/static/logo6.png'},
    {'name': 'troller', 'location': 'Копенгаген', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 7000, 'logo': '/static/logo7.png'},
    {'name': 'primalassault', 'location': 'Варшава', 'description': 'Лучшие вакансии ждут Ваших резюме!',
     'employee_count': 10000, 'logo': '/static/logo8.png'}
]


""" Категории """


specialties = [
    {'code': 'frontend', 'title': 'Фронтенд', 'picture': '/static/specialties/specty_frontend.png'},
    {'code': 'backend', 'title': 'Бэкенд', 'picture': '/static/specialties/specty_backend.png'},
    {'code': 'gamedev', 'title': 'Геймдев', 'picture': '/static/specialties/specty_gamedev.png'},
    {'code': 'devops', 'title': 'Девопс', 'picture': '/static/specialties/specty_devops.png'},
    {'code': 'design', 'title': 'Дизайн', 'picture': '/static/specialties/specty_design.png'},
    {'code': 'products', 'title': 'Продукты', 'picture': '/static/specialties/specty_products.png'},
    {'code': 'management', 'title': 'Менеджмент', 'picture': '/static/specialties/specty_management.png'},
    {'code': 'testing', 'title': 'Тестирование', 'picture': '/static/specialties/specty_testing.png'}
]
