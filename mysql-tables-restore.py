#!/usr/bin/python3

import os
import time
import datetime

DB_HOST_BACKUP =''
DB_USER_BACKUP = ''
DB_USER_PASSWORD_BACKUP = ''
DB_NAME_BACKUP = ''
COPY_BACKUP_PATH = ''
BACKUP_PATH = ''

DATETIME = time.strftime('%Y%m%d-%H%M%S')
print ("DATETIME: " + DATETIME + "\n")

DATE = time.strftime('%Y%m%d')
TODAYBACKUPPATH = BACKUP_PATH + DATE + "*/"

print (time.strftime('%Y%m%d-%H%M%S') + " - Copying backup " + TODAYBACKUPPATH + " to " + COPY_BACKUP_PATH + " ...")
copy_backup = "cp -R " + TODAYBACKUPPATH + " " + COPY_BACKUP_PATH
os.system(copy_backup)
print (time.strftime('%Y%m%d-%H%M%S') + " - " + TODAYBACKUPPATH + " copied to " + COPY_BACKUP_PATH + "\n")

gunzip_path = COPY_BACKUP_PATH + DATE + "*"
print (time.strftime('%Y%m%d-%H%M%S') + " - Extracting backup files in " + gunzip_path + " ...")
gunzip = "gunzip " + gunzip_path + "/*"
os.system(gunzip)
print (time.strftime('%Y%m%d-%H%M%S') + " - Backup files extracted.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Listing files/tables inside " + gunzip_path + " ...")
sqlfiles_cmd = "ls " + gunzip_path
sqlfiles_data_raw = os.popen(sqlfiles_cmd).read()
sqlfiles_data = sqlfiles_data_raw.split('\n')
sqlfiles_data.pop()
sqlfiles_data_new = ''
print (time.strftime('%Y%m%d-%H%M%S') + " - Listing files/tables inside " + gunzip_path + " done.\n")

for sqlfiles in sqlfiles_data:
    sqlfiles_data_new += sqlfiles +'\n'
    #tables_name = sqlfiles.split('.')
    sqlfiles2_cmd = "ls " + gunzip_path + "/" + sqlfiles
    sqlfiles2 = os.popen(sqlfiles2_cmd).read()
    sqlfiles2 = sqlfiles2[:-1]
    print (time.strftime('%Y%m%d-%H%M%S') + " - Restoring " + sqlfiles2 + " ...")
    restore_cmd = "mysql -h " + DB_HOST_BACKUP + " -u " + DB_USER_BACKUP + " -p" + DB_USER_PASSWORD_BACKUP + " " + DB_NAME_BACKUP + " < " + sqlfiles2
    os.system(restore_cmd)
    print (time.strftime('%Y%m%d-%H%M%S') + " - " + sqlfiles2 + " restored.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Restore script completed, your backup has been restored to " + DB_HOST_BACKUP + ".\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Deleting extracted files ...")
rmgunzip = "rm -rf " + COPY_BACKUP_PATH + "*"
os.system(rmgunzip)
print (time.strftime('%Y%m%d-%H%M%S') + " - Extracted files deleted.\n")
