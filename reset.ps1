$param1=$args[0]
write-host $param1
docker-compose down
if($param1 -eq "db" -Or $param1 -eq "all"){
	docker volume rm tashis_pgdata
	docker rm tashis_db_1
	docker rmi tashis_db
}
if($param1 -eq "django" -Or $param1 -eq "all"){
	docker rm tashis_django_1
	docker rmi tashis_django
}
if($param1 -eq "hard"){
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q)
}