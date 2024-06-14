FROM condaforge/mambaforge
RUN mkdir /app
WORKDIR /app
COPY index.html /app/index.html
COPY app.py /app/app.py
COPY geo.json /app/geo.json
COPY pic_geo.json /app/pic_geo.json
COPY test.json /app/test.json
COPY test1.json /app/test1.json
CMD ["python", "/app/app.py"]
EXPOSE 8000