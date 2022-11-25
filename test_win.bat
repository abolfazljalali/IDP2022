@echo off
title IDP Group 4 server
cd src/idp_web

echo:
echo:
echo ------------------------------------------
echo IDP Group 4 Django server automated tests
echo ------------------------------------------
echo:
echo:

python manage.py test

pause