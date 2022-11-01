# Django_AWS

### ssh연결

sudo ssh -i Key_Never.pem ubuntu@43.200.92.0


### venv 연결
cd Django_AWS
source venv/bin/activate

## 서버 키기

### uwsgi 연결
uwsgi --http :8000 -i /etc/uwsgi/sites/server_django.ini

### nginx 연결

nginx sudo systemctl restart nginx


| http://43.200.92.0/