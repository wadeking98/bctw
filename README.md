# bctw
application to record BC biology telemetry data

To run the application simply run ```docker-compose up```


If you would like to populate the database with some test data, log into the container  
with ```docker exec -it bctw_django_1 /bin/bash``` once in the container run ```cd tashis```
and then ```python3 manage.py shell < load_dat.py```
