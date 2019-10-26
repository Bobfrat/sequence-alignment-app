FROM 534479722520.dkr.ecr.us-east-1.amazonaws.com/core:20181213.0

LABEL maintainer="robert.fratantonio@rpsgroup.com"

RUN yum -y install openssl

COPY docker-support/scripts/install /install
COPY docker-support/ssh/repo-key /root/.ssh/id_rsa
COPY docker-support/ssh/repo-key.pub /root/.ssh/id_rsa.pub
COPY docker-support/ssh/known_hosts /root/.ssh/known_hosts
RUN chmod 0700 /root/.ssh && \
    chmod 0600 -R /root/.ssh && \
    useradd -m oceansmap


# Install the project dependencies
COPY requirements.txt /requirements.txt
RUN /install/install_python_packages.sh

RUN mkdir /usr/share/wms_query_service
COPY tasks /usr/share/wms_query_service/tasks
COPY app.py config.yml /usr/share/wms_query_service/
WORKDIR /usr/share/wms_query_service

# copies source over excluding files in .dockerignore
COPY wms_query_service /usr/share/wms_query_service/wms_query_service
COPY util /usr/share/wms_query_service/util
RUN chown -R oceansmap:oceansmap /usr/share/wms_query_service

COPY docker-support/scripts/build_oceansmap.sh ./
COPY docker-support/scripts/configure.sh ./
COPY docker-support/scripts/wait_for_redis.sh ./
COPY docker-support/scripts/start.sh /usr/share/wms_query_service/start.sh

# Allow users to host their own certificate and private keys
RUN mkdir /etc/certs
RUN mkdir /etc/oceansmap
VOLUME ["/etc/certs"]
VOLUME ["/etc/oceansmap"]
# keep logs from filling up container and degrading performance
VOLUME ["/var/log"]

# tell that we're exposing a listening port 3000
EXPOSE 3000


# run gunicorn.  Note that we use 0.0.0.0 as ip rather than localhost
CMD ["/bin/bash", "/usr/share/wms_query_service/start.sh"]
