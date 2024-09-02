import discord
import time
import os
from discord.ext import commands
import discord.voice_client


# intents, bot 설정

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

#아래에 필요한 변수를 지정 할 수 있어요.




#아래에 필요한 함수를 지정 할 수 있어요




#여기부터는 봇의 구동 코드를 작성합니다. 
@bot.event
async def on_ready(): 
    #봇이 시작되었을 때 어떻게 할 것인가요?
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("Syncing commands. . .")
    #아래는 슬래쉬 명령어를 업데이트 해줍니다. 
    try : 
        await bot.sync_commands()
        print("Commands synced")
        
    except Exception as E :
        print("Failed \n Error : {}".format(E))


"""
예시 1 - 명령어 구동 (기본)

@bot.slash_command(name="A명령어" , discrpiption = "이 명령어의 설명")
async def A명령어(ctx : discord.ApplicationContext): 
    await ctx.respond(f"A명령어가 실행되었어요.")

예시 2 - string 값 받아오기

@bot.slash_command(name="B명령어" , discrpiption = "이 명령어의 설명")
async def B명령어(ctx : discord.ApplicationContext,content : str):  
    await ctx.respond(f"{content} 라는 정보를 받았습니다. ")
    

"""


# 간단한 인사 명령어
@bot.slash_command(name = "greeting" , discription = "Hello to Bot!")
async def greeting(ctx : discord.ApplicationContext) :
    ctx.respond(f"{ctx.user}님 안녕하세요? " )
    


bot.run(os.environ.get("YOUR_API_KEY"))
# 또는
#bot.run("토큰")