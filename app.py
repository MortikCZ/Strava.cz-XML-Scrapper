import requests

def fetch_menu(id_jidelny):
    url = f"http://www.strava.cz/foxisapi/foxisapi.dll/istravne.istravne.process?xmljidelnickyA&zarizeni={id_jidelny}&jazyk=CZ&httphlavicka=A"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")