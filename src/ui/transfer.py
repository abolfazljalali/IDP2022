import requests
import mysql.connector
import os
import cv2
from getpass import getpass

"""
Middleware to connect the backend
with UI in PHP.
"""

print("Connecting to database...")
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="image_gallery"
)
cursor = db.cursor()

print("Connecting to API...")
username = input("Enter Django username: ")
password = getpass("Enter Django password: ")
url = '127.0.0.1:8000'
session = requests.session()

storage = "../idp_web/storage/images/"
destination = "images/"

# Authenthicating
req = session.get('http://' + url + '/admin/login/?next=/admin/%27')
token = req.cookies['csrftoken']

login_data = {'csrfmiddlewaretoken': token, 'username': username, 'password': password}
req = session.post('http://' + url + '/admin/login/?next=/admin/', data=login_data)
token = req.cookies['csrftoken']

# Getting data from the API
header = {'X-CSRFToken': token}
req = session.get('http://' + url + '/frontal/image/', headers=header)
data = req.json()

print("Clearing existing files...")
for f in os.listdir(destination):
    os.remove(os.path.join(destination, f))
cursor.execute("TRUNCATE images")

print("Migrating files...")
for image in data:
    infile = image['fields']['file_name']
    name = infile.split('.')[0]

    # Converting the image to jpg
    read = cv2.imread(storage + infile)
    outfile = name + '.jpg'
    cv2.imwrite(destination + outfile, read, [int(cv2.IMWRITE_JPEG_QUALITY), 200])

    # Reading data
    dimensions = read.shape
    filesize = os.path.getsize(destination + outfile)

    # Inserting to database
    cursor.execute("INSERT INTO images (title, description, img, width, height, filesize) VALUES "
                   f'("{name}", "{name}", "{outfile}", {dimensions[0]}, {dimensions[1]}, {filesize})')

# Committing and closing the connection
db.commit()
db.close()

print("Done!")
