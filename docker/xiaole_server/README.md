С�ֲ������ͼ�������ط���docker����������Ϊ���밲װ��php55��centos�������Ѵ��Ϊcentos_php_xiaole.tar
�轫�þ�������ʹ�ø�Dockerfile
����Ϊ/server�뽫����������С�ֳ���ӳ���Ŀ¼
centos���밲װphp55��С�ַ�����Ҫphp֧��redis��pthreads
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
pthreads��װ
wget http://pecl.php.net/get/pthreads-2.0.10.tgz
tar xf pthreads-2.0.10.tgz 
cd pthreads-2.0.10
/usr/local/php/bin/phpize
./configure --with-php-config=/usr/local/php/bin/php-config
make
make install

�޸�php�������ļ�php.ini,�������  ģ��Ŀ¼�����в�ͬ�������Լ���Ŀ¼�޸�
extension = "/usr/local/php/lib/php/extensions/no-debug-zts-20121212/pthreads.so"
extension = "/usr/local/php/lib/php/extensions/no-debug-zts-20121212/redis.so"

