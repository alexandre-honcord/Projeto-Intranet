Iniciar o projeto

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.venv/Scripts/activate.ps1

pip install -r requeriments.txt

cd server\

py manage.py runserver
