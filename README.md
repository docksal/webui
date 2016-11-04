# Docksal Web UI
Web UI for Docksal

```
docker run -d --name webui --label "io.docksal.group=system" --label "io.docksal.virtual-host=webui.docksal" --env "VIRTUAL_HOST=webui.docksal" --restart=always --privileged --userns=host -v /:/rootfs:ro -v /var/run:/var/run:rw -v /sys:/sys:ro -v /var/lib/docker/:/var/lib/docker:ro --expose 80 --expose 443 docksal/webui
```
