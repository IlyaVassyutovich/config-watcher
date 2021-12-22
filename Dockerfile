FROM python:3-alpine


LABEL org.opencontainers.image.authors="Ilya Vassyutovich <B3986DFC895D503C395A704D39FD100DF9D03E17>"
LABEL org.opencontainers.image.source="https://github.com/IlyaVassyutovich/config-watcher"
LABEL org.opencontainers.image.url="https://github.com/IlyaVassyutovich/config-watcher"


WORKDIR /app

COPY src/ .


ENTRYPOINT [ "python3", "-m", "main" ]
CMD [ "--running-config", "/configs/running-config", "--controlled-config", "/configs/controlled-config" ]
