1. sudo docker-compose build
Собираем наш контейнер

2. sudo docker-compose run --rm app sh
Заходим в контейнер

3. python manage.py migrate
Применяем миграции

4. python manage.py createsuperuser
	Вводим данные которые нас попосят ввести
		- Логин
		- E-mail
		- Пароль
5. exit
	Выходим из контейнера

6. sudo docker-compose up app
	Запускаем наш контейнер с приложением

7. В адресной строке браузера вводим 127.0.0.1
	Любуемся результатом. Поскольку врачи у нас не добавленны
	"Список врачей пуст"

8. В адресной строке браузера вводим 127.0.0.1/admin
	В форму заносим логин и пароль которые мы создавали на шаге 4

9. Заходим в адимнку.
	Appointments - записи на прием к врачу
	Doctors - доктора
	Specializations -специализации докторов
	Необходимо создать специальизацию, после чего можно будет создавать доктора
	и присвоить ему специализацию.

10. Перезапускаем наш контейнер

11. Снова идем по адрессу 127.0.0.1
		Видим список из докторов и специализаций которые мы создали
		По клику на имя доктора мы можем записаться к нему на прием
		В форме поиска справа можно найти доктора по его имени.
