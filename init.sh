#!/usr/bin/env bash
phantomjs_exist=`ls | grep phantomjs | wc -c`
chrome_exist=`ls | grep chrome | wc -c`
source ./venv/bin/activate
pip freeze > requirements.txt
if [ $phantomjs_exist -gt 0 ];then
    echo 'phantomjs exist'
else
    echo 'phantomjs not exist'
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    unzip ./phantomjs-2.1.1-macosx.zip
    rm -rf ./phantomjs-2.1.1-macosx.zip
    tar -xvf ./phantomjs-2.1.1-linux-x86_64.tar.bz2
    rm -rf ./phantomjs-2.1.1-linux-x86_64.tar.bz2
fi

if [ $chrome_exist -gt 0 ];then
    echo 'chrome exist'
else
    echo 'chrome not exist'
    wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip
    wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
    unzip ./chromedriver_mac64.zip
    rm -rf ./chromedriver_mac64.zip
    mv chromedriver chromedriver_mac64
    unzip ./chromedriver_linux64.zip
    rm -rf ./chromedriver_linux64.zip
    mv chromedriver chromedriver_linux64
fi

