from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import json
import requests
from bs4 import BeautifulSoup
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

API_KEY = '5323340737:AAHyYYVzXZuPVP_vvbnIGnhJvnTMxiu_QAo' #robot parskala
#URL = []
URLA13464 = "https://torob.com/p/c248e83f-2af8-4957-8a91-5e72a0f3acef/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA134128 = "https://torob.com/p/328b901a-74d4-4be0-94e5-0b5e064fe42c/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA136128 = "https://torob.com/p/79cdc70c-8d97-4852-a8ae-066ee0d7febd/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA738128 = "https://torob.com/p/75df54e8-a14d-4118-827f-1ba9409ca029/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a73-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA738256 = "https://torob.com/p/b768a136-d151-4abd-9072-7724158b21cc/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a73-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA326128 = "https://torob.com/p/efea46ec-17d5-40d2-b481-82d2cf45ef26/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a32-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA328128 = "https://torob.com/p/918f1ea2-bb87-4f2d-b4e1-acfebc398ae7/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a32-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS21FE6128 = "https://torob.com/p/00c7c08e-2843-4ec7-acc8-7b9cbd7086be/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s21-fe-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS21FE8128 = "https://torob.com/p/80585ad0-9765-440a-879f-a0b2a284d295/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s21-fe-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS21FE8256 = "https://torob.com/p/1d271685-1c53-48f8-a419-ebc9f33cfe00/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s21-fe-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA536128 = "https://torob.com/p/7e42a036-c5a8-4611-905c-8254e3187d22/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a53-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA538128 = "https://torob.com/p/79d0860e-5ae0-475f-94bd-4b7ac5aa4b44/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a53-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA538256 = "https://torob.com/p/3e7e8907-cd2a-4668-b8ea-8017eeed6f64/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a53-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA336128 = "https://torob.com/p/797675a2-dfb0-4581-8507-33603cb021fd/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a33-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA338128 ="https://torob.com/p/b9a493fa-d381-4f14-892b-82ad8a55ce4b/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a33-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLM13464 = "https://torob.com/p/80853558-43b5-4003-80af-a3cc912353ad/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-m13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLM134128 = "https://torob.com/p/ef81dde3-fba3-4641-ac63-fcd58f7c03d0/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-m13-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLM32464 = "https://torob.com/p/09f68537-59e9-4a9d-a2fd-67f3f0304daf/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-m32-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLM326128 = "https://torob.com/p/a44e381d-55d1-4c8a-bb9c-86bfa8104e6c/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-m32-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLM328128 = "https://torob.com/p/6d2e1a8d-3248-4dc0-b4ef-8f5dce336fec/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-m32-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA23464 = "https://torob.com/p/eef9da8b-69b0-4f57-b51b-2aad299b6eda/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a23-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-64-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA234128 = "https://torob.com/p/b0b6b7b3-d1d9-4cfb-b0d8-8cc0a95b02f3/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a23-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA236128 = "https://torob.com/p/3f85efce-55a0-41e0-b1fc-e8b3266ff394/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a23-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLA238128 = "https://torob.com/p/d19bfb12-94a5-465f-a937-cb887bf9e050/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-a23-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS22ULTRA8128 = "https://torob.com/p/0a7b1ae8-eee6-492d-ab35-609f5f38cfc0/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s22-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS22ULTRA12128 = "https://torob.com/p/d6370082-830a-4293-aea7-c9179acf51fe/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s22-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"
URLS22ULTRA12512 = "https://torob.com/p/7262ea66-5a63-4680-b20e-3f770186508a/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-s22-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-512-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"

