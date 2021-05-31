const { WAConnection, HKDFInfoKeys, MessageType  } = require('@adiwajshing/baileys')
const HKDF = require('futoin-hkdf')
const conn = new WAConnection()

conn.on ('open', () => {
    console.log (`credentials updated!`)
    require('fs').writeFileSync('./auth_info.json', JSON.stringify(conn.base64EncodedAuthInfo(), null, '\t'))
})


conn.loadAuthInfo ('./auth_info.json')    
conn.logger.level = 'silent'
conn.on('chat-update', chatUpdate => {

    if (chatUpdate.messages && chatUpdate.count) {

        const message = chatUpdate.messages.all()[0]
        const messageType = Object.keys(message.message)[0]

        if(
            messageType == MessageType.image || 
            messageType == MessageType.video || 
            messageType == MessageType.document || 
            messageType == MessageType.sticker
        ) {
            console.log('New media Message');

            const {mediaKey, url, mimetype, title} = message.message[messageType]
            console.log({ mediaKey: mediaKey.toString('base64'), url, messageType, mimetype, title });

        } else {
            console.log('message', messageType, 'no action related to files.');
        }

    }

})

function getMediaKeys(buffer, mediaType) {
    if (typeof buffer === 'string') {
        buffer = Buffer.from (buffer.replace('data:;base64,', ''), 'base64')
    }
    // expand using HKDF to 112 bytes, also pass in the relevant app info
    const expandedMediaKey = hkdf(buffer, 112, HKDFInfoKeys[mediaType])
    return {
        iv: expandedMediaKey.slice(0, 16),
        cipherKey: expandedMediaKey.slice(16, 48),
        macKey: expandedMediaKey.slice(48, 80),
    }
}

function hkdf(buffer, expandedLength, info = null) {
    return HKDF(buffer, expandedLength, { salt: Buffer.alloc(32), info: info, hash: 'SHA-256' })
}

conn.connect()