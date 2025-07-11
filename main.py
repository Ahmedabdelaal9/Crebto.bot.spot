import requests
import time
import json
from telegram import Bot

# تحميل إعدادات من config.json
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

BOT_TOKEN = config['telegram_bot_token']
CHAT_ID = config['telegram_chat_id']
MIN_TRADE_AMOUNT = config['min_trade_amount']

bot = Bot(token=BOT_TOKEN)

def get_binance_whales():
    # هنا مثال بسيط: في الواقع تحتاج API أو مصدر بيانات مناسب
    # هذا مثال وهمي لإرسال رسالة
    whales = [
        {"address": "حوت1", "platform": "Binance", "amount": 1500000, "coin": "BTC", "type": "شراء"},
        {"address": "حوت2", "platform": "Bybit", "amount": 900000, "coin": "ETH", "type": "شراء"},
    ]
    return whales

def send_whale_alert(whale):
    msg = f"""🚨 صفقة حوت ضخمة 🚨

📊 المنصة: {whale['platform']}
💰 القيمة: {whale['amount']} دولار
📈 العملة: {whale['coin']}
🧠 نوع العملية: {whale['type']} 🟢
⏱️ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}"""

    bot.send_message(chat_id=CHAT_ID, text=msg)

def main():
    print("بدء مراقبة الحيتان...")
    while True:
        whales = get_binance_whales()
        for whale in whales:
            if whale['amount'] >= MIN_TRADE_AMOUNT:
                send_whale_alert(whale)
                print(f"تم إرسال تنبيه لحوت: {whale['address']}")
        time.sleep(60*10)  # كل 10 دقائق

if __name__ == "__main__":
    main()
