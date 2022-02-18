import ptbot
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

token = "5279817313:AAGzLCXYkgbM-_VfG0fgflS50HjVGfdaREU"
id = "5122589211"


def notify_progress(secs_left, message_id, pertime):
    bot.update_message(
        id,
        message_id,
        f"Осталось секунд:{secs_left}{render_progressbar(pertime,secs_left)}"
    )


def reply(id, text):
    pertime = parse(text)
    message_id = bot.send_message(id, "ᅠ ᅠ")
    bot.create_countdown(
        pertime,
        notify_progress,
        message_id=message_id,
        pertime=pertime
    )
    bot.create_timer(pertime, notify)


def notify():
    bot.send_message(id, "Время вышло")
bot = ptbot.Bot(token)
bot.reply_on_message(reply)

bot.run_bot()
