docker-compose build
docker-compose run
docker-compose run web python manage.py loaddata techs
docker-compose run web python manage.py loaddata tools
