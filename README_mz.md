export FISHROS_URL=http://192.168.18.1:5500

mkdir -p /tmp/fishinstall/tools/translation/assets
cd /tmp/fishinstall
wget $FISHROS_URL/install.py  && python3  install.py