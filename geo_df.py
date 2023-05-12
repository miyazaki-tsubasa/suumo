import requests

api_key = 'AIzaSyDDZ3yTODmzCLdcFAS_RNb4QGo3MenvGgw'
address = '東京都新宿区西落合３'

url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

response = requests.get(url)
data = response.json()

if data['status'] == 'OK':
    location = data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
    print(f'経度: {longitude}, 緯度: {latitude}')
else:
    print('Geocodingに失敗しました')