listURLs =[URLA13464,URLA134128, URLA136128,URLA738128, URLA738256, URLA326128, URLA328128, URLS21FE6128, URLS21FE8128, URLS21FE8256, URLA536128, URLA538128, URLA538256, URLA336128, URLA338128, URLM13464, URLM134128, URLM32464, URLM326128, URLM328128, URLA23464, URLA234128, URLA236128, URLA238128, URLS22ULTRA8128, URLS22ULTRA12128]
flistURLs =['URLA13464', 'URLA134128', 'URLA136128', 'URLA738128', 'URLA738256', 'URLA326128', 'URLA328128', 'URLS21FE6128', 'URLS21FE8128', 'URLS21FE8256', 'URLA536128', 'URLA538128', 'URLA538256', 'URLA336128', 'URLA338128', 'URLM13464', 'URLM134128', 'URLM32464', 'URLM326128', 'URLM328128', 'URLA23464', 'URLA234128', 'URLA236128', 'URLA238128', 'URLS22ULTRA8128', 'URLS22ULTRA12128']
URL_keyboard1 = [['Samsung'],['Xiaomi'],['Apple'],['Poco']]
URL_samsung = [['A13','A23','A33','A53'],['A32','M32','M13'],['A73','S21FE',],['S22ULTRA']]
URL_xiaomi = [['note11','Note 11s'],['AS'],['note 11 pro'],['M4 pro']]
URL_apple = [['13 pro max'],['13 pro'],['11'],['13']]
URL_poco = [['X4 pro 4g'],['M4 pro 4g'],['X4 pro 5g'],['M4 pro 4g']]
#STORE AND RAM OF MODEL KEYBORD
keybordA13 = [['4/64','4/128','6/128']]
keybordA73 = [['8/128','8/256']]
keybordA32 = [['6/128','8/128']]
keybordS21FE = [['6/128','8/128','8/256']]
keybordA53 = [['6/128','8/128','8/256']]
keybordA33 = [['6/128','8/128']]
keybordM13 = [['4/64','6/128','8/128']]
keybordA23 = [['4/64','4/128','6/128','8/128']]
keybordS22ULTRA = [['8/128','12/256','12/512']]
#SETING OF KEYBORD BRAND
markup = ReplyKeyboardMarkup(URL_keyboard1, resize_keyboard=True, one_time_keyboard=True)
markup1 = ReplyKeyboardMarkup(URL_samsung, resize_keyboard=True, one_time_keyboard=True)
markup2 = ReplyKeyboardMarkup(URL_xiaomi, resize_keyboard=True, one_time_keyboard=True)
markup3 = ReplyKeyboardMarkup(URL_apple, resize_keyboard=True, one_time_keyboard=True)
markup4 = ReplyKeyboardMarkup(URL_poco, resize_keyboard=True, one_time_keyboard=True)
#SETING OF KEYBORD MODEL SAMSUNG
markupA13 = ReplyKeyboardMarkup(keybordA13, resize_keyboard=True, one_time_keyboard=True)
markupA73 = ReplyKeyboardMarkup(keybordA73, resize_keyboard=True, one_time_keyboard=True)
markupA32 = ReplyKeyboardMarkup(keybordA32, resize_keyboard=True, one_time_keyboard=True)
markupS21FE = ReplyKeyboardMarkup(keybordS21FE, resize_keyboard=True, one_time_keyboard=True)
markupA53 = ReplyKeyboardMarkup(keybordA53, resize_keyboard=True, one_time_keyboard=True)
markupA33 = ReplyKeyboardMarkup(keybordA33, resize_keyboard=True, one_time_keyboard=True)
markupM13 = ReplyKeyboardMarkup(keybordM13, resize_keyboard=True, one_time_keyboard=True)
markupA23 = ReplyKeyboardMarkup(keybordA23, resize_keyboard=True, one_time_keyboard=True)
markupS22ULTRA = ReplyKeyboardMarkup(keybordS22ULTRA, resize_keyboard=True, one_time_keyboard=True)
##SETING OF KEYBORD MODEL APPLE

#SETING OF KEYBORD MODEL XIAOMI

#SETING OF KEYBORD MODEL POCO


BRAND , ENDIA, MODEL , HAFEZ = range(4)
#model_goshi= "a1"
#START BOT
print("bot started!")
def start (update,context):
    update.message.reply_text('سلام برند مورد نظر را انتخاب کنین!',reply_markup=markup)
    return BRAND

