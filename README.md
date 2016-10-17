# sqlmongo
A quick flask-based app running both a PostgreSQL database and a Mongo Database.
Everything here can be easily altered or adapted to meet other needs.


## Install

1. Install Virtualbox and Vagrant
2. git clone this repo
3. open a Terminal, cd to ~/sqlmongo folder, and run "vagrant up"
4a. Wait about 10 min, until scripts stop running
4b. Run "vagrant ssh" to gain ssh access to virtual instance
5. open a browser: http://127.0.0.1:8080
5a. Alternatively, after SSHing in, run:
```shell
    sudo su -
    cd /var/www/sqlmongo
    python sqlmongo.py
```
5b. open http://127.0.0.1:9999, for DEBUG mode







## To access databases via terminal:



# Reset SQL Database
```shell
su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
```

# Postgres

Ensure that you have the Postgres 9.5 client. To install it, on Ubuntu Wily 15.10:

```shell
sudo su -
echo "deb http://apt.postgresql.org/pub/repos/apt/ wily-pgdg main" > \
    /etc/apt/sources.list.d/postgres.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt-get update
apt-get install -y postgresql-client-9.5
```

Connect to the database, from host machine:
```shell
psql -U sqldb -d sqlmongo -h 127.0.0.1 -W
the password is "sqldb"
```

Reset the database, within the guest VM:
```shell
sudo su - postgres -c "psql -f /vagrant/psql/db_reset.sql"
# become the postgres user, and run the command psql, with the file db_reset.sql
```

# Mongo

# to enter mongo on console
```mongod```





## System Logs
```shell

# python log
sudo nano /var/log/sqlmongo/info.log
watch tail -32 /var/log/sqlmongo/info.log

# uwsgi log
sudo nano /var/log/uwsgi/app/sqlmongo.log
sudo nano /var/log/uwsgi/app/uwsgi.log

# nginx logs
sudo nano /var/log/nginx/access.log
sudo nano /var/log/nginx/error.log

```









