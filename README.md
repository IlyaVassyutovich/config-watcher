# Config Watcher

TBD

```bash
docker run \
    --rm \
    --mount type=bind,src=/tmp/configs/running-config/qBittorrent/qBittorrent.conf,dst=/configs/running-config,readonly=true \
    --mount type=bind,src=/tmp/configs/controlled-config/qBittorrent.conf,dst=/configs/controlled-config,readonly=false \
        config-watcher:latest \
            --running-config /configs/running-config \
            --controlled-config /configs/controlled-config \
            --verbose
```
