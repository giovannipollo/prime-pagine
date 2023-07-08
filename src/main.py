# import logging
# import subprocess
# import json
# import requests
# from PIL import Image
# import os
# import telegram
# import asyncio

# from telegram import ForceReply, Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # Define a few command handlers. These usually take the two arguments update and
# # context.
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     pass


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Work in progress")
    
# async def send_first_page(context: ContextTypes.DEFAULT_TYPE):
#     response = requests.get("https://giornali.it/quotidiani-nazionali/la-verita/prima-pagina/")
#     with open("response.txt", "w") as f:
#         f.write(response.text)
#     with open("response.txt", "r") as f:
#         file = f.readlines()
#     for line in file:
#         if 'title="La Verità"' in line:
#             line = line.split(sep='"')
#             if line[1].endswith(".webp"):
#                 image_filename = line[1].split(sep="/")[-1].split(sep=".")[0] + "-big.webp"
#                 print(line[1])
#                 image_url = "https://giornali.it" + line[1].split(sep=".")[0] + "-big" + ".webp"
#     os.system("wget " + image_url)
#     image = Image.open(image_filename).convert("RGB")
#     os.system("rm ./*.webp")
#     image.save("prova.jpg", "jpeg")
#     with open("../conf.json") as json_file:
#         data = json.load(json_file)
#         group_id = data["group-id"]
#         await context.bot.send_photo(chat_id=group_id, photo="prova.jpg")

# async def send_message():
#     response = requests.get("https://giornali.it/quotidiani-nazionali/la-verita/prima-pagina/")
#     with open("response.txt", "w") as f:
#         f.write(response.text)
#     with open("response.txt", "r") as f:
#         file = f.readlines()
#     for line in file:
#         if 'title="La Verità"' in line:
#             line = line.split(sep='"')
#             if line[1].endswith(".webp"):
#                 image_filename = line[1].split(sep="/")[-1].split(sep=".")[0] + "-big.webp"
#                 print(line[1])
#                 image_url = "https://giornali.it" + line[1].split(sep=".")[0] + "-big" + ".webp"
#     os.system("wget " + image_url)
#     image = Image.open(image_filename).convert("RGB")
#     os.system("rm ./*.webp")
#     image.save("prova.jpg", "jpeg")
#     with open("../conf.json") as json_file:
#         data = json.load(json_file)
#         token = data["api-key"]
#         group_id = data["group-id"]
#     bot = telegram.Bot(token=token)
#     bot.send_photo(chat_id=group_id, photo="prova.jpg")

    
# def main() -> None:
#     """Start the bot."""
#     # Read the token from the conf.json file
#     with open("../conf.json") as json_file:
#         data = json.load(json_file)
#         token = data["api-key"]
#         group_id = data["group-id"]
        
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token(token=token).build()
    
#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CommandHandler("send_first_page", send_first_page))
    
    
#     # job_queue = application.job_queue
#     # Add a periodic function to check the GPU status
#     # periodic_task = job_queue.run_repeating(send_first_page, interval=10, first=0) 
#     # Run the bot until the user presses Ctrl-C
#     application.run_polling()


# # if __name__ == "__main__":
# #     # main()
# #     send_message()
    
# async def main():
#     await send_message()

# asyncio.run(main())



import requests
import json
import os
from PIL import Image
import telegram
import asyncio

async def send_photo_to_telegram():
    response = requests.get("https://giornali.it/quotidiani-nazionali/la-verita/prima-pagina/")
    with open("response.txt", "w") as f:
        f.write(response.text)
    with open("response.txt", "r") as f:
        file = f.readlines()
    for line in file:
        if 'title="La Verità"' in line:
            line = line.split(sep='"')
            if line[1].endswith(".webp"):
                image_filename = line[1].split(sep="/")[-1].split(sep=".")[0] + "-big.webp"
                print(line[1])
                image_url = "https://giornali.it" + line[1].split(sep=".")[0] + "-big" + ".webp"
    os.system("wget " + image_url)
    image = Image.open(image_filename).convert("RGB")
    os.system("rm ./*.webp")
    image.save("prova.jpg", "jpeg")
    with open("../conf.json") as json_file:
        data = json.load(json_file)
        token = data["api-key"]
        group_id = data["group-id"]
    bot = telegram.Bot(token=token)
    await bot.send_photo(chat_id=group_id, photo="prova.jpg")

async def main():
    await send_photo_to_telegram()

asyncio.run(main())
