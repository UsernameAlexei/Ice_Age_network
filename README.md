# Django project's Ice_Age_network

# Схема приложения
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/Ice_age_map.png)

# Описание
Веб приложение представляет собой социальную сеть, позволяющую пользователям публиковать посты, смотреть новости, подписываться на профили друг друга, чтобы видеть их посты.

## Приложение позволяет:
### Зарегестрироваться и авторизоваться, после регистрации пользователю будет создан профиль.
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/ice_age_auth.gif)

### Создать свои посты с возможностью редактирования и удаления.
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/Ice_age%20post_crud.gif)

### Найти профили других пользователей и подписаться на них.
К главной странице подключен JS обновляющий информацию в постах без обновления страницы.
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/users_profiles.gif)

### Посмотреть свой профиль.
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/Ice_age_my_profile.gif)

### Посмотреть последние тизеры новостей и перейти к ним.
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/Ice_age_news.gif)

### API
![image](https://github.com/UsernameAlexei/gif_projects/blob/Ice_Age_network_material/Ice_age_api.gif)

# Развертывание
1. Клонируем репозиторий
```cmd
https://github.com/UsernameAlexei/Ice_Age_network.git
```
2. Создаем виртуальное окружеие и устанавливаем requirements.txt
```cmd
 pip install -r requirements.txt
```

3. Настраиваем параметры БД в settings.py, пример:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ice_age_network', # имя БД
        'USER': 'postgres',
        'PASSWORD': 'PostPassword',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

4. Делаем миграции
```cmd
python manage.py makemigrations
```
```cmd
python manage.py migrate
```

5. Запускаем и регистрируем нового пользователя.
```cmd
python manage.py runserver
```
