FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:slim

RUN apt-get update && \
    apt-get install -y libengine-pkcs11-openssl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -s -L -o /tmp/libkmsp11.tgz https://github.com/GoogleCloudPlatform/kms-integrations/releases/download/v1.1/libkmsp11-1.1-linux-amd64.tar.gz && \
    cd /tmp && \
    tar -xopf /tmp/libkmsp11.tgz && \
    mv /tmp/libkmsp11-1.1-linux-amd64/libkmsp11.so /usr/local/lib/ && \
    mv /tmp/libkmsp11-1.1-linux-amd64/kmsp11.h /usr/local/include/ && \
    echo 'export PKCS11_MODULE_PATH="/usr/local/lib/libkmsp11.so"' | tee -a /etc/profile

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
CMD python3 /app/csrtool.py
