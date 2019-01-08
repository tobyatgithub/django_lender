# django_lender

In this repository, I implement the concept of Docker and working within containers as a part of my developer workflow. As compared to Flask, django shall significantly improve the development speed.

# Log
1/7/19:  
First implement with basic steps:
1. call code below to create the basic framework at local directory.
```bash
django-admin startproject <project_name> .
```  

2. create docker-compose.yml file to specify volumes of database, volumes of web, and volumes that communicates between. It also specify the entry point for the app.  

3. create Dockerfile to specify the source of python, build environment structure of container and set some python env features.  

4. create entrypoint.sh to specify the version of bash for containers, initialize bash environment, and run manage.py commands.  

5. modify setting.py to move Secret_key, debug, allowed_hosts, and database settings to .env file.  