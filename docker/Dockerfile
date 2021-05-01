# Ubuntu 20.04 with Java 8 installed.
# Build image with:  docker build -t rbonifacio/mcsl-java8:v2 .

FROM ubuntu:20.04
MAINTAINER Rodrigo Bonifacio, https://github.com/rbonifacio
RUN apt-get update               && \
    apt install -y openjdk-8-jdk && \
    apt-get install -y git       && \
    apt-get install -y wget      && \
    apt-get install -y cloc      && \
    apt-get clean                && \
    mkdir /mcsl


RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -t robbyrussell

WORKDIR /mcsl

RUN git config --global user.email "rbonifacio123@gmail.com" && \    
    git config --global user.name "rbonifacio"               && \              
    git clone https://github.com/CROSSINGTUD/MetaCrySL.git && \
    cd MetaCrySL                                           && \
    git fetch --all                                        && \
    git checkout -b docker                                 && \
    git pull origin docker                                 && \ 
    cd ..                                                  && \
    wget https://update.rascal-mpl.org/console/rascal-shell-stable.jar && \
    echo "alias rascal-shell='java -Xmx1G -Xss32m -jar /mcsl/rascal-shell-stable.jar'" >> ~/.zshrc && \
    echo "alias cloc1='cloc --skip-uniqueness --read-lang-def=/mcsl/mcsl_cloc_def.txt'" >> ~/.zshrc && \
    echo "alias cloc2='cloc --read-lang-def=/mcsl/mcsl_cloc_def.txt'" >> ~/.zshrc && zsh

COPY mcsl_cloc_def.txt /mcsl

CMD ["zsh"]