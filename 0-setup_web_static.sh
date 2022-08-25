#!/usr/bin/env bash
#set up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo sh -c 'echo "Holberton School" > /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}' /etc/nginx/sites-available/default
sudo service nginx restart
