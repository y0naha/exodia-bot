import os
import discord
import datetime
import pytz
from discord.ext import commands
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv

load_dotenv()

# Configuração
TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
TIMEZONE = os.getenv('TIMEZONE')

# Criação do bot
bot = commands.Bot(command_prefix='!')
voice_client = None
queue = []
credentials = None
service = None
reminder_tasks = {}

# Conexão com o YouTube


def youtube_search(query):
    global credentials
    global service

    if credentials is None:
        credentials = Credentials.from_authorized_user_file(
            'token.json', ['https://www.googleapis.com/auth/youtube.force-ssl'])
    if service is None:
        service = build('youtube', 'v3', credentials=credentials)

    request = service.search().list(
        part='snippet',
        type='video',
        q=query,
        maxResults=1,
    )
    response = request.execute()
    if len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    else:
        return None

# Comandos de música


@bot.command()
async def play(ctx, *, search):
    global voice_client
    if voice_client is None:
        voice_client = await ctx.author.voice.channel.connect()
    else:
        await voice_client.move_to(ctx.author.voice.channel)

    url = youtube_search(search)
    if url is not None:
        queue.append(url)
        if len(queue) == 1:
            voice_client.play(discord.FFmpegPCMAudio(
                queue[0], executable='ffmpeg'), after=lambda e: on_finished(ctx, e))
            await ctx.send(f'Now playing: {search}')
        else:
            await ctx.send(f'Added to queue: {search}')
    else:
        await ctx.send('Could not find the video')


def on_finished(ctx, error):
    global queue
    if error is not None:
        print(f'Error: {error}')
    if len(queue) > 0:
        queue.pop(0)
        if len(queue) > 0:
            voice_client.play(discord.FFmpegPCMAudio(
                queue[0], executable='ffmpeg'), after=lambda e: on_finished(ctx, e))
        else:
            voice_client.stop()
            voice_client.disconnect()
            voice_client = None
            # await ctx.send('End of queue')


@bot.command()
async def pause(ctx):
    global voice_client
    if voice_client is not None and voice_client.is_playing():
        voice_client.pause()


@bot.command()
async def resume(ctx):
    global voice_client
    if voice_client is not None and voice_client.is_paused():
        voice_client.resume()


@bot.command()
async def skip(ctx):
    global queue
    if len(queue) > 0:
        queue.pop(0)
        if len(queue) > 0:
            voice_client.play(discord.FFmpegPCMAudio(
                queue[0], executable='ffmpeg'), after=lambda e: on_finished(ctx, e))
            await ctx.send('Skipping to the next song')
        else:
            voice_client.stop()
            voice_client.disconnect()
            voice_client = None
            await ctx.send('End of queue')
    else:
      await ctx.send('The queue is already empty')

# comandos dos lembretes


@bot.command()
async def reminder(ctx, time, *, message):
    global reminder_tasks
    try:
        # Parse o tempo e converte para o fuso horário local
      tz = pytz.timezone(TIMEZONE)
      reminder_time = datetime.datetime.strptime(
          time, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(tz)
    # Cria um link de lembrete com a mensagem
      link = f'https://www.google.com/calendar/render?action=TEMPLATE&text={message}&dates={time}'

    # Agendamento da mensagem de lembrete
      task = bot.loop.call_later((reminder_time - datetime.datetime.now(tz)
                                ).total_seconds(), send_reminder, ctx, message, link)
      reminder_tasks[message] = task

      await ctx.send(f'Reminder set for {time} with message "{message}"')
    except Exception as e:
      print(e)
    await ctx.send('Invalid date format. Please use the format YYYY-MM-DD HH:MM:SS')


def send_reminder(ctx, message, link):
  global reminder_tasks
del reminder_tasks[message]
embed = discord.Embed(title='Reminder', description=message, url=link)
ctx.send(embed=embed)


@bot.command()
async def cancelreminder(ctx, *, message):
    global reminder_tasks
    if message in reminder_tasks:
      task = reminder_tasks[message]
      task.cancel()
      del reminder_tasks[message]
      await ctx.send(f'Reminder for "{message}" has been cancelled')
    else:
      await ctx.send(f'No reminder found for "{message}"')
