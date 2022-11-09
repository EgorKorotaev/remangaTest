## 1 установка
```commandline
pip install -r requirements.txt
```


## 2 запуск
```commandline
cd mysite   
python manage.py runserver
```
* http://localhost:8000/admin
* login: admin
* password: admin


## 3 api
* http://localhost:8000/api/ : root
* http://localhost:8000/api/title/ : Список всех **тайтлов** 
* http://localhost:8000/api/title/?page=2 : Список всех тайтлов, **вторая страница**
* http://localhost:8000/api/title/1/ : Подробное описание **тайтла 1**
* http://localhost:8000/api/volume/ : Список всех **томов**
* http://localhost:8000/api/volume/1/ : Подробное описание **тома 1**
* http://localhost:8000/api/chapter/ : Список всех **глав**
* http://localhost:8000/api/chapter/2/ : Подробное описание **главы 2** + **увеличивается счётчик просмотров + 1**
* http://localhost:8000/api/chapter/2/like/ : **Увеличение счётчика лайков на 1** 
* http://localhost:8000/api/tag/ : Список всех **тегов**
* http://localhost:8000/api/tag/1 : Подробное описание **тега 1**