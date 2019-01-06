import requests
from PIL import Image
from io import BytesIO



response = requests.get('https://api.nasa.gov/planetary/apod?api_key=[your_api_key]')

while response.status_code == 503:
    print(response.status_code)
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=[your_api_key]')

data = response.json()
image_url = data.get('url')    
img = Image.open(BytesIO(requests.get(image_url).content))
img.save('space.jpg')
