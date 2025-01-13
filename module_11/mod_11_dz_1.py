import pprint
import requests
import pandas as pd
from PIL import Image

#=======================Requests=======================================
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
    if k == 'api_path':
        link_path.append('https://genius.com' + ret_data[k])

print(f'Song path:{link_path}\n')

#=======================Pandas==========================
df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Gamer'],
                  [3,'Scott', 'Candle']], columns=['Id','Name', 'Work'])

print(df.sort_values(by='Work'))
def writeDframe(dataFrame, fname):
    ex_writer = pd.ExcelWriter(fname, engine='xlsxwriter')
    dataFrame.to_excel(ex_writer, index=False)
    ex_writer._save()

test = pd.read_csv("test.csv",sep=';')
print(test)
df.to_excel('test.xlsx', index=False)

writeDframe(test, 'out.xlsx')

#==========================Pillow=======================
# data = []
# for image in range(1,12):
#     data.append(f'./images/00{image}.png')
img_files = [f'./images/00{i}.png' for i in range(1,12)]

for img_path in img_files:
    image = Image.open(img_path)
    image = image.resize((640,480))
    image.save(img_path+'.jpg')

