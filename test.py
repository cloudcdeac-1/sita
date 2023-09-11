/bin/bash
yum update -y
yum install httpd -y
mkdir /var/www/html/laptop
echo "Laptop page IP is $HOSTNAME" > /var/www/html/laptop/index.html
systemctl start httpd
systemctl enable httpd

