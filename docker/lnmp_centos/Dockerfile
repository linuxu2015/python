FROM centos:6.6
MAINTAINER linuxu2015@gmail.com
#配置apt源
RUN rm -rf /etc/yum.repos.d/*
COPY yum.repo /etc/yum.repos.d/
#RUN echo "deb http://yum-server.aioute.com/ubuntu/mirror/mirrors.aliyun.com/ubuntu trusty main universe  multiverse restricted" > /etc/apt/sources.list
#RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list
#RUN apt-get update
#RUN apt-get upgrade -y
##安装软件
#RUN apt-get install nginx vim lrzsz php5 php5-fpm    php5-gd supervisor  php5-redis   php5-mysql  php5-cli  --force-yes -y
RUN yum install  supervisor vim lrzsz php55w php55w-fpm php55w-pear php55w-pecl-redis php55w-common php55w php55w-mbstring  php55w-gd php55w-devel php55w-mysql php55w-pecl-igbinary php55w-cli  php55w-pdo php55w-process crontabs cronie -y
RUN mkdir -p /var/log/supervisor
RUN echo "30 * * * * /usr/sbin/ntpdate 202.120.2.101" >> /var/spool/cron/root
RUN service crond restart
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
RUN rm -rf /etc/nginx/nginx.conf
RUN rm -rf /etc/supervisord.conf
COPY supervisord.conf /etc/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf
##创建数据卷
VOLUME ["/web"]
#VOLUME ["/var/log/nginx/"]
##开放端口
EXPOSE  80
CMD ["/usr/bin/supervisord"]

