import requests

from .tasks import div


response = requests.get('https://google.com')

if response.status_code == 200:
    div.apply_async((10,2))

print('done')
