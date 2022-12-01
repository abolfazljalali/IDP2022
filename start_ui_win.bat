@echo off
title IDP Group 4 UI PHP server

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
echo -------------------------------------
echo Migrating files from Django to PHP...
echo -------------------------------------
echo:

cd ../src/ui
python transfer.py

echo:
echo:
echo ---------------------------------------------------
echo IDP Group 4 PHP server
echo:
echo Leave this cmd running in the background and
echo navigate through the server using the web browser
echo and going to localhost:3000
echo ---------------------------------------------------
echo:
echo:

php -S 127.0.0.1:3000
