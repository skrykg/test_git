n = int(input())
triangle = []

for i in range(n+1):
	triangle.append([1]+[0]*n)

for i in range(1,n+1):
	for j in range(1,i+1):
		triangle[i][j] = triangle[i-1][j]+triangle[i-1][j-1]


for i in range(0,n+1):
	for j in range(0,i+1):
		print(triangle[i][j], end=' ')
	print()

ulan@ulan:~/project/serv_kysgyzstan_party$ docker-compose exec web /bin/bash
root@fa12b380dde1:/usr/src/app# tail -f /var/log/supervisor/web.log 




ulan@ulan:~$ mkdir Djang
ulan@ulan:~$ cd Djang
ulan@ulan:~/Djang$ python3.7 -m venv venv
ulan@ulan:~/Djang$ source venv/bin/activate
(venv) ulan@ulan:~/Djang$ pip3 install django
Collecting django
  Cache entry deserialization failed, entry ignored
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/43/d6/0aed0b12c66527748ce5a007da4618a65dfbe1f8fca82eccedf57d60295f/Django-3.0-py3-none-any.whl (7.4MB)
    100% |████████████████████████████████| 7.4MB 133kB/s 
Collecting pytz (from django)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl
Collecting sqlparse>=0.2.2 (from django)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
Collecting asgiref~=3.2 (from django)
  Cache entry deserialization failed, entry ignored
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/a5/cb/5a235b605a9753ebcb2730c75e610fb51c8cab3f01230080a8229fa36adb/asgiref-3.2.3-py2.py3-none-any.whl
Installing collected packages: pytz, sqlparse, asgiref, django
Successfully installed asgiref-3.2.3 django-3.0 pytz-2019.3 sqlparse-0.3.0
(venv) ulan@ulan:~/Djang$ pip3 freeze
asgiref==3.2.3
Django==3.0
pkg-resources==0.0.0
pytz==2019.3
sqlparse==0.3.0
(venv) ulan@ulan:~/Djang$ mkdir app
(venv) ulan@ulan:~/Djang$ cd app
(venv) ulan@ulan:~/Djang/app$ django-admin startproject blogengine
(venv) ulan@ulan:~/Djang/app$ cd blogengine
(venv) ulan@ulan:~/Djang/app/blogengine$ python3 manage.py startappblog
Unknown command: 'startappblog'. Did you mean startapp?
Type 'manage.py help' for usage.
(venv) ulan@ulan:~/Djang/app/blogengine$ ls
blogengine  manage.py
(venv) ulan@ulan:~/Djang/app/blogengine$ python3 manage.py startapp blog
(venv) ulan@ulan:~/Djang/app/blogengine$ ./manage.py runserver 5000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

December 17, 2019 - 07:31:58
Django version 3.0, using settings 'blogengine.settings'
Starting development server at http://127.0.0.1:5000/
Quit the server with CONTROL-C.
^C(venv) ulan@ulan:~/Djang/app/blogengine$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
(venv) ulan@ulan:~/Djang/app/blogengine$ ./manage.py runserver 5000









Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from account.models import User
>>> q = User(email='test@test.ru', name='test')
>>> q.set_password('passpass')
>>> q.save()
>>> q.password
'pbkdf2_sha256$180000$YbJoXznwudi7$zlmCowLGpVFmm/9b1upFABx0zYO7qmKmLOXKFLxHoI8='
>>> 

