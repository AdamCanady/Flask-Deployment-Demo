# Flask-Deployment-Demo (Worst Practices in Server Deployment)
Hey folks, this is a quick demo of how to put together a Flask app and deploy it on DigitalOcean for Carleton College's [DevX](http://devx.io). It uses such technologies as:

- Python
- Flask
- MongoDB
- Ubuntu
- Nginx (possibly in future versions)

## Getting Started with DO

You'll want a [DigitalOcean](https://digitalocean.com) account. So go there and make one. Then spin up a droplet (a virtual machine) with Ubuntu 14 on it. You can use one of their prebuilt app images if you'd like, but the default image should work ok. One cool thing you can do is add an SSH key. If you don't know about that, there's a quick guide [below](#ssh-keys). Then you can log in and install some cool stuff on it using `apt-get`. After you set up the droplet and add your key (press the button near the bottom when you're creating it), you can log in like this:

    ssh root@[SERVER IP]      where [SERVER IP] is replaced by an IP address like ssh root@104.236.27.54

Then you can use `apt-get` to install stuff. Since you logged in as `root`, you don't need to use the `sudo` command. All of your commands are automatically su-did. Install the following stuff if you're looking to use this app:

    apt-get install build-essential python-dev python-pip

Then install MongoDB using [this guide](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb) or the instructions below:

    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
    apt-get update
    apt-get install -y mongodb-org
    service mongod start

And finally, install Flask and PyMongo on this box:
    
    pip install pymongo
    pip install Flask

In this tutorial, I won't be walking through Python's virtualenv device, but it's definitely something you should get acquainted with if you plan on devving in Python a lot.

## Running this app

To run this application, go to the root of this application and run:

    python app.py

Then to make it a daemon (something that runs in the background all the time), the easiest way is:

    nohup python app.py &


## Extraneous commands that are useful

See what's running on all the ports on your system:

    netstat -tulpn

## What the files do


     app.py - this runs the app
     db_docs.js - this is what you should run to initialize your database

## SSH Keys

To give you the 2 minute introduction to SSH keys, the basic idea is that we want to give a server some piece of information and keep another piece of information that we don't share. With this and a bit of math, we can prove to the server that we are who we say we are and make it really hard for other people to act like they're us and gain access to our server. On a unix system, to generate an SSH key:

    ssh-keygen -t rsa -b 4096

then follow the guide. You can add a password and choose where to store it, but if you only have one, the default ~/.ssh/id_rsa(.pub) will work well. The file located at ~/.ssh/id_rsa is the private key (don't share this!!) and the ~/.ssh/id_rsa.pub is the public key. You can read it like this:

    cd ~
    cat .ssh/id_rsa.pub

If you go to your DigitalOcean (or BitBucket) account, you can add this SSH key (by copy and pasting it) to your account settings and automagically use it to access different resources (like servos or git push/pulling from repos). The possibilities are (relatively) endless!