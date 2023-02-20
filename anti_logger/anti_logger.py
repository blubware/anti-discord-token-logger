import requests, json, time, ctypes, os
from datetime import datetime
from colorama import Fore

def clear():
    kernel = os.name
    match kernel:
        case 'nt':
            os.system('cls')

        case _:
            os.system('clear')

with open('config.json') as config:
    config = json.load(config)

    token = config.get('token')
    delay = config.get('delay')

    password_changing = config.get('password_changing')
    password = config.get('password')
    another_password = config.get('another_password')
    email = config.get('email')

    webhook_logging = config.get('webhook_logging')
    webhook_url = config.get('webhook_url')
    
    panic = config.get('panic')

banner = fr'''
   ▄▄▄·  ▐ ▄ ▄▄▄▄▄▪  ▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄    
  ▐█ ▀█ •█▌▐█•██  ██ ██•  ▪     ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █· 
  ▄█▀▀█ ▐█▐▐▌ ▐█.▪▐█·██▪   ▄█▀▄ ▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄    
  ▐█ ▪▐▌██▐█▌ ▐█▌·▐█▌▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
   ▀  ▀ ▀▀ █▪ ▀▀▀ ▀▀▀.▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀
  ANTILOGGER by byte#6110
  1 > Antilogger
  2 > Check for possible token loggers
  3 > Change password's indefinitely'''

def antilogger():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW('antilogger')
    print(banner)
    script = input('  Script > ')
    match script:
        case '1':
            anti_logger()

        case '2':
            check_folders()

        case '3':
            change_passwords()

        case _:
            print(f'\'{script}\' is not a valid script, press enter to try again > ')

