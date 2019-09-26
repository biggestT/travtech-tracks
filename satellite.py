import requests

def get_img(row, apikey):
    code = row['code']
    lat = row['latitude']
    long = row['longitude']
    coord = f'{lat},{long}'
    params = {
        'center': coord,
        'zoom': 16,
        'size': '600x400',
        'scale': 1,
        'maptype': 'satellite',
        'key': apikey 
    }
    url = 'https://maps.googleapis.com/maps/api/staticmap'
    r = requests.get(url = url, params = params, stream=True)
    return (code, r.raw)
