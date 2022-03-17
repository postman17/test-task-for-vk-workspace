# test-task-for-vk-workspace

Требуется написать API для простого блога
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



