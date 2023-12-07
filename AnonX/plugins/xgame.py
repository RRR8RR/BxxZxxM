import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AnonX import app
import re
import sys

GAME_MESSAGE = "⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺\n\n★¦ مرحبا بك عزيزي:\n★¦في قسم العاب رنـثـون \n\n⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
        InlineKeyboardButton ('رنـثـون  رنـثـون ', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝⚡️', url =f"https://t.me/xLxLxLrr3")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
    

nmla = []

@app.on_message(command("رفع مطي"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n مطي ولد حباب 😂♥️")


@app.on_message(command("تنزيل مطي"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من المطايه 😂♥️")


@app.on_message(command("المرفوعين المطايه"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(command("رفع صرصر"))
async def rf3srsar(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصر 😂♥️")


@app.on_message(command("تنزيل صرصر"))
async def tnzelsrar(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصر 😂♥️")


@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه حد يرمي فلوس عليها 😂💃")


@app.on_message(command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")
  
  
@app.on_message(command("رفع منيوج"))
async def bjoiuyjk(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n منيوج واحد ينيج 😂♥️")


@app.on_message(command("تنزيل منيوج"))
async def kamal(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n منيوج اكواد تاب 😂♥️")
  
  
@app.on_message(command("رفع وصخ"))
async def fdsa(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n وصخ بنجاح  😂♥️")


@app.on_message(command("تنزيل وصخ"))
async def kophvc(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n الوصخ سبح 😂♥️")
  
  
@app.on_message(command("رفع عار"))
async def roky(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n عار عالمجتمع 😂♥️")


@app.on_message(command("تنزيل عار"))
async def zerso(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n عار خلاص 😂♥️")
  
  
@app.on_message(command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n صار بقر واحد يحلبه 🐄🤭")


@app.on_message(command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص خلص لبن 😂")
  
  
@app.on_message(command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n قرد حد يديلو موزه 😂🐒")


@app.on_message(command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n القرد صار انسان🙊🧍")
  
  
@app.on_message(command("رفع گلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص صارت قلبو 😂♥️")


@app.on_message(command("تنزيل گلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nمصارش قلبوو 😭💔")
  
  
@app.on_message(command("رفع خدام"))
async def qyui(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم ع البار    😂🤓")


@app.on_message(command("تنزيل خدام"))
async def klhj(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n الخدام ساب الشغل  😢🚶")
  
  
@app.on_message(command("رفع معرص"))
async def wqew(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n معرص البار  😂🤓")


@app.on_message(command("تنزيل معرص"))
async def ohho(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n المعرص صار راجل   😂🧔")
  
  
@app.on_message(command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  صارتي ارمله وجوزك مات 🥹")


@app.on_message(command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث متبقيش قموصه جوزك عايش اهو 😂🫶🏻")
  
  
@app.on_message(command("رفع مزه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n يمزه خدي بالك من نفسك 🥹❤️")


@app.on_message(command("تنزيل مزه"))
async def hhhhug(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n انتي صدقتي انك مزه ولا اي انا كنت بطبل 😂😝")
  
  
@app.on_message(command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  صارت ابنو وكل حياتو🥹🖤")


@app.on_message(command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حتي عيلتك مو طيقاك ورموك في الشارع ")
  
  
@app.on_message(command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي مهزأه ")


@app.on_message(command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n منو الغبي للي جان مفكر القمر دا ممكن يكون خاين 🥹🥹💕")  
  
  
@app.on_message(command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n صارتي بنتي وحته من گلبي 🥹❤️❤️❤️")


@app.on_message(command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر انا مخلفتش لسه🤡😂  ")  
  
  
@app.on_message(command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خنتها كام مره قول متتكسفش يخاين")


@app.on_message(command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n ايدا طلع سوء تفاهم انت اشرف من الشرف يسالك??❤️")
  
  
@app.on_message(command("رفع كواد"))
async def dadr(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n 😂 كواد طول عمرك مو اول مره")


@app.on_message(command("تنزيل كواد"))
async def hjj7gv(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  اهو كوادنزلتك 🙂💕")
  
  
@app.on_message(command("رفع حصان"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاص صار حصان رسمي نظمي😹")


@app.on_message(command("تنزيل حصان"))
async def cxxv(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث يعم كنا بنهزر معاك متصارش قفوش 😂😝")
  
  



@app.on_message(command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و وراح  غبي😹🤞")


@app.on_message(command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و بقي بيفهم😹🫶")
  
  
@app.on_message(command("رفع مرتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n مراتك خد و عملو واحد😹😽")


@app.on_message(command("تنزيل مرتي"))
async def xxxxt(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")  
  
  
@app.on_message(command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الجروب😹")


@app.on_message(command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")  
  
  
@app.on_message(command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")


@app.on_message(command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")  
  
  
@app.on_message(command("رفع جلبه"))
async def mmmuy(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n جلبه خدي عضمه😹🤞")


@app.on_message(command("تنزيل جلبه"))
async def dfrewq(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث جلبه تحولت الانسان😿😹")  
  
  
@app.on_message(command("رفع طيز"))
async def ssoss(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز و كبيره كمان😹🤞")


@app.on_message(command("تنزيل طيز"))
async def nobo(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز متزعلش نزلتك😹🫶")  
  
  
@app.on_message(command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"تم رفع العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي وهبلغ عنه😹🚓")


@app.on_message(command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"تم تنزيل العضوو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")
  

@app.on_message(
    command(["الالعاب","العاب"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4edb726cd168c2f4e1654.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺\n\nمرحبا بك في قسم العاب رنـثـون  3D\n\n⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "◁" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺\n\n★¦مرحبا بك في قسم العاب رنـثـون \n★¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\n⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('★¦العاب رنـثـون ', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝⚡️', url =f"https://t.me/xLxLxLrr3")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺\n\n★¦العاب رنـثـون 7\n★¦كت\n★¦تويت\n★¦اسال\n★¦اصراحه\n\n⩹━★⊷━⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝━⊶★━⩺." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝⚡️', url =f"https://t.me/xLxLxLrr3")
                      ],[
                         InlineKeyboardButton ('◁', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
