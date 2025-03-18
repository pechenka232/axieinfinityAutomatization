🤖 Automated Registration for Axie Infinity
This script automates the registration process on Axie Infinity, solves CAPTCHA using 2Captcha, retrieves the verification code from email, and checks the wallet balance on the Ethereum network using Web3.

🔧 Features
✅ Sends a registration request via email
✅ Retrieves a verification code from email
✅ Solves CAPTCHA using 2Captcha
✅ Checks the wallet balance in ETH

🛠 Installation & Setup
1️⃣ Install dependencies

pip install requests imapclient email bs4 web3
2️⃣ Configure the script
Edit the following variables before running the script:


API_KEY = 'YOUR_2CAPTCHA_API_KEY'
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_EMAIL_PASSWORD"
IMAP_SERVER = "imap.yourmail.com"  # Specify your IMAP server (e.g., imap.gmail.com)
wallet = "YOUR_ETH_WALLET"
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
3️⃣ Run the script

⚙ How the Script Works
1️⃣ Retrieves CAPTCHA and submits it to 2Captcha for solving
2️⃣ Sends a registration request
3️⃣ Checks email for the verification code
4️⃣ Verifies wallet balance in ETH
5️⃣ Displays the result: successful registration or an error

📌 Important Notes
Your email must support IMAP for email verification
CAPTCHA is solved automatically using 2Captcha
A valid RPC URL (e.g., Infura) is required for wallet balance verification
📜 License
This project is released under the MIT License. Use at your own risk.





🤖 Автоматическая регистрация на Axie Infinity
Этот скрипт выполняет автоматическую регистрацию на сайте Axie Infinity, решает капчу через 2Captcha, получает код подтверждения с почты и проверяет баланс кошелька в сети Ethereum с использованием Web3.

🔧 Функционал
✅ Отправка запроса на регистрацию по email
✅ Получение кода подтверждения из почты
✅ Решение капчи через 2Captcha
✅ Проверка кошелька и его баланса в ETH

🛠 Установка и настройка
1️⃣ Установите зависимости

pip install requests imapclient email bs4 web3
2️⃣ Заполните конфигурацию в коде
Отредактируйте переменные в коде перед запуском:


API_KEY = 'ВАШ_API_КЛЮЧ_ОТ_2CAPTCHA'
EMAIL = "ВАША_ПОЧТА"
PASSWORD = "ВАШ_ПАРОЛЬ_ОТ_ПОЧТЫ"
IMAP_SERVER = "imap.yourmail.com"  # Укажите IMAP-сервер (например, imap.gmail.com)
wallet = "ВАШ_ETH_WALLET"
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
3️⃣ Запустите скрипт

⚙ Как работает скрипт
1️⃣ Получает капчу и отправляет её в 2Captcha для решения
2️⃣ Отправляет запрос на регистрацию
3️⃣ Проверяет почту и извлекает код подтверждения
4️⃣ Проверяет баланс кошелька в ETH
5️⃣ Выводит результат: успешная регистрация или ошибка

📌 Важно
Для работы с почтой ваш email должен поддерживать IMAP
Капча решается автоматически через 2Captcha
Для проверки кошелька требуется актуальный RPC-URL (например, Infura)
📜 Лицензия
Этот проект распространяется под лицензией MIT. Используйте на свой страх и риск.



