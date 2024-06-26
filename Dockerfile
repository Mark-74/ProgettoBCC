FROM python:3.11.8-alpine

COPY requirements.txt .
RUN apk update
RUN apk add pkgconfig
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev npm
RUN pip install --no-cache-dir -r requirements.txt

COPY src /src
COPY tailwind.config.js /src
WORKDIR /src
RUN mkdir logs

RUN npm install -D tailwindcss
RUN npx tailwindcss -i ./static/css/input.css -o ./static/css/tailwind.css

CMD ["python", "__init__.py"]
