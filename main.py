from telethon import TelegramClient, events
import configuration
import functions

client = TelegramClient(configuration.sessao, configuration.api_id, configuration.api_hash)

print('[SIM - BOT] - INICIADO COM SUCESSO...')
 
#functions.All()
functions.MessageCapture(client)

client.start()
client.run_until_disconnected()


