# Configure Nginx

'''
server {
    listen 443 ssl;
    server_name bezzze.ru;
    # ... other SSL/root domain configuration ...

    # 1. Route the n8n subpath to the n8n container (port 5678)
    location /n8n/ {
        # IMPORTANT: Route traffic to the n8n port
        proxy_pass http://127.0.0.1:5678;

        # WebSocket support for n8n
        proxy_set_header Connection "upgrade";
        proxy_set_header Upgrade $http_upgrade;

        # Standard proxy headers
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 2. Route all other traffic (the root domain and other paths) to FastAPI
    location / {
        # IMPORTANT: Route traffic to the FastAPI port
        proxy_pass http://127.0.0.1:8000;

        # Standard proxy headers
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
'''
