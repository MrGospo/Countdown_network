# Countdown_network
Countdown to any number of screens over the network
Полностью функционирующий обратный отсчет. Упрощен код.


На Windows:
1. Скачай Python с официального сайта (https://www.python.org/downloads/windows/). (https://www.python.org/downloads/windows/) Во время установки убедись, что поставлена галочка "Add Python to PATH".
2. pip install flask flask-socketio
3. Запусти сервер python app.py
4. На сервере открой http://<ip-сервера>:8000/?admin=1
5. Открой на всех дисплеях http://<ip-сервера>:8000

На Linux:
1. sudo apt update
2. sudo apt install python3 python3-pip
3. pip3 install flask flask-socketip
4. cd countdown_project
5. python3 app.py
6. На сервере открой http://<ip-сервера>:8000/?admin=1
7. Открой на всех дисплеях http://<ip-сервера>:8000


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
