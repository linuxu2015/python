FROM ubuntu:latest
MAINTAINER linuxu2015@gmail.com
#配置apt源
RUN echo "deb http://yum-server.aioute.com/ubuntu/mirror/mirrors.aliyun.com/ubuntu trusty main universe  multiverse restricted" > /etc/apt/sources.list
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
##安装软件
RUN apt-get install nginx vim lrzsz php5 php5-fpm    php5-gd supervisor  php5-redis   php5-mysql  php5-cli  --force-yes -y
RUN mkdir -p /var/log/supervisor
RUN echo "30 * * * * /usr/sbin/ntpdate 202.120.2.101" >> /var/spool/cron/root
RUN service cron restart
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
RUN rm -rf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf
##创建数据卷
VOLUME ["/web"]
#VOLUME ["/var/log/nginx/"]
##开放端口
EXPOSE  80
CMD ["/usr/bin/supervisord"]

