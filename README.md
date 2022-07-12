# FO - Drive - Server

---

### Easy designed drive system that allow you to remotely save your files on a server

---

[FO - Drive](https://github.com/path/to/fodrive) is a free easy-to-use drive system that allow you to remotely save your files on a server.

You are actually seeing the server project. The client is aviable [here](https://github.com/path/to/fodrive).

---

## Setup

### We will cover here the setup of FO - Drive server.

#### First, let's take a look at what is needed to run a FO - Drive server :

- A server that can bind a web application.

And... that it !

I personally recommend [repl.it](https://replit.com) (without commercial partnership), as it is fast, and if you combine it with [uptimerobot](https://uptimerobot.com/), you can have a webserver that is always up.

The choice is yours, but it can be a bad idea to host the server directly at home, for example. You should prefer remote hosting.

#### Now, let's install everything !

Simply past the code bellow, and it should install the server :

```bash
git clone https://github.com/uremom
cd fo-drive_server/
python -m pip install -r requirements.txt
python setup.py
```

Once finished running, `setup.py` should have successfully installed and configured FO - Drive server.

After that, you should be able to run `main.py`, and launch the server, ready for client to start using !

---

TODO :

- [ ] Start creating the server app
- [ ] Create smooth UI.