from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import hashlib
import hmac
import base64
import requests
import mimetypes
import random
import os

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')
if not os.path.exists('./decoded'):
    os.makedirs('./decoded')

# Payload pdf exemplo
# {
#   mediaKey: 'JPLCs6KLpe/exkEbhenNSeSR79f5sSowMhE0MqNdpKQ=',
#   url: 'https://mmg.whatsapp.net/d/f/AuWmR-lCzpyFPgjXwtTswQoTV0fsf886MccGt0arr6sg.enc',
#   messageType: 'documentMessage',
#   mimetype: 'application/pdf',
#   title: '1820_I1HFmGZ.pdf'
# }

mediaKey = 'JPLCs6KLpe/exkEbhenNSeSR79f5sSowMhE0MqNdpKQ='
url = 'https://mmg.whatsapp.net/d/f/AuWmR-lCzpyFPgjXwtTswQoTV0fsf886MccGt0arr6sg.enc'
file_name = 'videotest'
mimetype = 'application/pdf'
# title = None
title = '1820_I1HFmGZ.pdf'

if not title:
    file_name = random.getrandbits(128)
    file_extension = mimetypes.guess_extension(mimetype)
    title = '{}{}'.format(file_name, file_extension)
    
# Download .enc inside /tmp folder
r = requests.get(url, allow_redirects=True)
open('tmp/{}.enc'.format(file_name), 'wb').write(r.content)


def HKDF(key, length, appInfo=b""):
    key = hmac.new(b"\0"*32, key, hashlib.sha256).digest()
    keyStream = b""
    keyBlock = b""
    blockIndex = 1
    while len(keyStream) < length:
        keyBlock = hmac.new(key, msg=keyBlock+appInfo+(chr(blockIndex).encode("utf-8")), digestmod=hashlib.sha256).digest()
        blockIndex += 1
        keyStream += keyBlock
    return keyStream[:length]

def AESUnpad(s):
    return s[:-ord(s[len(s)-1:])];

def AESDecrypt(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv);
    plaintext = cipher.decrypt(ciphertext);
    return AESUnpad(plaintext);

mediaKeyExpanded=HKDF(base64.b64decode(mediaKey),112,b"WhatsApp Image Keys")
macKey=mediaKeyExpanded[48:80]
mediaData=open('tmp/{}.enc'.format(file_name), "rb").read()

file= mediaData[:-10]
mac= mediaData[-10:]

imgdata=AESDecrypt(mediaKeyExpanded[16:48],file, mediaKeyExpanded[:16])

with open('decoded/{}'.format(title), 'wb') as f:
    f.write(imgdata)

print("Decrypted image (hopefully)")
