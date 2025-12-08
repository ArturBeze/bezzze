ReadMe


sudo rm /etc/nginx/sites-avillable/bezzze.ru

sudo rm /etc/nginx/sites-enabled/bezzze.ru


sudo nano /etc/nginx/sites-avillable/bezzze.ru

sudo nano /etc/nginx/sites-enabled/bezzze.ru


Fullchain certificate location

    ssl_certificate /etc/letsencrypt/live/bezzze.ru/fullchain.pem;

Privkey certificate location

    ssl_certificate_key /etc/letsencrypt/live/bezzze.ru/privkey.pem;


Start nginx

    sudo systemctl start nginx
    
Stop nginx

    sudo systemctl stop nginx
    
Restart nginx

    sudo systemctl restart nginx
