#!/bin/bash

# vars
DB_CONTAINER="mysql_db"
DB_USER="admin"
DB_PASS="LogisticaSur2021"
SQL_SCRIPT="/etc/zona_precio.sql"

if [ $(id -u) -ne 0 ]; then
	echo;echo "[!] You must run this script as root (sudo $0).";echo
else
	sudo docker build LogisticaSur/ --tag "logisticasur-img:1.0" && \
	sudo docker-compose up --detach && \
	sudo docker cp sql/zona_precio.sql ${DB_CONTAINER}:/etc/
	echo
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (10%)\r"
        sleep 1
        echo -ne "[!] 'Initialize.sh' is still finishing wait...  (28%)\r"
        sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (45%)\r"
	sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (78%)\r"
	sleep 1
	echo -ne "[!] 'Initialize.sh' is still finishing wait...  (100%)\r"
	echo -n ""

	for i in {1..30}; do
		docker exec -i ${DB_CONTAINER} /bin/bash -c "mysql -u ${DB_USER} -p${DB_PASS} < ${SQL_SCRIPT}" > /dev/null 2>&1
		if [ $? -eq 0 ]; then
			echo;echo;echo "[+] 'Initialize.sh' has terminated successfully.";echo
			break
		fi
		sleep 1
	done
fi
