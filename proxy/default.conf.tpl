server {
    listen ${LISTEN_PORT};

    location /static {
        add_header 'Access-Control-Allow-Origin' '*';
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}
