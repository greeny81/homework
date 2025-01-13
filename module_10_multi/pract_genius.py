import pprint
import requests
import pandas as pd

ACCESS_TOKEN = "29-gFUkSSfy7iub12HfpXPwunz8tSUJ3ECVxvS_92zMsC1MwCyqu-EnbEP3rZNyH"
RANDOM_GENRE = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
GENIUS_API_URL = "https://api.genius.com/search"

#genre = requests.get(RANDOM_GENRE).json()

link_path = []
ret_data = []
genre = "rippling candy indie"
data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
data = data.json()
try:
    ret_data = data['response']['hits'][0]['result']
except:
    pass

for k in ret_data:
    #print(f'k:{k} ')
    if k == 'api_path':
        link_path.append('https://genius.com' + ret_data[k])

print(f'Song path:{link_path}')
#===============
df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Maker']], columns=['id','name', 'occupation'])
print(df)