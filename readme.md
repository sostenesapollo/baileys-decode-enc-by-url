#### Using .enc urls with to decode with mediaKey 
- [x] Download ```.enc``` files
- [x] Write file into ```./tmp directory``` and generate a random name if doesn't have it 
- [x] Convert downloaded ```.enc``` into a real file and store into ```./decoded```

### Audio payload

```
    {
    url: 'https://mmg.whatsapp.net/d/f/AhJJD1xpcJw9Pw7NGmuqVbvpn5GaG8qJOitF0PbcyqXy.enc',
    mediaKey: 'fNKalX3uVGmOf/CdbsI8TIdxCDoXeD2V6uhu8yrPUIg=',
    messageType: 'audioMessage',
    whatsappTypeMessageToDecode: 'WhatsApp Audio Keys',
    mimetype: 'audio/ogg; codecs=opus',
    title: undefined
    }
```