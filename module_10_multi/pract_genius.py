import pprint

import requests

ACCESS_TOKEN = "29-gFUkSSfy7iub12HfpXPwunz8tSUJ3ECVxvS_92zMsC1MwCyqu-EnbEP3rZNyH"
RANDOM_GENRE = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
GENIUS_API_URL = "https://api.genius.com/search"

#genre = requests.get(RANDOM_GENRE).json()
#print(genre)
genre = "brass"
data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
#pprint.pprint(data.json())
data = data.json()
pprint.pprint(data['response']['hits'][0]['result'])
ret_data = data['response']['hits'][0]['result']


print(genre)


