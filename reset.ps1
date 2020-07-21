$param1=$args[0]
write-host $param1
docker-compose down
if($param1 -eq "db" -Or $param1 -eq "all"){
	docker volume rm bctw_pgdata
	docker rmi bctw_db
}
if($param1 -eq "django" -Or $param1 -eq "all"){
	docker rmi bctw_django
}
if($param1 -eq "vue" -Or $param1 -eq "all"){
	docker volume rm bctw_vuedata
	docker rmi bctw_vue
}
if($param1 -eq "hard"){
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q)
	docker volume rm $(docker volume ls -q)
}