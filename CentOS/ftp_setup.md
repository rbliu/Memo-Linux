# ftp and vsftp on CentOS 7

* To setup ftp on the CentOS 7 machine, we need to install ftp and vsftpd first:
```
yum install ftp vsftpd
```

* To look up the location of vsftpd configuration files:
```
rpm -qc vsftpd
```

* Backup the config file:
```
cd /etc/vsftpd
cp vsftpd.conf vsftpd.conf.origin
```

* Modify the config file:
```
vim /etc/vsftpd/vsftpd.conf
# anonymous_enable=YES ==> NO
listen=YES
use_localtime=YES
```
Here I only allow real user to access.

* To enable and restart vsftp:
```
systemctl enable vsftpd
systemctl restart vsftpd
```

* Configure the firewall"
```
firewall-cmd --permanent --zone=public --add-service=ftp
firewall-cmd --reload
```

* Now you can test the ftp:
```
ftp localhost
```
