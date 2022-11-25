@echo off
title IDP Group 4 server
cd src/idp_web

echo:
echo:
echo ------------------------------------------------------------
echo IDP Group 4 Django server
echo:
echo Leave this cmd running in the background and
echo navigate through the server using the web browser
echo and going to localhost:8000
echo:
echo Use localhost:8000/admin to log in
echo Use localhost:8000/frontal/image/insert to upload an image
echo:
echo For further information about API for development purposes,
echo see Discord channel #design or contact Arren
echo ------------------------------------------------------------
echo:
echo:

python manage.py runserver