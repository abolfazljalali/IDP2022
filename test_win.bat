@echo off
title IDP Group 4 automated testing

echo:
echo:
echo -----------------------------
echo Source activating the venv...
echo -----------------------------
echo:

cd Scripts
call activate.bat

echo:
echo:
echo ------------------------------------------
echo IDP Group 4 Django server automated tests
echo ------------------------------------------
echo:
echo:

cd ../src/idp_web
python manage.py test

pause
