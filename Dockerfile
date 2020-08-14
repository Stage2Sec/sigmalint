FROM python:3.8-alpine
RUN pip install --upgrade pip

RUN adduser -D sigmalint
USER sigmalint
WORKDIR /home/sigmalint

COPY --chown=sigmalint:sigmalint requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/sigmalint/.local/bin:${PATH}"

COPY --chown=sigmalint:sigmalint . .
RUN pip install --user .

WORKDIR /rules
ENTRYPOINT [ "sigmalint", "--inputdir", ".", "--method" ]
CMD [ "s2" ]