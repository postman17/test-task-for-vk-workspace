# test-task-for-vk-workspace

###Run project
```
- create and activate virtualenv
- pip install -r requirements.txt
- make initial
- make run
```
###Linters
```
- make lint
```

##Требуется написать API для простого блога
March 16, 2022

Сущности:

  – Article:

    * заголовок

    * баннер (base64)

    * дата и время создания

    * дата и время редактирования

    * richtext

  – Tag:

    * name

  – Автор (django.contrib.auth.models.User)


Ручки: 

  _ UserListView

  – ArticleViewset:

    * фильтр по тегу

    * фильтр по автору

    * свободный поиск

  – TagViewset


Технологии:

  – Python3

  – Django >= 2.0

  – Django REST framework

  – sqlite


По оформлению:

  – RESTful API

  – PEP8



