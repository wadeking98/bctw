# bctw
application to record BC biology telemetry data

To run the application simply run ```docker-compose up```
**Note: you must apply database migrations before using the app**  

log into the container with ```docker exec -it bctw_django_1 /bin/bash```  
once in the container run ```./init.sh```, this will apply the database migration  
If you would like to load some test data then type ```cd tashis``` in the container
and then ```python3 manage.py shell < load_dat.py```
