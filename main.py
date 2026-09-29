import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Welcome to Global Connect Hub!\n\n"
        "Find remote jobs, scholarships, freelance work, "
        "and online opportunities worldwide."
    )

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Remote Jobs\n\n"
        "We share verified remote opportunities here.\n"
        "Always check the employer before applying and never pay upfront fees."
    )

async def scholarships(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Scholarships\n\n"
        "We share scholarship opportunities and application information here.\n"
        "Always verify the official scholarship website."
    )

async def freelance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💻 Freelance Opportunities\n\n"
        "Find legitimate freelance and online work opportunities."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Need help?\n\n"
        "🌍 Join our channel: https://t.me/globalconnecthub24"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))
app.add_handler(CommandHandler("scholarships", scholarships))
app.add_handler(CommandHandler("freelance", freelance))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
