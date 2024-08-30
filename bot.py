import json
from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes, Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters

# Función para cargar la configuración desde el archivo JSON
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

# Cargar la configuración
config = load_config()
TOKEN = config["token"]
CORRECT_PASSWORD = config["password"]
SUCCESS_MESSAGE = config["success_message"]
ANOTHER_MESSAGE = config["another_message"]

# Crear una función que maneje el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Utilizamos await para esperar la ejecución de la coroutine reply_text
    await update.message.reply_text('¡Bienvenido hacker! Por favor, introduce nuestro lema para continuar.')

# Crear una función para manejar los mensajes del usuario
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text

    if user_input == CORRECT_PASSWORD:
        # Utilizamos await para esperar la ejecución de la coroutine reply_text
        await update.message.reply_text(SUCCESS_MESSAGE)
        await update.message.reply_text(ANOTHER_MESSAGE)
    else:
        # Utilizamos await para esperar la ejecución de la coroutine reply_text
        await update.message.reply_text('Lema incorrecta.')

def main() -> None:

    # Crear la aplicación
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar manejadores para comandos y mensajes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar el bot
    application.run_polling()


if __name__ == '__main__':
    main()
