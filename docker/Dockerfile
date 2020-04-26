FROM osrf/ros:melodic-desktop-full-bionic

# install packages
RUN apt-get update && apt-get install -q -y --no-install-recommends \
    build-essential \
    curl \
    cmake \
    imagemagick \
    libboost-all-dev \
    libgts-dev \
    libjansson-dev \
    libtinyxml-dev \
    mercurial \
    pkg-config \
    psmisc \
    xvfb \
    && rm -rf /var/lib/apt/lists/*
# install nodejs 
RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install -y nodejs
# install gazebo packages
RUN apt-get update && apt-get install -q -y --no-install-recommends \
    libgazebo9-dev \
    && rm -rf /var/lib/apt/lists/*
    

# clone gzweb
ENV GZWEB_WS /root/gzweb
RUN hg clone https://bitbucket.org/osrf/gzweb $GZWEB_WS
WORKDIR $GZWEB_WS

# build gzweb
RUN hg up default \
    && xvfb-run -s "-screen 0 1280x1024x24" ./deploy.sh -m -t

# setup environment
EXPOSE 8080
EXPOSE 7681

# run gzserver and gzweb
CMD gzserver --verbose & npm start
