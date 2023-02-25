# Exodia Bot
Este bot permite ouvir música através do YouTube e criar lembretes diários que geram um link com informações adicionais.
# Como usar o bot Exodia
## Adicionando o bot ao seu servidor Discord
Para adicionar o bot ao seu servidor do Discord, você deve ter privilégios de administrador no servidor. Em seguida, siga os seguintes passos:

1. Acesse o link de convite do bot: [coloque aqui o link do convite do bot].<br>
2. Selecione o servidor que você deseja adicionar o bot e clique em "Autorizar".<br>
3. O bot agora estará disponível em seu servidor do Discord.<br>

## Comandos disponíveis
# Comandos de música
`!play [search]`: busca um vídeo no YouTube e começa a reproduzir a música no canal de voz do usuário. Se já houver uma música sendo reproduzida, adiciona à fila.
`!pause`: pausa a música que está sendo reproduzida.
`!resume`: retoma a reprodução da música que foi pausada.
`!skip`: pula para a próxima música da fila, se houver.

# Comandos de lembrete
`!reminder [message] [time]`: cria um lembrete diário com a mensagem especificada e um link para obter informações adicionais. O tempo deve ser especificado em formato HH:MM, no fuso horário do servidor.
`!cancelreminder [id]`: remove o lembrete diário com o ID especificado.

## Configuração do bot
O bot usa uma chave de API do Google para acessar o YouTube Data API, que é necessário para tocar músicas do YouTube. Para configurar seu próprio bot, você deve seguir as seguintes etapas:

1. Crie um novo projeto no Console do Google Cloud e habilite o YouTube Data API v3.

2. Crie uma chave de API do Google e copie-a.

3. Crie um arquivo .env no diretório raiz do seu projeto e adicione a seguinte linha de código:

```makefile
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```
Substitua "YOUR_API_KEY_HERE" pela chave de API do Google que você copiou.

4. Certifique-se de instalar as dependências necessárias executando o comando npm install no diretório raiz do seu projeto.

5. Inicie o bot executando o comando node index.js no diretório raiz do seu projeto.

***

- Para executar o bot, você precisará criar um arquivo .env com as seguintes variáveis de ambiente:

* DISCORD_TOKEN: o token de autenticação do Discord para o seu bot.
* YOUTUBE_API_KEY: a chave de API do YouTube para buscar vídeos e informações.
* TIMEZONE: o fuso horário em que o bot deve operar (por exemplo, "America/Sao_Paulo").

## Execução

Após configurar as variáveis de ambiente, você pode executar o bot com o seguinte comando:

```
python index.py

```

Certifique-se de ter as bibliotecas `discord.py`, `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`, `pytz` e `python-dotenv` instaladas.
## Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE.md para obter detalhes.