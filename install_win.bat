@echo off

title IDP Group 4 server installation

echo:
echo:
echo ----------------------------------------------------
echo IDP Group 4 server installation
echo:
echo Make sure you have Python 3.10 with Pip installed!
echo ----------------------------------------------------

echo:
echo:
echo --------------------------------
echo Installing required libraries...
echo --------------------------------
echo:

pip install django
pip install pillow

echo:
echo:
echo ---------------------
echo Making migrations...
echo ---------------------
echo:

cd src/idp_web
python manage.py makemigrations
python manage.py makemigrations frontal
python manage.py migrate

echo:
echo -------------------------------
echo Creating superuser...
echo:
echo Please fulfill this form
echo:
echo For development purposes,
echo use name and password
echo that can be easily remembered!
echo -------------------------------

python manage.py createsuperuser

echo:
echo ----------------------------------
echo Installation complete
echo Run the server with start_win.bat
echo ----------------------------------
echo:

pause