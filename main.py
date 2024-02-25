import telebot

# 替换成你的Telegram Bot Token
TOKEN = '6979288571:AAFEWvS102C3OPg7fPS6VXhUsnOGchVe-cA'

bot = telebot.TeleBot(TOKEN)

# CSS样式
CSS_STYLE = """
<style>
/* 添加你的 CSS 样式 */
body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f2f2f2;
}

.namecard {
    border: 2px solid #ccc;
    border-radius: 10px;
    padding: 20px;
    width: 300px;
    background-color: #fff;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.name {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 10px;
}

.position {
    font-style: italic;
    color: #666;
    text-align: center;
    margin-bottom: 15px;
}

.contact {
    color: #444;
    text-align: center;
}

.contact-item {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 5px;
}

.contact-item img {
    width: 20px;
    height: 20px;
    margin-right: 5px;
}

.contact-item span {
    font-size: 14px;
}

.button {
    display: block;
    width: 100%;
    text-align: center;
    background-color: #4CAF50;
    color: white;
    padding: 10px 0;
    margin-top: 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #45a049;
}
</style>
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "欢迎使用名片生成器！请发送您的名字、职位和联系方式。")

@bot.message_handler(func=lambda message: True)
def generate_namecard(message):
    # 解析用户输入
    user_input = message.text.split('\n')
    name = user_input[0]
    position = user_input[1]
    contact = user_input[2]

    # 生成名片HTML
    namecard_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>个性化名片</title>
    {CSS_STYLE}
    </head>
    <body>
    <div class="namecard">
        <div class="name">{name}</div>
        <div class="position">{position}</div>
        <div class="contact">{contact}</div>
    </div>
    </body>
    </html>
    """

    # 保存名片为HTML文件
    with open('namecard.html', 'w') as f:
        f.write(namecard_html)

    # 发送名片给用户
    bot.send_message(message.chat.id, "您的名片已生成，请查收！", parse_mode='HTML')
    bot.send_document(message.chat.id, open('namecard.html', 'rb'))

bot.polling()