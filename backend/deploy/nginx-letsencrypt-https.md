You can also use Cloudflare's Flexible SSL, which is free and easy:
https://www.cloudflare.com/ssl/

> Cloudflare allows any Internet property to become HTTPS-enabled with the click of a button. You’ll never need to worry about SSL certificates expiring or staying up to date with the latest SSL vulnerabilities when you’re using Cloudflare SSL.
>
> [Flexible SSL](https://www.cloudflare.com/ssl/) encrypts traffic from Cloudflare to end users of your website, but not from Cloudflare to your origin server. This is the easiest way to enable HTTPS because it doesn’t require installing an SSL certificate on your origin.

<br>

---

<br>

> References:
> https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04

Before performing these configurations, you must first configure Nginx.
Please check deploy/nginx-config.md

# 1. Installing Certbot

Install Certbot and it’s Nginx plugin with apt:
```bash
$ sudo apt install certbot python3-certbot-nginx
```

# 2. Obtaining an SSL Certificate

Certbot provides a variety of ways to obtain SSL certificates through plugins. The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary. To use this plugin, type the following:
```bash
$ sudo certbot --nginx -d example.com -d www.example.com
```
This runs certbot with the --nginx plugin, using -d to specify the domain names we’d like the certificate to be valid for.

**For Example:**
```bash
$ sudo certbot --nginx -d tutoring.helpyourmath.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for tutoring.helpyourmath.com
Waiting for verification...
Cleaning up challenges
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/tutoring

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/tutoring

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations! You have successfully enabled https://tutoring.helpyourmath.com

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=tutoring.helpyourmath.com
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/tutoring.helpyourmath.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/tutoring.helpyourmath.com/privkey.pem
   Your cert will expire on 2023-02-22. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

```

Some `443/SSL` statements will be appended to the Nginx configuration file ( `/etc/nginx/sites-available/tutoring` ):

```
server {
    listen 80; # This line would be deleted by Certbot. managed by Certbot
    server_name tutoring.helpyourmath.com;
    ...

    # The following statement will be appended:

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

# 3. Verifying Certbot Auto-Renewal

Let’s Encrypt’s certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process. The certbot package we installed takes care of this for us by adding a systemd timer that will run twice a day and automatically renew any certificate that’s within thirty days of expiration.

You can query the status of the timer with systemctl:

```bash
$ sudo systemctl status certbot.timer
● certbot.timer - Run certbot twice daily
     Loaded: loaded (/lib/systemd/system/certbot.timer; enabled; vendor preset: enabled)
     Active: active (waiting) since Tue 2021-11-23 00:03:54 UTC; 3h 48min ago
    Trigger: Tue 2021-11-23 14:56:00 UTC; 11h left
   Triggers: ● certbot.service

Nov 23 00:03:54 ubuntu systemd[1]: Started Run certbot twice daily.
```

To test the renewal process, you can do a dry run with certbot:
```bash
$ sudo certbot renew --dry-run
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/en.fatlitalk.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator nginx, Installer nginx
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for en.fatlitalk.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of nginx server; fullchain is
/etc/letsencrypt/live/en.fatlitalk.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates below have not been saved.)

Congratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/en.fatlitalk.com/fullchain.pem (success)
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates above have not been saved.)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
```

If you see no errors, you’re all set. When necessary, Certbot will renew your certificates and reload Nginx to pick up the changes. If the automated renewal process ever fails, Let’s Encrypt will send a message to the email you specified, warning you when your certificate is about to expire.
