import requests


token = "2619421814940190"


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }


def get_intelligence_hero():
    url = 'https://superheroapi.com/api/2619421814940190/'
    headers = get_headers()
    name_list = ['Hulk', 'Captain America', 'Thanos']
    id_dict = {}

    for name in name_list:
        id = requests.get(url + 'search/' + name, headers=headers)
        list = id.json()['results']
        for dict_1 in list:
            if name == dict_1['name']:
                id_dict[int(dict_1['powerstats']['intelligence'])] = dict_1['name']

    print(f'Самый умный - {id_dict.get(max(id_dict))}. Его intelligence равен {max(id_dict)}.')
    print(f'Для сравнения - у {id_dict[sorted(id_dict)[-2]]} intelligence равен {sorted(id_dict)[-2]},'
          f' а у {id_dict[sorted(id_dict)[-3]]} intelligence равен {sorted(id_dict)[-3]}.')


get_intelligence_hero()


