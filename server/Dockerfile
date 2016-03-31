FROM jgkamat/netcat

ADD src/* /

RUN chmod 755 /server-app

EXPOSE 4242

ENTRYPOINT [ "/server-app" ]

