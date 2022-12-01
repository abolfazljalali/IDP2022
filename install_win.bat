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
echo -------------------------------
echo Making a virtual environment...
echo -------------------------------
echo:

cd ..
python -m venv IDP2022-main

echo:
echo:
echo -----------------------------
echo Source activating the venv...
echo -----------------------------
echo:

cd IDP2022-main/Scripts
call activate.bat

echo:
echo:
echo --------------------------------
echo Installing required libraries...
echo --------------------------------
echo:

pip install django
pip install pillow
pip install tifffile
pip install requests
pip install mysql-connector-python
pip install opencv-python

echo:
echo:
echo ---------------------
echo Making migrations...
echo ---------------------
echo:

cd ../src/idp_web
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
echo ------------------------------------------------
echo Installation complete
echo Run the django server with start_django_win.bat
echo Run the UI with start_ui_win.bat
echo ------------------------------------------------
echo:

pause
