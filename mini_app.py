import os
import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # Получаем имя хоста
    hostname = socket.gethostname()

    # Получаем IP-адрес хоста
    ip_address = socket.gethostbyname(hostname)

    # Получаем имя автора из переменной окружения
    author = os.getenv('AUTHOR', 'Неизвестный автор')

    return f"""
    <h1>Информация:</h1>
    <p><b>Имя хоста:</b> {hostname}</p>
    <p><b>IP-адрес хоста:</b> {ip_address}</p>
    <p><b>Автор:</b> {author}</p>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)