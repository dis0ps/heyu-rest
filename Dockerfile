FROM python:3-slim-buster

RUN useradd -G dialout heyu && mkdir -p /home/heyu/app && chown -R heyu.heyu /home/heyu

RUN mkdir -p /usr/local/etc/heyu && echo "TTY /dev/ttyUSB0" > /usr/local/etc/heyu/x10.conf
RUN mkdir -p  /usr/local/var/tmp/heyu && mkdir -p /usr/local/var/lock

RUN chown heyu.heyu /usr/local/var/tmp/heyu /usr/local/var/lock usr/local/etc/heyu

COPY ./heyu_bin/heyu /usr/local/bin
ENV HEYU_PATH="/usr/local/bin/heyu"

WORKDIR /home/heyu/app
COPY ./requirements.txt /home/heyu/app
RUN pip install -r /home/heyu/app/requirements.txt
ENV PATH="/home/heyu/.local/bin:${PATH}"
COPY ./*.py /home/heyu/app/

EXPOSE 8080

USER heyu

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app" ]
