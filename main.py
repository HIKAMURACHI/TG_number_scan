#made for research purposes

import time
import re
import json
import random
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
import os.path

def stringSimple(data):
    string = json.dumps(data.stringify())
    newstr = string.replace("\\n", "")
    dataString = newstr.replace("\\t", "")
    return dataString

def getWord(start, end, data):
    word = ""
    for _ in range(end - start):
        word += str(data[start])
        start += 1
    return word

if not os.path.isfile("numbers.txt"):
    file = open("numbers.txt", 'w')
    file.write("id          phone         Name" + "\n")
    file.close()


api_id = API_ID
api_hash = 'API_HASH'
phone = 'YOUR_NUMBER'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

phoneCountry = "" #country code
phoneCode = [] #operator code
phoneLast = #last number (int)

searchWord = "user_id="
searchWord_f = 'first_name='
searchWord_l = 'last_name=' 

for code in phoneCode:
    for _ in range(9999): #range of search
        phoneLast = int(phoneLast) + 1 # step
        if len(str(phoneLast)) < 7: #add free 0 if numb less (change 7 for u country)
            phoneLast = (7-len(str(phoneLast))) * "0" + str(phoneLast)
        phoneNum = phoneCountry + str(code) + str(random.randint(1000000,9999999)) #for random search
        #phoneNum = phoneCountry + str(code) + str(phoneLast) #for step by step
        print(phoneNum, end=" - ")                
        contact = InputPhoneContact(client_id=0, phone=phoneNum, first_name="", last_name="")        
        result = client(ImportContactsRequest([contact]))          
        dataString = stringSimple(result)        
        stringStart = dataString.find(searchWord)
        stringEnd = dataString.find(',')        
        user_numb_id = getWord(stringStart + len(searchWord), stringEnd, dataString)                        
        user_id = getWord(stringStart, stringEnd, dataString)                        
        print(user_id)        
        if user_id.find('user_id') == 0:   
            result = client.get_entity(int(user_numb_id))             
            dataString = stringSimple(result)
            print(dataString)       
            stringStart = dataString.find(searchWord_f)
            stringMiddle = dataString.find(searchWord_l)     
            stringEnd = dataString.find('username=')  
            user_firstName = getWord(stringStart + len(searchWord_f), stringMiddle - 1, dataString)      
            user_lastName = getWord(stringMiddle + len(searchWord_l), stringEnd - 1, dataString)  
            userName = user_firstName + " " + user_lastName   
            file = open('numbers.txt', 'a+')
            file.write(user_numb_id + " " + str(phoneNum) + " " + userName + "\n")
            file.close()
        else:
            print("Nah")        
        time.sleep(7)
file.close()
