<br>

## UBUNTU

[Pruning](https://docs.docker.com/engine/manage-resources/pruning/)

```bash
docker system prune --volumes
```

<br>

## Dockerfile

This ``... clears out the local repository of retrieved package files'' via [advanced packaging tool (APT)](https://manpages.ubuntu.com/manpages/xenial/man8/apt-get.8.html)

```bash
apt clean
```

<br>

[How to Change Timezone in a Docker Container](https://www.baeldung.com/ops/docker-set-timezone)

```bash
ENV TZ=Europe/London
RUN apt clean && apt -q -y update && apt -q -y upgrade && \ 
    apt install -y tzdata && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && apt clean
```

<br>


## Container Image

```shell
jupyter lab --ip 0.0.0.0 --port 8888 --no-browser  --allow-root
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
