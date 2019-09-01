

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import datetime
import random
import time
import os
token = os.environ.get('TOKEN')
vk_session = vk_api.VkApi( token=token)


session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def minutes():
    x=str(datetime.datetime.now())
    y=x[11:]
    minutes=y[3:5]
    seconds=y[6:]
    return int(minutes)
def seconds():
    x=str(datetime.datetime.now())
    y=x[11:]
    minutes=y[3:5]
    seconds=y[6:]
    return int(seconds[0:2])


while True:
    for event in longpoll.listen():
        if(minutes()%5==0):    
            mastmp=vk_session.method('wall.get', {'owner_id': '-163915966','count': 20})
            x=len(mastmp["items"])
            for i in range (0,x):
                if(str(mastmp["items"][i]['from_id'])=='414517334'):
                    print(mastmp["items"][i]['id'])
                    vk_session.method('wall.delete', {'owner_id': '-163915966','post_id': str(mastmp["items"][i]['id'])})
            mastmp2=vk_session.method('wall.get', {'owner_id': '-137821135','count': 20})
            y=len(mastmp2["items"])
            for i in range (0,y):
                if(str(mastmp2["items"][i]['from_id'])=='414517334'):
                    print(mastmp2["items"][i]['id'])
                    vk_session.method('wall.delete', {'owner_id': '-137821135','post_id': str(mastmp2["items"][i]['id'])})
            vk_session.method('wall.post', {'owner_id': '-163915966','message': "#1server.Рассматриваю предложения на автомобиль. Тонер старый - 108%.","attachment":"photo-177844818_457239078"})
            time.sleep(60)
            
