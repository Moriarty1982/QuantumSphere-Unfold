FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    ghostscript \
    latexmk \
    poppler-utils \
    python3 \
    texlive-bibtex-extra \
    texlive-extra-utils \
    texlive-fonts-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-latex-recommended \
    texlive-pictures \
    texlive-science \
    zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
