#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

rm -rf dist/
rm -rf *.egg-info/
python3.4 setup.py sdist
cd dist/
tar -xvzf $(ls | grep giwyn)
rm *.tar.gz
cd $(ls | grep giwyn)
sudo python3.4 setup.py install

