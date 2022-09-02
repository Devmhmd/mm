import time
import requests
import telebot
from telebot import *
from telebot import util
from telebot import types
tokin = "5626665627:AAEA7xieWMo4unQDaaPPAXEY158WwSKsz2E" #tokin bot

def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@devs_Team&user_id={user_id}"
    ).text
    
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return True
    else:
        return True


while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])

        def welcome(message):
            User = message.from_user.username 
            ID = message.chat.id
            channel = types.InlineKeyboardButton(
                text=" ⚒️ Channel Developer ",

                url="https://t.me/YDDCJ"

            )



            if check_user(message.from_user.id):



                start = types.InlineKeyboardButton(

                    text=" 📮 Start ",

                    callback_data="start"

                )

                programmer = types.InlineKeyboardButton(

                    text=" 👨🏻‍💻 Developer ",

                    url="https://t.me/VR_LA"

                )

                Keyboards = types.InlineKeyboardMarkup()
                Keyboards.row_width = 2
                Keyboards.add(start, programmer, channel)
                bot.reply_to(
                    message,
                    text=f"🌹| Hi {message.from_user.first_name} In Bot Send View Telegram \n📌Your Username : [ @{User} ]\n🔎Your ID : [ {ID} ]\n🔰| Please Click",

                    reply_markup=Keyboards
                )
            else:

                Keyboard = types.InlineKeyboardMarkup()
                Keyboard.row_width = 1
                Keyboard.add(channel)
                bot.reply_to(
                    message,
                    text=f"\n💖| Hi {message.from_user.first_name} \n You must subscribe to the developer's channel Then press \n                                                   /start\n🔰| Subscribe to use the bot",
                    reply_markup=Keyboard
                )

        @bot.callback_query_handler(func=lambda call: True)

        def bot_query_handler(call):
            if call.data == "start":
                run(call.message)
            elif call.data == "view":
                view_get(call.message)
            

        def run(message):
            
            view = types.InlineKeyboardButton(
                text=" ✲ SEND VIEW ✲ ",
                callback_data="view"
            )
            Key = types.InlineKeyboardMarkup()
            Key.row_width = 1
            Key.add(view)
            bot.reply_to(
                message,
                text=f"🔰| Please Click",
                reply_markup=Key
            )
        def view_get(message):
            msg = bot.reply_to(
                message,
                "\n✲ Enter Link"
            )
            bot.register_next_step_handler(msg, run_view)

        def run_view(message):
            start = bot.send_message(
                message.chat.id,
                f'✲ Starting ⏳ Please Wait ...'
            )
            time.sleep(0.5)
            link = message.text
            main_url = f'https://{link}?embed=1'
            views_url = 'https://t.me/v/?views='
            proxies = requests.get("https://apis.clouduz.ru/api/virus.php?type=all").text.splitlines()
            count_proxies = len(proxies)
            sent, bad_proxy, done, next_proxy = 0, 0, 0, 0
            _headers = {
	  'accept-language': 'en-US,en;q=0.9',
	  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
	  'x-requested-with': 'XMLHttpRequest'
	}
            B = 0
            H = 0
            S = len(proxies)
            for proxy in proxies:
            	S-=1
            	try:
            		session = requests.session()
            		session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            		session.headers.update(_headers)
            		main_res = session.get(main_url).text
            		_token = re.search('data-view="([^"]+)', main_res).group(1)
            		views_req = session.get(views_url + _token)
            		H+=1
            		Hit = (' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            	except requests.exceptions.ConnectionError:
            		B+=1
            	o = types.InlineKeyboardMarkup(row_width=1)
            	A1 = types.InlineKeyboardButton(f"❌ Bad Proxy : {B} ",callback_data="smoka")
            	A2 = types.InlineKeyboardButton(f"✅ Done send : {H}",callback_data="smoka1")
            	A4 = types.InlineKeyboardButton(f"🔎 proxy : {proxy}",callback_data="smoka3")
            	A5 = types.InlineKeyboardButton(f" 📍 Num Of List : {S}",callback_data="smoka4")
            	
            	o.add(A1,A2,A4,A5)
            	bot.edit_message_text(text="*send view now*",chat_id=int(message.chat.id),
                                message_id=start.message_id, parse_mode = "markdown",reply_markup=o) 

        try:
            print("Done")
            bot.polling(True)
        except Exception as ex:
            print(ex)
            telebot.logger.error(ex)

    except:
        continue
