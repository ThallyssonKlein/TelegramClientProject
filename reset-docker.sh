sudo docker stop $(sudo docker ps -q)
sudo docker rm $(sudo docker ps -q -a)
sudo docker compose build --no-cache
sudo docker compose up -d
