# roadmap:
# 1. build an image custom docker with python3 docker image 
# merged with build syntax to execute the programmatic layer, so called logic and api layer.  
# 2. run the built docker images
# 3. the programmatic layer and Database layer run on different docker container, yet they connect and communicate with each other

db:
	docker run -itd --name db --rm \
	-p 3306:3306 \
	-e MYSQL_ROOT_PASSWORD=awanawan \
	mysql \
	--default-authentication-plugin=mysql_native_password
# -it -> interactive connection to docker, d -> detach or running the docker in background
# --name 
images:
	docker images

build:
	docker build -t virgiawanlr/backend:v1.0.0 -f ./Dockerfile .

# -t -> tag, or so called the given name of the docker image.
# -f ./Dockerfile . -> 

run:
	docker run -itd --name backend --network host \
	--volume=/home/virgiawan/project/User_SignUp_SignIn/.env:/app/.env \
	virgiawanlr/backend:v1.0.0

# --network host -> for establish the network as reliable as the localhost, if its not given, the program
# will searching the network inside the ran container

# --volume=/home/virgiawan/project/User_SignUp_SignIn/.env:/app/.env -> for making the docker volume
# docker volume -> making the entanglement of two twin-named entities (file/dir), that occur in the running container
# and on the local host working dir. whatever applied to one another will give the exact effect to its twin.
# it is applied to when user need to hide the sensitive value, such as passwords ect.

# virgiawanlr/backend:v1.0.0 -> the desire docker images to run

log:
	docker logs -f backend