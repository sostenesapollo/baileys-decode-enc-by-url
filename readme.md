#### Using .enc urls with to decode with mediaKey 
- [x] Download ```.enc``` files
- [x] Write file into ```./tmp directory``` and generate a random name if doesn't have it 
- [x] Convert downloaded ```.enc``` into a real file and store into ```./decoded```

### Audio payload

payload_audio = {
  'url': 'https://mmg.whatsapp.net/d/f/AhJJD1xpcJw9Pw7NGmuqVbvpn5GaG8qJOitF0PbcyqXy.enc',
  'mediaKey': 'fNKalX3uVGmOf/CdbsI8TIdxCDoXeD2V6uhu8yrPUIg=',
  'messageType': 'audioMessage',
  'whatsappTypeMessageToDecode': 'WhatsApp Audio Keys',
  'mimetype': 'audio/ogg; codecs=opus'
}

### Image payload

payload_image = {
  'url': 'https://mmg.whatsapp.net/d/f/AgfjfrORL0TfvrWe5jbf1xXESmnPGezNn0QmSf-7We_p.enc',
  'mediaKey': 'Lh6YXfZxhuhJo2/FdPuQrEARg6BiZ+zHkybfXNg3dYA=',
  'messageType': 'imageMessage',
  'whatsappTypeMessageToDecode': 'WhatsApp Image Keys',
  'mimetype': 'image/jpeg'
}

### PDF payload

payload_pdf = {
  'url': 'https://mmg.whatsapp.net/d/f/AuWmR-lCzpyFPgjXwtTswQoTV0fsf886MccGt0arr6sg.enc',
  'mediaKey': 'JPLCs6KLpe/exkEbhenNSeSR79f5sSowMhE0MqNdpKQ=',
  'messageType': 'documentMessage',
  'whatsappTypeMessageToDecode': 'WhatsApp Document Keys',
  'mimetype': 'application/pdf',
  'title': '1820_I1HFmGZ.pdf'
}

### Video payload

payload_video = {
  'url': 'https://mmg.whatsapp.net/d/f/Ag5bLACAJ-yo5mwQc8BuxBrr_yElaLh9x4V60NTf3NrO.enc',
  'mediaKey': 'uYsctaBPFmJYe+EtSkM/SW1D7NXWhwOAOM7NWbxMJvs=',
  'messageType': 'videoMessage',
  'whatsappTypeMessageToDecode': 'WhatsApp Video Keys',
  'mimetype': 'video/mp4'
}
