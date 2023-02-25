# Como usar o bot
## Adicionando o bot ao seu servidor Discord
Para adicionar o bot ao seu servidor do Discord, você deve ter privilégios de administrador no servidor. Em seguida, siga os seguintes passos:

1.Acesse o link de convite do bot: [coloque aqui o link do convite do bot].<br>
2.Selecione o servidor que você deseja adicionar o bot e clique em "Autorizar".<br>
3.O bot agora estará disponível em seu servidor do Discord.<br>

# Comandos disponíveis
O bot tem os seguintes comandos disponíveis:

<b>!lembrar</b>
<br>
Este comando permite que os usuários adicionem lembretes para serem notificados pelo bot em um horário especificado. Os usuários devem digitar "!lembrar" seguido de uma mensagem com o texto do lembrete e o horário em que desejam ser notificados. O formato do horário deve ser "DD/MM/YYYY HH:MM".

Exemplo de uso:

```console
!lembrar Lembrete importante às 10:30
```

<b>!tocar</b>
<br>
Este comando permite que os usuários toquem músicas do YouTube no canal de voz atual do servidor. Os usuários devem digitar "!tocar" seguido do URL da música no YouTube. 


Exemplo de uso:

```javascript
!tocar https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
</b>!parar</b>
<br>
Este comando permite que os usuários parem de tocar música no canal de voz atual do servidor.

Exemplo de uso:

```console
!parar
```

<b>!ajuda</b>
<br>
Este comando lista todos os comandos disponíveis no bot.

Exemplo de uso:

```console
!ajuda
```

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

## Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE.md para obter detalhes.