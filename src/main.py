import logging
import subprocess
import json
import requests
from PIL import Image
import os

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    pass


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Work in progress")
    
async def send_first_page(context: ContextTypes.DEFAULT_TYPE):
    os.system("wget https://giornali.it/img/prime-pagine/la-verita_882e738e885a00054c77b56714c4cce2-big.webp")
    image = Image.open("la-verita_882e738e885a00054c77b56714c4cce2-big.webp").convert("RGB")
    os.system("rm la-verita_882e738e885a00054c77b56714c4cce2-big.webp")
    image.save("prova.jpg", "jpeg")
    with open("../conf.json") as json_file:
        data = json.load(json_file)
        group_id = data["group-id"]
        await context.bot.send_photo(chat_id=group_id, photo="prova.jpg")

def main() -> None:
    """Start the bot."""
    # Read the token from the conf.json file
    with open("../conf.json") as json_file:
        data = json.load(json_file)
        token = data["api-key"]
        group_id = data["group-id"]
        
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token=token).build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    job_queue = application.job_queue
    # Add a periodic function to check the GPU status
    periodic_task = job_queue.run_repeating(send_first_page, interval=10, first=0) 

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()