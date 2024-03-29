> References:
> https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
> https://www.digitalocean.com/community/questions/how-to-deploy-multiple-django-apps-as-subdomains-using-nginx-and-gunicorn


# 1. Create and open a systemd socket file for Gunicorn

The Gunicorn socket will be created at boot and will listen for connections. When a connection occurs, systemd will automatically start the Gunicorn process to handle the connection.

```bash
$ sudo vim /etc/systemd/system/gunicorn-for-tutoring.socket
```

Inside, we will create a [Unit] section to describe the socket,
a [Socket] section to define the socket location,
and an [Install] section to make sure the socket is created at the right time:

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn-for-tutoring.sock

[Install]
WantedBy=sockets.target
```


# 2. Create and open a systemd service file for Gunicorn

The service filename should match the socket filename with the exception of the extension:

```bash
$ sudo vim /etc/systemd/system/gunicorn-for-tutoring.service
```

Start with the [Unit] section, which is used to specify metadata and dependencies.
We’ll put a `Description` of our service here and tell the init system to only start this `After` the networking target has been reached. Because our service relies on the socket from the socket file, we need to include a `Requires` directive to indicate that relationship.

Next, we’ll open up the [Service] section. We’ll specify the `User` and `Group` that we want to process to run under. We will give our `regular user account` ownership of the process since it owns all of the relevant files. We’ll give group ownership to the `www-data` group so that Nginx can communicate easily with Gunicorn.
We’ll then map out the `working directory` and specify the command to use to start the service.
In this case, we’ll have to specify the full path to the `Gunicorn executable`, which is installed within our virtual environment.
We will `bind` the process to the Unix socket we created within the /run directory so that the process can communicate with Nginx.
We `log` all data to standard output so that the journald process can collect the Gunicorn logs.
We can also specify any optional Gunicorn tweaks here. For example, we specified 3 `worker` processes in this case.

Finally, we’ll add an [Install] section. This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running.

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn-for-tutoring.socket
After=network.target

[Service]
User=jake
Group=www-data
WorkingDirectory=/home/jake/tutoring/backend
ExecStart=/home/jake/tutoring/backend/.venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn-for-tutoring.sock \
          a_project_config.wsgi:application

[Install]
WantedBy=multi-user.target
```

We can now start and enable the Gunicorn socket.
This will create the socket file at `/run/gunicorn-for-tutoring.sock` now and at boot.
When a connection is made to that socket, systemd will automatically start the `gunicorn-for-tutoring.service` to handle it:

```bash
$ sudo systemctl start gunicorn-for-tutoring.socket
$ sudo systemctl enable gunicorn-for-tutoring.socket
Created symlink /etc/systemd/system/sockets.target.wants/gunicorn-for-tutoring.socket → /etc/systemd/system/gunicorn-for-tutoring.socket.
```

We can confirm that the operation was successful by checking for the socket file.

Note:
- To stop the systemd service.
  Reference: https://superuser.com/questions/513159/how-to-remove-systemd-services
    ```bash
    $ systemctl stop gunicorn-for-tutoring
  
    $ sudo systemctl status gunicorn-for-tutoring
    Unit gunicorn-for-tutoring.service could not be found.
  
    $ systemctl daemon-reload
    $ systemctl reset-failed
    ```

# 3. Checking for the Gunicorn Socket File

Check the status of the process to find out whether it was able to start:
```bash
$ sudo systemctl status gunicorn-for-tutoring.socket
● gunicorn-for-tutoring.socket - gunicorn socket
     ...
```

Notes:
- If something goes wrong, Check the Gunicorn socket’s logs by typing:
    ```bash
    $ sudo journalctl -u gunicorn-for-tutoring.socket
    ```
- If it returns something like `Feb 14 06:11:18 ubuntu systemd[1]: gunicorn-for-tutoring.socket: Socket unit configuration has changed while unit has been running, no open socket file descriptor left. The socket unit is not functional until restarted.`
    ```bash
    # Stop the gunicorn-for-tutoring.socket unit:
    $ sudo systemctl stop gunicorn-for-tutoring.socket
    # Reload the systemd configuration to ensure that the changes are applied:
    $ sudo systemctl daemon-reload
    # Start the gunicorn-for-tutoring.socket unit again:
    $ sudo systemctl start gunicorn.socket
    ```
- If it returns `Loaded: loaded (/etc/systemd/system/gunicorn-for-tutoring.service; disabled; vendor preset: enabled)  Active: failed (Result: exit-code)`, run:
    ```bash
    $ sudo systemctl start gunicorn-for-tutoring
    ```

Next, check for the existence of the gunicorn-for-tutoring.sock file within the /run directory:
```bash
$ file /run/gunicorn-for-tutoring.sock
/run/gunicorn-for-tutoring.sock: socket
```

Check gunicorn--for-tutoring process:
```bash
$ ps ax|grep gunicorn--for-tutoring
```

# 4. Testing Socket Activation

Currently, if you’ve only started the gunicorn-for-tutoring.socket unit, the gunicorn-for-tutoring.service will not be active yet since the socket has not yet received any connections. You can check this by typing:
```bash
$ sudo systemctl status gunicorn-for-tutoring
● gunicorn-for-tutoring.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/gunicorn-for-tutoring.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: ● gunicorn-for-tutoring.socket
```

To test the socket activation mechanism, we can send a connection to the socket through curl by typing:
```bash
$ curl --unix-socket /run/gunicorn-for-tutoring.sock localhost
```

You should receive the HTML output from your application in the terminal. This indicates that Gunicorn was started and was able to serve your Django application. You can verify that the Gunicorn service is running by typing:

```bash
$ sudo systemctl status gunicorn-for-tutoring
● gunicorn-for-tutoring.service - gunicorn daemon
     ...
```

If you make changes to the `/etc/systemd/system/gunicorn-for-tutoring.service` file, reload the daemon to reread the service definition and restart the Gunicorn process by typing:
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn-for-tutoring
```
