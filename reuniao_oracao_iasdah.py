import requests
import os

# --- CONFIGURAÇÕES ---
# O Token do seu Bot, obtido a partir das variáveis de ambiente
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# !!! IMPORTANTE: Substitua o valor abaixo pelo ID correto do seu grupo !!!
# O ID de um grupo privado é um número negativo, por exemplo: -100123456789
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# O caminho para a imagem que deseja enviar
IMAGE_FILE_PATH = "r_oracao_iasdah.jpg"

# A mensagem de texto que será enviada após a imagem
MESSAGE_TEXT = """*-----------------------------*
*|   Reunião de oração   |*
*-----------------------------*

*Hoje às 20h00*
_Por Zoom_

Boa tarde a todos.
Estão todos convidados para estarem presentes na reunião de oração de *hoje à noite às 20h00*.

*Acesso por Zoom:*
https://us02web.zoom.us/j/480270323
*ID da reunião:* 480 270 323
E também *por telefone:* +351 308 804 188"""


def send_telegram_photo(bot_token, chat_id, image_path):
    """Envia uma imagem para o chat especificado no Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    try:
        with open(image_path, 'rb') as photo_file:
            files = {'photo': photo_file}
            payload = {'chat_id': chat_id}
            response = requests.post(url, data=payload, files=files, timeout=20)
            response.raise_for_status()  # Verifica se houve erros no pedido
            print(f"Imagem enviada com sucesso para o chat ID: {chat_id}")
            return True
    except FileNotFoundError:
        print(f"ERRO: O ficheiro da imagem não foi encontrado em '{image_path}'")
        return False
    except requests.exceptions.RequestException as e:
        print(f"ERRO ao enviar a imagem: {e}")
        return False

def send_telegram_message(bot_token, chat_id, text):
    """Envia uma mensagem de texto para o chat especificado no Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'  # Usa o modo Markdown para formatar o texto
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status() # Verifica se houve erros no pedido
        print(f"Mensagem de texto enviada com sucesso para o chat ID: {chat_id}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"ERRO ao enviar a mensagem de texto: {e}")
        return False

if __name__ == "__main__":
    if not TELEGRAM_BOT_TOKEN:
        print("ERRO CRÍTICO: A variável de ambiente TELEGRAM_BOT_TOKEN não está definida.")
    elif TELEGRAM_CHAT_ID == "COLOQUE_O_ID_CORRETO_AQUI":
        print("ERRO CRÍTICO: Por favor, edite o script e insira o ID de chat correto na variável TELEGRAM_CHAT_ID.")
    else:
        print("--- A iniciar o envio do anúncio da Reunião de Oração ---")
        # 1. Enviar a imagem primeiro
        if send_telegram_photo(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, IMAGE_FILE_PATH):
            # 2. Se a imagem for enviada com sucesso, enviar a mensagem de texto
            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, MESSAGE_TEXT)
        
        print("--- Processo concluído ---")
