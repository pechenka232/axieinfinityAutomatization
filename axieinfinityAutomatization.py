import requests
import time
import imaplib
import email
import re
from bs4 import BeautifulSoup
from web3 import Web3

# APIшник от 2Captcha
API_KEY = 'APIшник'
EMAIL = "Почта"
PASSWORD = "Пароль"
IMAP_SERVER = "imap"
wallet = "wallet"  
RPC_URL = "Инфуриа"

# Подключаем Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if web3.is_connected():
    print("Web3: Подключено к Ethereum")
else:
    print("Web3: Ошибка подключения")

# Функция для отправки запроса на регистрацию
def register_user(email):
    url = "https://graphql-gateway.axieinfinity.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://axieinfinity.com",
        "Origin": "https://axieinfinity.com",
        "Accept": "application/json"
    }

    data = {
        "query": """
            mutation SendVerificationEmail($email: String!, $actionType: Int!) {
                atiaLegacySendVerificationEmail(email: $email, actionType: $actionType)
            }
        """,
        "variables": {"email": email, "actionType": 0}
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Запрос на регистрацию отправлен")
    else:
        print(f"Ошибка при регистрации: {response.status_code}, Ответ: {response.text}")

# Функция для получения кода подтверждения из почты
def get_verification_code():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        for _ in range(15):  # Попытки в течение 3 минут
            result, data = mail.search(None, 'FROM "no-reply@axieinfinity.com"')
            if data[0]:
                latest_email_id = data[0].split()[-1]
                result, msg_data = mail.fetch(latest_email_id, "(RFC822)")
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                code = re.search(r"\b\d{6}\b", body)
                if code:
                    return code.group(0)

            print("Ожидание кода подтверждения...")
            time.sleep(10)

        print("Код подтверждения не найден")
        return None

    except Exception as e:
        print("Ошибка при получении кода:", e)
        return None

# Функция для получения URL капчи
def get_captcha_image():
    url = "https://axieinfinity.com/pre-register"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    captcha_image = soup.find('img', class_='axie-captcha-image')

    if captcha_image:
        captcha_url = captcha_image['src']
        print(f'URL капчи: {captcha_url}')
        return captcha_url
    else:
        print('Капча не найдена')
        return None

# Функция для отправки капчи в 2Captcha
def solve_captcha(captcha_url):
    response = requests.post(
        'http://2captcha.com/in.php',
        data={'key': API_KEY, 'method': 'url', 'body': captcha_url, 'json': 1}
    )
    result = response.json()
    if result['status'] == 1:
        captcha_id = result['request']
        print(f'Капча отправлена на решение, ID: {captcha_id}')
        return captcha_id
    else:
        print(f'Ошибка отправки капчи: {result["request"]}')
        return None

# Функция для получения решения капчи
def get_solution(captcha_id):
    while True:
        response = requests.get(
            f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}&json=1'
        )
        result = response.json()
        if result['status'] == 1:
            print(f'Капча решена! Результат: {result["request"]}')
            return result["request"]
        else:
            print('Ожидание решения капчи...')
            time.sleep(15)

# Функция для проверки кошелька
def check_wallet(wallet_address):
    if not web3.is_address(wallet_address):
        print("Некорректный адрес кошелька")
        return False

    balance = web3.eth.get_balance(wallet_address)
    balance_eth = web3.from_wei(balance, 'ether')

    print(f"Баланс кошелька {wallet_address}: {balance_eth} ETH")
    return True

# Основной процесс
email_to_register = EMAIL  

# Получаем капчу и решаем
captcha_url = get_captcha_image()
if captcha_url:
    captcha_id = solve_captcha(captcha_url)
    if captcha_id:
        captcha_solution = get_solution(captcha_id)
        if captcha_solution:
            print(f"Решенная капча: {captcha_solution}")

# Отправляем запрос на регистрацию
register_user(email_to_register)

# Ждем код подтверждения
verification_code = get_verification_code()
if verification_code:
    print(f"Код подтверждения: {verification_code}")
else:
    print("Код подтверждения не получен")

# Проверяем кошелек

if check_wallet(wallet):
    print("Кошелек валиден, регистрация подтверждена")
else:
    print("Ошибка с кошельком")
