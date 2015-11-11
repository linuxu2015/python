小乐插座推送及其他相关服务docker，基础镜像为编译安装好php55的centos，镜像已打包为centos_php_xiaole.tar
需将该镜像导入在使用该Dockerfile
卷组为/server须将本地主机的小乐程序映射该目录
centos编译安装php55，小乐服务需要php支持redis和pthreads
yum install -y gcc gcc-c++  make zlib zlib-devel pcre pcre-devel  libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers openssl-devel openssl.x86_64 libxml2 libxml2-devel  libxml2-devel bzip2-devel libcurl-devel libjpeg-devel libpng-devel freetype-devel gmp-devel openssl-devel  tar git -y
wget http://cn2.php.net/distributions/php-5.5.28.tar.gz
tar xf php-5.5.28.tar.gz
cd wget http://cn2.php.net/distributions/php-5.5.28.tar.gz
tar xf php-5.5.28.tar.gz
cd php-5.5.28
./configure  --prefix=/usr/local/php --with-config-file-path=/usr/local/php/etc --with-bz2 --with-curl --enable-ftp --enable-sockets --disable-ipv6 --with-gd --with-jpeg-dir=/usr/local --with-png-dir=/usr/local --with-freetype-dir=/usr/local --enable-gd-native-ttf --with-iconv-dir=/usr/local --enable-mbstring --enable-calendar --with-gettext --with-libxml-dir=/usr/local --with-zlib --with-pdo-mysql=mysqlnd --with-mysqli=mysqlnd --with-mysql=mysqlnd --enable-dom --enable-xml --enable-fpm --with-libdir=lib64 --enable-bcmath --enable-ctype --enable-exif --enable-fileinfo  --with-gmp  --enable-json --enable-pdo --enable-simplexml --enable-shmop  --enable-posix  --enable-phar --enable-zip --enable-sysvsem --enable-fpm --with-xmlrpc --enable-maintainer-zts --with-openssl  --enable-pcntl
make clean
make 
make install
cp php.ini-production /usr/local/php/etc/php.ini
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf

redis
git clone https://github.com/nicolasff/phpredis.git
cd phpredis/
/usr/local/php/bin/phpize
./configure --with-php-config=/usr/local/php/bin/php-config
make
make install
pthreads安装
wget http://pecl.php.net/get/pthreads-2.0.10.tgz
tar xf pthreads-2.0.10.tgz 
cd pthreads-2.0.10
/usr/local/php/bin/phpize
./configure --with-php-config=/usr/local/php/bin/php-config
make
make install

修改php的配置文件php.ini,添加如下  模块目录可能有不同，根据自己的目录修改
extension = "/usr/local/php/lib/php/extensions/no-debug-zts-20121212/pthreads.so"
extension = "/usr/local/php/lib/php/extensions/no-debug-zts-20121212/redis.so"

