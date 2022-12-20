db:
	docker run -itd --name db --rm \
	-p 3306:3306 \
	-e MYSQL_ROOT_PASSWORD=awanawan \
	mysql \
	--default-authentication-plugin=mysql_native_password
