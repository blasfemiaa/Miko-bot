from discord import Intents, Member, Message
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import asyncio
import discord
from PIL import Image, ImageFilter
import pytesseract
import io
load_dotenv()
token = os.getenv("discord.token")

intents = Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

usuarios_eliminados = []
balas = 6
tambor = [False] * 6
tambor[random.randint(0, 5)] = True
juego_curso = False
jugadores = []
turno_actual = 0
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\User\Documents\tesseract\tesseract.exe"


@bot.command()
async def ruletarusa(ctx):
    global juego_curso, usuarios_eliminados, jugadores, balas, turno_actual

    if juego_curso:
        await ctx.send("Ya hay un juego en curso.")
        return

    role_name = "ruletita"
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    jugadores = [member for member in ctx.guild.members if role in member.roles and not member.bot]
    
    


    usuarios_eliminados = []
    juego_curso = True
    balas = 10
    turno_actual = 0
    await ctx.send("¡Preparen el orto!")
    
    await empezar_juego(ctx)


async def empezar_juego(ctx):
    global juego_curso, turno_actual

    while juego_curso:
        if len(jugadores) <= 1:
            await ctx.send("¡Fin del juego! No quedan suficientes jugadores.")
            juego_curso = False
            break

        jugador_actual = jugadores[turno_actual]
        await ctx.send(f"{jugador_actual.mention}, es tu turno. Escribe `!disparar` para intentar disparar.")
        await asyncio.sleep(10000)

@bot.command()
async def disparar(ctx):
    global juego_curso, turno_actual, balas, jugadores

    if not juego_curso:
        await ctx.send("No hay juego en curso.")
        return

    if ctx.author != jugadores[turno_actual]:
        await ctx.send("No es tu turno.")
        return

    balas -= 1

    if tambor[random.randint(0, 5)]:
        await ctx.send(f"{ctx.author.mention} ¡Caducaste!")
        usuarios_eliminados.append(ctx.author)
        jugadores.remove(ctx.author)
        await ctx.channel.set_permissions(ctx.author, send_messages=False)
        
    
    else:
        await ctx.send(f"{ctx.author.mention} ¡Carajo, te faltan los dedos!")

    turno_actual = (turno_actual + 1) % len(jugadores)

    if len(jugadores) <= 1:
        await ctx.send(f"¡Fin del juego! El ganador es {jugadores[0].mention}.")
        juego_curso = False
        return

    await empezar_juego(ctx)


@bot.command()
async def detener(ctx):
    global juego_curso
    if juego_curso:
        juego_curso = False
        await ctx.send("Se terminó el juego.")
    else:
        await ctx.send("No hay juego en curso.")
        
@bot.command()
async def textoimg(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]

        image_data = await attachment.read()
        image = Image.open(io.BytesIO(image_data))
        
        image = image.convert('L')  
        image = image.filter(ImageFilter.SHARPEN) 
        
        
        text = pytesseract.image_to_string(image)
        if text.strip():
            await ctx.send(f'**Texto extraído:**\n{text}')
        else:
            await ctx.send("No se encontró texto en la imagen.")
    else:
        await ctx.send("No hay texto para extraer.")
        


@bot.event
async def on_ready():
    print("Bot prendido")

@bot.event
async def on_message( message: Message):
    if message.author == bot.user:
        return

    user_message = message.content.lower()

    if "peron" in user_message:
        await message.channel.send("PERON PERON, QUE GRANDE SOS")
    elif "neko neko" in user_message:
        await message.channel.send("Neko neko nyaa")
    elif "neko" in user_message:
        await message.channel.send("Neko neko nyaa")
    elif "nekoneko" in user_message:
        await message.channel.send("Neko neko nyaa")
    elif "quien es dios?" in user_message:
        await message.channel.send("yo soy dios, dios es peron, peron es el creador de todas las cosas en este mundo, peron, te dio la vida.")
    elif "dios" in user_message:
        await message.channel.send("PERON ES DIOS, PELOTUDO QUE NO ENTENDES ENFERMITO MENTAL GORDO DEPOSITO DE SEMEN MALNACIDO RETRASADO TETON SIN ESCRUPULOS ACEITOSO REBOSADO")
    

    await bot.process_commands(message)

def main():
    bot.run(token)

if __name__ == '__main__':
    main()





