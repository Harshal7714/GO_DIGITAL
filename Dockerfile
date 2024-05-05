FROM python:3.8


RUN pip install boto3 pymysql


COPY python-Code.py /


CMD ["python", "/python-Code.py"]
