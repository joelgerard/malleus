FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install lsb-release
RUN apt-get -y install curl

RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get -y install google-cloud-sdk-datastore-emulator

RUN gcloud config set project malleus-local

CMD ["gcloud","beta","emulators","datastore","start","--host-port","gdatastore:8081"]