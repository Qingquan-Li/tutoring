> References:
> https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
> https://stackoverflow.com/questions/65124421/deploy-both-django-and-react-on-cloud-using-nginx
> https://mattsegal.dev/nginx-django-reverse-proxy-config.html


# Configure Nginx to Proxy Pass to Gunicorn

After Gunicorn is set up, we need to configure Nginx to pass traffic to the process.

Start by creating and opening a new server block in Nginx’s sites-available directory:
```bash
$ sudo vim /etc/nginx/sites-available/tutoring
```

Inside, open up a new server block. We will start by specifying that this block should `listen` on the normal port `80` and that it should respond to our server’s `domain name` or `IP address`.

Next, we will tell Nginx to ignore any problems with finding a `favicon`. We will also tell it where to find the `static` assets that we collected in our `~/myprojectdir/static` directory. All of these files have a standard URI prefix of “/static”, so we can create a location block to match those requests.

Finally, we’ll create a location / {} block to match all other requests. Inside of this location, we’ll include the standard `proxy_params` file included with the Nginx installation and then we will pass the traffic directly to the `Gunicorn socket`:
```
server {
    listen 80;
    server_name tutoring.helpyourmath.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/jake/tutoring/backend;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn-for-tutoring.sock;
    }

}

Handle React.js (frontend) and Django (backend) with letsencrypt:

```
server {
    #listen 80;
    server_name tutoring.helpyourmath.com;

    location / {
        root /home/jake/tutoring/frontend/build;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    location = /favicon.ico { access_log off; log_not_found off; }

    location /django_static/ {
        autoindex on;
        alias /home/jake/tutoring/backend/django_static/;
    }

    location /admin {
        try_files $uri @proxy_api;
    }

    location /api/v1 {
        try_files $uri @proxy_api;
    }

    location @proxy_api {
        proxy_pass http://unix:/run/gunicorn-for-tutoring.sock;
        # By default, NGINX sends a HTTP request to WSGI server with host header of 127.0.0.1
        # Ensure original Host header is forwarded to our Django app (from Nginx to Gunicorn)
        # $http_host vs $host: github.com/frappe/frappe_docker/pull/184
        proxy_set_header Host $host;
        # Tell Gunicorn the original IP address of the client.
        # NGINX will always "lie" to you and say that the client IP address is 127.0.0.1.
        # Optional, if you don't want to know the client IP address.
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        # $scheme: request scheme, “http” or “https.”
        # Django sometimes needs to know whether the incoming request is secure (HTTPS) or not (HTTP).
        # For example, some features of the SecurityMiddleware class checks for HTTPS.
        # NGINX is always telling Django that the client's request to the sever is not secure, even when it is.
        # Fix it: put the client request protocol into a header called X-Forwarded-Proto.
        # Then set up the SECURE_PROXY_SSL_HEADER setting to read this header in Django settings.py file:
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/tutoring.helpyourmath.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/tutoring.helpyourmath.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = tutoring.helpyourmath.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name tutoring.helpyourmath.com;
    return 404; # managed by Certbot


}
```

Now, we can enable the file by linking it to the sites-enabled directory:
```bash
$ sudo ln -s /etc/nginx/sites-available/tutoring /etc/nginx/sites-enabled
```

Test your Nginx configuration for syntax errors by typing:
```bash
$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If no errors are reported, go ahead and restart Nginx by typing:
```bash
$ sudo systemctl restart nginx
```

Check errors in Nginx:
```bash
$ sudo vim /var/log/nginx/error.log
```

If we have enabled ufw (uncomplicated firewall), we need to open up our firewall to normal traffic on port 80:
> References:
> https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands
```bash
$ sudo ufw allow 'Nginx Full'
```
