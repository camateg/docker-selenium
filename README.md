# selenium-test

This Docker image will test Google's image search for pictures of robots and ensure that at least one exist(s).  It uses Google Chrome via a headless Ubuntu X session and reports the results via unittest.

Usage:

    git clone https://github.com/camateg/docker-selenium.git
    cd selenium-test
    docker build .
    docker run run --security-opt seccomp:chrome.json -ti <id>
