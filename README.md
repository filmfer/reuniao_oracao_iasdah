# reuniao_oracao_iasdah

Este código Python serve para enviar automaticamente um anúncio 📢 de uma reunião de oração 🕊️ para um grupo no Telegram, incluindo uma imagem 🖼️ e uma mensagem de texto formatada em Markdown. A seguir explico o funcionamento, configuração e as variáveis usadas:

O que faz o código
Envia uma imagem para um chat de grupo do Telegram.

Envia uma mensagem de convite com link do Zoom logo depois da imagem.

Utiliza o serviço oficial da API do Telegram para bots 🤖.

Como configurar
Defina as variáveis de ambiente TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID.

O token é gerado ao criar um bot pelo BotFather no Telegram 🔑.

O chat ID normalmente é negativo, como por exemplo: -100123456789 (para grupos privados).

Certifique-se de que o ficheiro de imagem (IMAGE_FILE_PATH) exista no local correto 🗂️.

É possível alterar o texto da mensagem conforme o evento ou grupo 📝.

Execute o script no terminal após definir as variáveis (por exemplo, usando o comando export TELEGRAM_BOT_TOKEN=SEU_TOKEN; export TELEGRAM_CHAT_ID=SEU_CHAT_ID; python nome_do_arquivo.py).

Variáveis principais
TELEGRAM_BOT_TOKEN: Token do Bot (proteger e nunca partilhar 🌐).

TELEGRAM_CHAT_ID: ID do grupo onde a mensagem será enviada 💬.

IMAGE_FILE_PATH: Caminho para o ficheiro da imagem 📷.

MESSAGE_TEXT: Texto da mensagem, pode usar Markdown para formatar 🌟.

Emojis usados para resumir funções
🤖 Automatiza envio pelo Telegram

🖼️ Envia imagens junto do anúncio

📝 Mensagens personalizáveis

🔑 Requer configuração com variáveis de ambiente

🎯 Destina-se a grupos específicos (Chat ID)

Com este script, é fácil promover eventos ou reuniões automaticamente usando o bot do Telegram, muito útil para comunidades, igrejas, ou grupos diversos!