def anti_logger():
    ctypes.windll.kernel32.SetConsoleTitleW(f'antilogger')
    headers = {'authorization': token, 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTUxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    request = requests.get('https://discord.com/api/v9/auth/sessions', headers=headers)

    response = json.loads(request.text)

    authorized_sessions = []
    for x in response['user_sessions']:
        session = x['id_hash']
        authorized_sessions.append(session)

    session_count = len(authorized_sessions)
    print(f'  {session_count} authorized sessions')
    print(f'  Starting anti logger')

    while True:
        request_2 = requests.get('https://discord.com/api/v9/auth/sessions', headers=headers)
        response = json.loads(request_2.text)

        for x in response['user_sessions']:
            session = x['id_hash']
            approx_last_used_time = x['approx_last_used_time']
            os = x['client_info']['os']
            platform = x['client_info']['platform']
            location = x['client_info']['location']

            if session not in authorized_sessions:
                print(f'  {Fore.RED}[ALERT] {Fore.RESET}Unknown user has logged into your account')
                
                if panic:
                    requests.post('https://discord.com/api/v9/users/@me/delete', json={'password': password, 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NTUxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='})
                    
                    if webhook_logging:
                        payload = {"embeds":
                        [{"color":16711680,
                        "fields":[{"name":"Password Changed To", "value":another_password},
                        {"name":"Token Changed To", "value": new_token}],
                        
                        "footer":{"text": datetime.now()}}],
                        
                        "username":"antilogger notifications", 
                        "avatar_url":"https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg"}
                        requests.post(webhook_url, json=payload)
                    
                    with open('logs.txt', 'a') as logfile:
                        logfile.write(f'ACCOUNT DISABLED AT {datetime.now()}\n')

                
                
                if password_changing:
                    change_url = f'https://discord.com/api/v9/users/@me'
                    payload = {'password': password,'new_password': another_password}
                    change_password = requests.patch(change_url,headers={'authorization': token}, json=payload)
                    print(f'  {Fore.RED}[ALERT] {Fore.RESET}Password has been changed to {another_password}')

                    request_3 = requests.post('https://discord.com/api/v9/auth/login', headers={'email': email, 'password': another_password})
                    response = json.loads(request_3.text)
                    new_token = response.get('token')

                    if webhook_logging:
                        payload = {"embeds":
                        [{"color":16711680,
                        "fields":[{"name":"Password Changed To", "value": another_password},
                        {"name":"Token Changed To", "value": new_token}],

                        "footer":{"text": datetime.now()}}],
                        
                        "username":"antilogger notifications",
                        "avatar_url":"https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg"}
                        requests.post(webhook_url, json=payload)

                    with open('logs.txt', 'a') as logfile:
                        logfile.write(f'PASSWORD CHANGED FROM {password} TO {another_password} AT {datetime.now()}\n')

                                
                if webhook_logging:
                    requests.post(webhook_url, json={"embeds":[{"color":16711680,"fields":[{"name":"ALERT", "value":f"Unknown user logged into your account at {datetime.now()}"}],"footer":{"text":"sent from antilogger"}}],"username":"antilogger notifications","avatar_url":"https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg"})

                    requests.post(webhook_url, json={"content": '',"embeds": [{"title": "Attacker Information","color": 16711680,"fields": [{"name": "Operatiing System", "value": os},{"name": "Location", "value": location},{"name": "Platform", "value": platform},{"name": "Last Used", "value": approx_last_used_time}]}],"username": "antilogger notifications","avatar_url": "https://i.pinimg.com/564x/9d/0a/f1/9d0af17f210624e75c0a57d4f6ae9427.jpg","attachments": []})
                print(f'''  {Fore.RED}[ALERT]{Fore.RESET} ATTACKER INFORMATION
  {Fore.CYAN}OS{Fore.RESET} > {os}
  {Fore.CYAN}Location{Fore.RESET} > {location}
  {Fore.CYAN}Platform{Fore.RESET} > {platform}
  {Fore.CYAN}Last Used{Fore.RESET} > {approx_last_used_time}
  ''')

                with open('logs.txt', 'a') as logfile:
                    logfile.write(f'UNAUTHROIZED USER LOGGED IN AT {datetime.now()}\n')


        temp_delay = delay
        for x in range(delay):
            ctypes.windll.kernel32.SetConsoleTitleW(f'antilogger | {temp_delay}')
            time.sleep(1)
            temp_delay -=1

def check_folders():
    appdata_path = os.getenv('appdata')

    appdata_paths = {
        'Discord': f'{appdata_path}\\discord\\Local Storage\\leveldb',
        'Discord PTB': f'{appdata_path}\\discordptb\\Local Storage\\leveldb',
        'Discord Canary': f'{appdata_path}\\discordcanary\\Local Storage\\leveldb'}

    for i in appdata_paths:

        if os.path.exists(appdata_paths[i]):
            access_time = os.path.getatime(appdata_paths[i])
            access_time_str = time.ctime(access_time)

            print(f'  Your {i} storage folder was last accessed at {access_time_str}')

        else:
            continue

    input('  All done, press enter to return to main menu > ')
    antilogger()

def change_passwords():
    payload = { 'login': email, 'password': password}
    url = f'https://discord.com/api/v9/auth/login'

    with open('output/password.txt','a') as password_file:
        password_file.write(f'\n{email} : {password}')
    
    request_1 = requests.post(url,json=payload)

    response = request_1.text
    response_json = json.loads(response)
    token = response_json.get('token')

    print(f'  Using token > {token}...')
    print(f'  Using password > {another_password}')

    change_url = f'https://discord.com/api/v9/users/@me'
    payload = {'password': password,'new_password': another_password}
    request_2 = requests.patch(change_url,headers={'authorization': token}, json=payload)

    ########################################################################################

    payload = { 'login': email, 'password': another_password}
    url = f'https://discord.com/api/v9/auth/login'

    with open('output/password.txt','a') as password_file:
        password_file.write(f'\n{email} : {password}')
        print(f'  Wrote > {email} : {password}')
    
    request_3 = requests.post(url,json=payload)

    response = request_3.text
    response_json = json.loads(response)
    token = response_json.get('token')

    print(f'  Using token > {token}...')
    print(f'  Using password > {password}')

    change_url = f'https://discord.com/api/v9/users/@me'
    payload = {'password': another_password,'new_password': password}

    print(f'  Sleeping for {delay} seconds')
    
    time.sleep(int(delay))

antilogger()