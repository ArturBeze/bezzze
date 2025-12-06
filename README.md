ReadMe

sudo rm /etc/nginx/sites-avillable/bezzze.ru
sudo rm /etc/nginx/sites-enabled/bezzze.ru

sudo nano /etc/nginx/sites-avillable/bezzze.ru
sudo nano /etc/nginx/sites-enabled/bezzze.ru

ssl_certificate /etc/letsencrypt/live/bezzze.ru/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/bezzze.ru/privkey.pem;
