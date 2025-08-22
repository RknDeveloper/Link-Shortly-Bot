# (©) @RknDeveloper ❣️

import re, os
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Rkn-Developer")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Hᴇʟʟᴏ {}, 👋

I ᴀᴍ ᴀɴ Aᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ Pᴏᴡᴇʀғᴜʟ Lɪɴᴋ Sʜᴏʀᴛᴇɴᴇʀ Bᴏᴛ. 🔗  

Uꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ:  
✅ Sʜᴏʀᴛᴇɴ ʏᴏᴜʀ ʟᴏɴɢ ʟɪɴᴋꜱ ɪɴ ꜱᴇᴄᴏɴᴅꜱ  
✅ Sᴜᴘᴘᴏʀᴛꜱ Mᴜʟᴛɪᴘʟᴇ Uʀʟ ꜱɪᴛᴇꜱ  
✅ Aᴅᴅ Yᴏᴜʀ Oᴡɴ Aᴘɪ & Sɪᴛᴇ  

🔑 Jᴜꜱᴛ ꜱᴇᴛ ʏᴏᴜʀ Aᴘɪ ᴋᴇʏ & Sɪᴛᴇ ᴏɴᴄᴇ, ᴀɴᴅ ꜱᴇɴᴅ ᴀɴʏ ʟɪɴᴋ (http/https).  
I ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ᴀ ꜱʜᴏʀᴛ ʟɪɴᴋ.  

👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ: @Rkn_Bots_Updates</b>"""
    
    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/Rkn_Bots_Updates>𝐑𝐊𝐍 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://github.com/RknDeveloper>Rᴋɴ Dᴇᴠᴇʟᴏᴘᴇʀ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://github.com/RknDeveloper/link-shortly-bot>link shortly bot</a></b>     
╰───────────────⍟ """
   
    # ⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/RknDeveloper/link-shortly-bot>link shortly bot</a>
• ❣️ <a href=https://github.com/RknDeveloper>OWNER</a>
• ❣️ <a href=https://t.me/Rkn_Bots_Updates>Rᴋɴ Dᴇᴠᴇʟᴏᴘᴇʀ</a> """
