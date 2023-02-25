const Discord = require('discord.js');
const ytdl = require('ytdl-core');

const dispatcher = serverQueue.connection.play(ytdl(serverQueue[0].url, { filter: 'audioonly' }))
const client = new Discord.Client();
const prefix = '!';
const queue = new Map();

client.once('ready', () => {
  console.log('Bot online!');
});

client.on('message', async message => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'play') {
    execute(message, queue);
    return;
  } else if (command === 'skip') {
    skip(message, queue);
    return;
  } else if (command === 'stop') {
    stop(message, queue);
    return;
  } else if (command === 'reminder') {
    let time = args[0];
    let reminder = args.slice(1).join(' ');

    message.reply(`Lembrete criado para ${time} minutos a partir de agora: ${reminder}`);

    setTimeout(() => {
      message.reply(`Lembrete: ${reminder}`);
    }, time * 60 * 1000);
  } else {
    message.reply('Comando inválido.');
  }
});

async function execute(message, queue) {
  const args = message.content.split(' ');
  const voiceChannel = message.member.voice.channel;

  if (!voiceChannel) {
    return message.reply('Você precisa estar em um canal de voz para reproduzir música!');
  }

  const permissions = voiceChannel.permissionsFor(message.client.user);

  if (!permissions.has('CONNECT') || !permissions.has('SPEAK')) {
    return message.reply('Eu preciso das permissões para entrar e falar no seu canal de voz!');
  }

  const songInfo = await ytdl.getInfo(args[1]);
  const song = {
    title: songInfo.videoDetails.title,
    url: songInfo.videoDetails.video_url
  };

  if (!queue.get(message.guild.id)) {
    queue.set(message.guild.id, []);
  }

  queue.get(message.guild.id).push(song);

  if (queue.get(message.guild.id).length === 1) {
    play(message, queue);
  } else {
    message.channel.send(`${song.title} adicionado à fila!`);
  }
}

async function play(message, queue) {
  const serverQueue = queue.get(message.guild.id);

  if (!serverQueue) {
    return;
  }

}
