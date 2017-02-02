# mysql-tables-restore
Restore MySQL database. This script **only works** if the backup ran using script from this [repo](https://github.com/dhewana/mysql-tables-dump).

## Config example
```
DB_HOST_BACKUP ='127.0.0.1'
DB_USER_BACKUP = 'dbuser'
DB_USER_PASSWORD_BACKUP = 'dbpassword'
DB_NAME_BACKUP = 'dbname'
BACKUP_PATH = '/home/user/dbname/'
COPY_BACKUP_PATH = '/home/user/gunzip/dbname/'
```
