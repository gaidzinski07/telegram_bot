#!/usr/bin/python3.6
import tokens
import time
import mensagens
import random
from userList import userList
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot(tokens.bot_token)
users = userList()

def recebendoMensagem(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':

        print(content_type + " message from", msg['from']['first_name'] + "(" + str(chat_id) + "): ", msg['text'])

        if str.upper(msg['text']) == 'QUERO RECEBER':
            adicionarUser(chat_id)

        elif str.upper(msg['text']) == 'SAIR':
            removerUser(chat_id)

        elif chat_id not in users.users:
            enviarMensagem(chat_id, "Envie \"Quero receber\" para receber mensagens de 2 em 2 horas te lembrando de beber água!")

def removerUser(chat_id):
    if chat_id in users.userArray:
        users.remover(chat_id)
        enviarMensagem(chat_id, "Removido da lista.")
        print("Lista atual de user:", users.userArray)
    else:
        enviarMensagem(chat_id, "Você não está na lista ainda. Envie \"Quero receber\" para entrar.")

def adicionarUser(chat_id):
    if chat_id not in users.userArray:
        users.adicionar(chat_id)
        enviarMensagem(chat_id, "Adicionado a lista! De duas em duas horas você receberá uma mensagem te lembrando de beber água!")
        print("Lista atual de user:", users.userArray)
    else:
        enviarMensagem(chat_id, "Você já está adicionado a lista!")

def enviarMensagem(chat_id, msg):
    bot.sendMessage(chat_id, msg)

def enviarMultiplasMensagens(msg):
    for user in users.userArray:
        enviarMensagem(user, msg)

bot.message_loop(recebendoMensagem)

print("Iniciando rotina de mensagens...")

while True:
    time.sleep(2*3600)
    enviarMultiplasMensagens(mensagens.mensagens[random.randrange(len(mensagens.mensagens))])
    pass