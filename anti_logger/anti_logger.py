import requests, json, time, ctypes
from datetime import datetime
from colorama import Fore

with open('config.json') as config:
    config = json.load(config)

    token = config.get('token')
    delay = config.get('delay')

    password_changing = config.get('password_changing')
    
    if password_changing:
        password = config.get('password')
        another_password = config.get('another_password')
        email = config.get('email')

    webhook_logging = config.get('webhook_logging')

    if webhook_logging:
        webhook_url = config.get('webhook_url')

banner = r'''
   ▄▄▄·  ▐ ▄ ▄▄▄▄▄▪  ▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄  
  ▐█ ▀█ •█▌▐█•██  ██ ██•  ▪     ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █·
  ▄█▀▀█ ▐█▐▐▌ ▐█.▪▐█·██▪   ▄█▀▄ ▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄ 
  ▐█ ▪▐▌██▐█▌ ▐█▌·▐█▌▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
   ▀  ▀ ▀▀ █▪ ▀▀▀ ▀▀▀.▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀
  ANTILOGGER by byte#6110'''

def anti_logger():
    print(banner)
    headers = {'authorization': token, 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTUxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    request = requests.get('https://discord.com/api/v9/auth/sessions', headers=headers)

    response = json.loads(request.text)
    user_sessions = response.get('user_sessions')

    authorized_sessions = []
    for x in user_sessions:
        session = x.get('id_hash')
        authorized_sessions.append(session)

    session_count = len(authorized_sessions)
    print(f'┃  {session_count} authorized sessions')
    print(f'┃  Starting anti logger')

    while True:
        request_2 = requests.get('https://discord.com/api/v9/auth/sessions', headers=headers)
        response = json.loads(request_2.text)
        user_sessions = response.get('user_sessions')
        
        for x in user_sessions:
            session = x.get('id_hash')
            if session not in authorized_sessions:
                print(f'┃  {Fore.RED}[ALERT] {Fore.RESET}Unknown user has logged into your account')
                if password_changing:
                    change_url = f'https://discord.com/api/v9/users/@me'
                    payload = {'password': password,'new_password': another_password}
                    change_password = requests.patch(change_url,headers={'authorization': token}, json=payload)
                    print(f'┃  {Fore.RED}[ALERT] {Fore.RESET}Password has been changed to {another_password}')
                    
                    with open('logs.txt', 'a') as logfile:
                        logfile.write(f'PASSWORD CHANGED FROM {password} TO {another_password} AT {datetime.now()}\n')

                    request_3 = requests.post('https://discord.com/api/v9/auth/login', headers={'email': email, 'password': another_password})
                    response = json.loads(request_3.text)
                    new_token = response.get('token')

                if webhook_logging and password_changing:
                    payload = {"embeds": [{"color": '16711680', "fields": [{"name": "Password Changed To", "value": another_password}][{"name": "Token Changed To", "value": new_token}], "footer": {"text": datetime.now()}}],"username": "antilogger notifications", "avatar_url": "https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg"}
                    requests.post(webhook_url, json=payload)

                if webhook_logging and not password_changing:
                    payload = {"embeds": [{"color": 16711680,"fields": [{"name": "ALERT", "value": f"Unknown user logged into your account at {datetime.now()}"}],"footer": {"text": "sent from antilogger"}}], "username": "antilogger notifications", "avatar_url": "https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg"}
                    requests.post(webhook_url, json=payload)


        temp_delay = delay
        for x in range(delay):
            ctypes.windll.kernel32.SetConsoleTitleW(f'antilogger | {temp_delay}')
            time.sleep(1)
            temp_delay -=1


anti_logger()