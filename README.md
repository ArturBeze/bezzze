# 🛠 Шаг 1: Подготовка сервера

Подключись к VPS по SSH:

ssh user@your-server-ip


Установи Docker и Docker Compose (если еще нет):

\# Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

\# Docker Compose v2
sudo apt install docker-compose-plugin -y

\# Проверка
docker --version
docker compose version


Создай папку для проекта:

mkdir -p ~/project
cd ~/project

# 🛠 Шаг 2: Клонируем репозиторий
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git .


Точка . в конце нужна, чтобы содержимое репозитория попало в текущую папку.

# 🛠 Шаг 3: Настройка .env

Скопируй пример:

cp .env.example .env


Открой для редактирования:

nano .env


Замени переменные на свои:

POSTGRES_PASSWORD=strongpassword
RABBITMQ_PASSWORD=rabbitpass
MONGO_INITDB_ROOT_PASSWORD=mongopass
REDIS_PASSWORD=redispass
DOMAIN=bezzze.ru


Если используешь другой домен, поменяй DOMAIN.

Сохрани и выйди (Ctrl+O, Enter, Ctrl+X).

# 🛠 Шаг 4: Первый запуск Docker Compose
docker compose up -d


Флаги -d запускают контейнеры в фоне.

Проверка:

docker compose ps


Ты должен увидеть все сервисы: n8n, postgres, redis, rabbitmq, mongo, site, caddy.

# 🛠 Шаг 5: Настройка GitHub Actions (опционально для автодеплоя)

На GitHub → Settings → Secrets → Actions добавь:

Secret	Значение
SERVER_HOST	IP или домен сервера
SERVER_USER	имя пользователя SSH
SERVER_SSH_KEY	приватный ключ SSH (без пароля)

При пуше в ветку main Actions будет автоматически:

подключаться к серверу

делать git pull

обновлять Docker Compose

# 🛠 Шаг 6: Проверка

Открой браузер и зайди на:

https://bezzze.ru/
https://bezzze.ru/n8n/


Сайт должен открываться, n8n доступен по /n8n/.

# 🛠 Шаг 7: Обновления

Локально меняешь файлы (site, docker-compose.yml, Caddyfile, .env)

Commit и push в GitHub:

git add .
git commit -m "Update site or configs"
git push


Если Actions настроен — обновление на сервере пройдет автоматически.
Если нет — на сервере:

cd ~/project
git pull
docker compose up -d --build


server {
    listen 80;
    server_name bezzze.ru;

    # Перенаправляем HTTP на HTTPS
    return 301 https://$host$request_uri;
}

# NGINX

  server {
      listen 443 ssl;
      server_name bezzze.ru;
  
      root /usr/share/nginx/html;
      index index.html;
  
      # SSL сертификаты
      ssl_certificate /etc/letsencrypt/live/bezzze.ru/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/bezzze.ru/privkey.pem;
  
      ssl_protocols TLSv1.2 TLSv1.3;
      ssl_ciphers HIGH:!aNULL:!MD5;
  
      # FastAPI прокси
      location /api/ {
          proxy_pass http://fastapi:8000/;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
      }
  
      # N8N прокси
      location /n8n/ {
          proxy_pass http://n8n:5678/;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
      }
  
      # Статический сайт
      location / {
          try_files $uri $uri/ /index.html;
      }
  }

