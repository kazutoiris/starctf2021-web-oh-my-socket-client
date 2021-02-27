FROM python

COPY ./client /client
WORKDIR /client

RUN pip3 install -r requirements.txt && \
    chmod a+x start.sh

EXPOSE 5000

CMD ["./start.sh"]