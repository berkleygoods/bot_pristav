import requests

def parse_data(user_data):
    print(user_data)

# url = f'https://api-ip.fssp.gov.ru/api/v1.0/search/physical?token={token}&region={region}&firstname={name}&secondname={secondname}&lastname={lastname}&birthdate={birthday}'
# token = '5wX4GPGWz6ZT'
# url = 'https://api-ip.fssp.gov.ru/api/v1.0/search/physical'
# params = {                     # параметры,которые вставляются в url для запроса
#     'token': token,
#     'region': region,
#     'name': name,
#     'secondname': secondname,
#     'lastname': lastname,
#     'birthday': birthday
# }
# print(url)
# res = requests.get(url, params=params)       # вставляем их
# res_dict = res.json()                        # для результата нужен task, поэтому мы переводим в json
# task = res_dict.get('response').get('task')   # достаем task
# prms = {                               # новые пармаетры с таск
#     'token': token,
#     'task': task,
# }
# result = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/result', params=prms)
# print(result.text)
# result_dict = result.json()
# debt = result_dict.get('subject')     # ключ subject-задолженность,делаем тоже самое чтобы его достать
# print(debt)
# if debt:
#     print('bad')
# if not debt:
#     print('lit')


#from bs4 import BeautifulSoup
#import urllib.request
#f = urllib.request.urlopen("https://api-ip.fssp.gov.ru/swagger").read()
#print(f)

#soup = BeautifulSoup(f, 'lxml')
