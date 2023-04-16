from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import openai
openai.api_key = "MY_API_KEY"  # the api key will be inserted accordingly


def ask_gpt(question):
    model_engine = "davinci"
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am a bot that can answer your questions. Please ask me anything.")


def answer(update, context):
    question = update.message.text
    response = ask_gpt(question)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def main():
    updater = Updater(token="MY_TOKEN", use_context=True)  # the bot token name will be inserted accordingly
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    answer_handler = MessageHandler(Filters.text & ~Filters.command, answer)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(answer_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
