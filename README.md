# Industrial Project Course / 2022

Dear Collaborators,
In order to run this project, it is always better to make a separate virtual environment, and add the current respository components to your project.

#### Step 1:
If you are using Mac/Linux, please open a terminal and make a virtual environments using the command below:
```
python -m venv <your-project-name>
```

remember, your accessible binaries may have different name for python executable, then, please make sure you try the available binary file on your computer. For example, you may need to run this code:
```
python3 -m venv <your-project-name>
```

#### Step 2:

After creating your virtual environment, remember to **source** the **activate** bash file upon your terminal using the command below:

```
source /<your-project-address>/bin/activate
```

#### Step 3:

In this step, install required libraries using the command mentioned below:

```
pip install django
pip install pillow
pip install tifffile
```
#### Step 4:

Download the repository from the github, and put the code in the main directory of your project. The project tree should look like this:
```
- <your-project-name>
| - bin
| - lib
| - include
| - src
  | - idp_web
    | - frontal
    | - idp_web
    | - manage.py
```

#### Step 5:
After putting the code in the right place, you'll need to run the migration commands in order to create the database. For that purpose, run the command below:
```
python manage.py makemigrations
python manage.py makemigrations frontal
python manage.py migrate
```

#### Step 6:
After running the migration commands, you can access the model and admin control panel by creating a super user as mentioned below:
```
python manage.py createsuperuser
```

It will ask for your username, email, and password. Fill them carefully and create your own user.

#### Step 7:

In order to run the code, please run the code below:
```
python manage.py runserver
```


If you have any question, please put them in the issue section or ask them on the discord!
