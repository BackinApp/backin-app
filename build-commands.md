docker ps -a

docker build --tag backin:1.0 .

docker run --publish 8000:8000 --detach --name backin_web backin:1.0

docker run --publish 8000:8000 --name backin_web backin:1.0

docker rm --force backin_web

# -----------------
python manage.py collectstatic

gunicorn --bind :8088 --workers 16 backin.wsgi:application
