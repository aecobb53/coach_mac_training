FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY coach_mac_training coach_mac_training
COPY entrypoint.sh .
COPY info.json .
COPY favicon.ico .


COPY favicon.png .

COPY Coach-Mac-Training-Emblem.ico .
COPY Coach-Mac-Training-Emblem.png .

# COPY . .

ENTRYPOINT [ "bash", "entrypoint.sh" ]
