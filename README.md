ReadMe


sudo rm /etc/nginx/sites-available/bezzze.ru

sudo rm /etc/nginx/sites-enabled/bezzze.ru


sudo nano /etc/nginx/sites-available/bezzze.ru

sudo nano /etc/nginx/sites-enabled/bezzze.ru

sudo ln -s /etc/nginx/sites-available/bezzze.ru /etc/nginx/sites-enabled/


Fullchain certificate location

    ssl_certificate /etc/letsencrypt/live/bezzze.ru/fullchain.pem;

Privkey certificate location

    ssl_certificate_key /etc/letsencrypt/live/bezzze.ru/privkey.pem;

Check nginx status

    sudo systemctl status nginx

Check nginx

    sudo nginx -t

Start nginx

    sudo systemctl start nginx
    
Stop nginx

    sudo systemctl stop nginx
    
Restart nginx

    sudo systemctl restart nginx
