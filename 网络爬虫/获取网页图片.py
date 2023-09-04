import sys
import requests
import os

url = 'https://www.example.com/image.jpg'

try:
    response = requests.get(url)
    response.raise_for_status() # Raise an exception if the status code is not 200
except requests.exceptions.RequestException as e:
    print('Error:', e)
    sys.exit(1)

try:
    with open(os.path.join(os.getcwd(), 'image.jpg'), 'wb') as f:
        f.write(response.content)
        print('Image saved successfully')
except IOError as e:
    print('Error saving image:', e)



