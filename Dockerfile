FROM python:3.9.16

COPY src/ /opt/web-crawler/

ENTRYPOINT ["python", "-u", "src/main.py"]
CMD ["-h"]