from telethon import TelegramClient, events
import configuration
import functions

client = TelegramClient(configuration.sessao, configuration.api_id, configuration.api_hash)

print('[SIM - BOT] - INICIADO COM SUCESSO...')
 
#functions.All()
functions.MessageCapture(client)

client.start()
client.run_until_disconnected()


<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');
header('Access-Control-Allow-Credentials: true');
header('Content-Type: application/json');

session_start();

$auth_url = 'https://m-parceiros.lendasbet.com/pt/partner/login';

$auth_data = [
    'l_username' => 'lucasapi',
    'l_password' => '3llcb231',
];

$csv_url = 'https://m-parceiros.lendasbet.com/pm/pt/partners/pendingpartnersjson';

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $auth_url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($auth_data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookies.txt');
curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookies.txt');

$response = curl_exec($ch);

if ($response === false) {
    echo 'Erro ao fazer a primeira solicitação CURL: ' . curl_error($ch);
    exit;
}

curl_setopt($ch, CURLOPT_URL, $csv_url);
curl_setopt($ch, CURLOPT_HTTPGET, true);

$csv_response = curl_exec($ch);

curl_close($ch);

echo json_encode($csv_response);
?>