def brand(update,context):
    brand_goshi = str(update.message.text).lower()
    print(brand_goshi)
    if brand_goshi in "samsung" : 
        print("samsung brand")
        return samsung(update,context)
    if brand_goshi in "xiaomi" : 
        print("xiaomi brand")
        return xiaomi(update,context)
def xiaomi (update,context):
    print("xiaomi function")
    update.message.reply_text('مدل مورد نظر رو انتخاب کن!',reply_markup=markup2)
    return MODEL

def samsung (update , context ):
    print("this is a samsung func")
    update.message.reply_text('مدل مورد نظر رو انتخاب کن!',reply_markup=markup1)
    #model = update.message.text
    return MODEL

def model(update,context):
    print("modle function")
    global model_goshi
    model_goshi = str(update.message.text).upper()
    print(model_goshi)
    
    if model_goshi in "A13" : update.message.reply_text('حافظه و رم مورد نظر را انتخاب کنید:',reply_markup=markupA13)
    if model_goshi in "A23" : update.message.reply_text('حافظه و رم مورد نظر را انتخاب کنید:',reply_markup=markupA23)
    #moddel_func()
    #return model_goshi
    
    return HAFEZ
    

def cancle (update,context):
    global URL
    #print(update.message.chat_id)
    URL = URLA13464
    getdata(URL,update,context)


    #print(context)
    return ConversationHandler.END
'''
def model_samsung(update,context):
    print("this is model samsung")
    model = update.message.text
    print(model)
    update.message.reply_text('مدل مورد نظر رو انتخاب کن!',reply_markup=markup1)
    return HAFEZ
'''
'''
def moddel_func():
    print("this function is moddel func")
    return HAFEZ
'''
def hafeze(update,context):

    print("this is hafeze")
    hafeze = str(update.message.text)
    print(hafeze)
    if hafeze in "4/64" : hafeze1=464
    if hafeze in "4/128" : hafeze1=4128
    if hafeze in "6/128" : hafeze1=str(6128)
    if hafeze in "8/128" : hafeze1="8128"
    if hafeze in "8/256" : hafeze1="8256"
    if hafeze in "12/256" : hafeze1="12256"
    if hafeze in "12/512" : hafeze1="12512"
    print(model_goshi)
    URL = model_goshi + str(hafeze1)
    #print(URL)
    #URL= URLA13464
    page=requests.get(URL)
    print(page)
    #getdata(URL,update,context)
    return ENDIA

def getdata(update,context,URL):
    print("this is a get data func")
    #print(URL)
    update.message.reply_text("لینک دریافت شد")
    page=requests.get(URL)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    text=soup.find_all("script")[1].text
    #print(text)
    json_object = json.loads(text)
    torob_dict = json.dumps(json_object, indent = 4)
    with open("torob.json", "w", encoding="utf-8") as outfile:
        outfile.write(text)
        #print(text)
    #for i in range(30) :
    
    for i in range(10):
        q1=json.loads(text)['offers']['offers'][i]['price']
        a1=json.loads(text)['offers']['offers'][i]['name']
        update.message.reply_text(str(i) +' '+a1+' '+q1)
    update.message.reply_text(" از /start استفاده کنیداتمام فرآیند",reply_markup=ReplyKeyboardRemove())
    
def endi(update,context):
    update.message.text("endddddi!")   
    return ConversationHandler.END 
 


updater = Updater(API_KEY , use_context=True)
dp = updater.dispatcher

conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],

        states={
            BRAND:[CommandHandler('start', start), MessageHandler(Filters.text, brand)],
            MODEL:[CommandHandler('start', start), MessageHandler(Filters.text, model)],
            HAFEZ:[CommandHandler('start', start), MessageHandler(Filters.text, hafeze)],
            ENDIA:[CommandHandler('start', start), MessageHandler(Filters.text, endi)]
        },

        fallbacks=[CommandHandler('cancle', cancle)]
    )

dp.add_handler(conv_handler)


#dp.add_handler(CommandHandler("start",startcommand))
#dp.add_handler(CommandHandler("help",helpcommand))
#dp.add_handler(MessageHandler(Filters.text,message))

updater.start_polling(5)
updater.idle()