from telethon import TelegramClient, sync, events
import configuration
import functions

#Função responsável por mostrar o ID dos grupos
def All():

    client = TelegramClient(configuration.sessao, configuration.api_id, configuration.api_hash)
    client.start()
    dialogs = client.get_dialogs()

    for dialog in dialogs:
        print('------------X-------------')
        if dialog.id < 0:
            print(f'NOME DO GRUPO: {dialog.title}')
            print(f'ID DO GRUPO: {dialog.id}')
        print('------------X-------------')
    client.disconnect()

def MessageCapture(client):
    @client.on(events.NewMessage(chats=[configuration.MINES_ID_ORIGEM, configuration.SPACEMAN_ID_ORIGEM, configuration.FORTUNE_TIGER_ID_ORIGEM,configuration.PENALTY_SHOOT_UP_ID_ORIGEM, configuration.AVIATOR_ID_ORIGEM]))
    async def relay_message(event):
        # MINES_ENVIAR_MENSAGEM
        if event.peer_id.channel_id == 1939194214 and configuration.MINES_PREFERENCE == True:
            print('SIM - MINES REPLICANDO MENSAGEM...')
            message_updated = functions.ChangeLinkAfiliate(event)
            await client.send_message(configuration.MINES_ID_DESTINO, message_updated, link_preview=False,parse_mode='html')
            return
        # SPACEMAN_ENVIAR_MENSAGEM
        if event.peer_id.channel_id == 1681284432 and configuration.SPACEMAN_PREFERENCE == True:
            print('SIM - SPACEMAN REPLICANDO MENSAGEM')
            message_updated = functions.ChangeLinkAfiliate(event)
            await client.send_message(configuration.SPACEMAN_ID_DESTINO, message_updated, link_preview=False,parse_mode='html')
            return
        # FORTUNE_TIGER_ENVIAR_MENSAGEM
        if event.peer_id.channel_id == 1925549581 and configuration.FORTUNE_TIGER_PREFERENCE == True:
            print('SIM - FORTUNE_TIGER REPLICANDO MENSAGEM')
            message_updated = functions.ChangeLinkAfiliate(event)
            await client.send_message(configuration.FORTUNE_TIGER_ID_DESTINO, message_updated, link_preview=False,parse_mode='html')
            return
        # PENALTY_SHOOT_UP_ENVIAR_MENSAGEM
        if event.peer_id.channel_id == 1938509759 and configuration.PENALTY_SHOOT_UP_PREFERENCE == True:
            print('SIM - PENALTY SHOOT UP  REPLICANDO MENSAGEM')
            message_updated = functions.ChangeLinkAfiliate(event)
            await client.send_message(configuration.PENALTY_SHOOT_UP_ID_DESTINO, message_updated, link_preview=False,parse_mode='html')
            return
        # AVIATOR_ENVIAR_MENSAGEM
        if event.peer_id.channel_id == 1592219591 and configuration.AVIATOR_PREFERENCE == True:
            print('SIM - AVIATOR REPLICANDO MENSAGEM')
            await client.send_message(configuration.AVIATOR_ID_DESTINO, event.raw_text)
            return
def ChangeLinkAfiliate(event):
    original_text = event.message.message
    updated_text = original_text.replace("CADASTRE-SE E JOGUE AQUI!", f"<a href={configuration.link_afiliado}>CADASTRE-SE E JOGUE AQUI!</a>")

    return updated_text