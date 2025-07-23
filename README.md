# HTTP server for a keepass database

This server is a simple file server for one file (the keepass password
database).

Keepass 2.59 windows client saves the database over HTTP(S) like this:
```
"GET    /passwords-personal.kdbx HTTP/1.1" 200 -
"PUT    /passwords-personal.kdbx.tmp HTTP/1.1" 200 -
"GET    /passwords-personal.kdbx HTTP/1.1" 200 -
"DELETE /passwords-personal.kdbx HTTP/1.1" 200 -
"MOVE   /passwords-personal.kdbx.tmp HTTP/1.1" 200 -
"GET    /passwords-personal.kdbx HTTP/1.1" 200 -
```

> [!NOTE] Note
> The `MOVE` method is somewhat uncommon. Keepass includes a `Location` header with that specifies the destionation to move to (URI is the source)

This server is made to fulfill these requests made by a Keepass client but nothing more.

## Features

There are callbacks for
- backing up the database before overwriting
- synchronization with external location (like rclone-mounted google drive
location)

## Deployment

- Adjust the filenames and locations in `config.py`.
- Start the server by running `start.sh`.
  - You're going to need Python3.12 or newer with packages `flask` and `gunicorn`.
- Configure reverse proxy with nginx or a web server of your choice.

> [!CAUTION]
> Caution! When exposing this server to the internet, make sure to
> protect the access with HTTP Auth (nginx `auth_basic` directive) and TLS
> (certbot)!

## When is this useful?

Imagine you're unable to install google drive software to your company laptop.
This is where it's beneficial to have the database accessible by HTTPS (with
authentication, of course - this is within Keepass capabilities). On your
server, the database can be synchronized back to google drive with rclone.
