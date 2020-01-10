python3 manage.py startapp app_name
docker-compose build
docker-compose run
docker-compose run web python manage.py loaddata techs
docker-compose run web python manage.py loaddata tools
