sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/hello.py /usr/local/lib/python2.7/hello.py
sudo /etc/init.d/gunicorn restart
