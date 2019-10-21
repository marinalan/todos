# todos
## Getting started
Create virtual environment in desired folder.
Example of command (feel free to replace folder for virtual environment with your own):
```
$python3.7 -m venv ~/.virtualenvs/djangopy3
```
Activate virtual environment
```
$. ~/.virtualenvs/djangopy3/bin/activate
```
To get started with the app, clone the repo and then install the needed packages:
```
$ pip install -r requirements.txt
```
Run migrations:
```
$ python manage.py migrate
```
Then to start development server:
```
$ python manage.py runserver
```
