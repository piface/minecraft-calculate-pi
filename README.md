Make sure you have installed the minecraft python api from here: http://www.raspberrypi-spy.co.uk/2013/10/how-to-setup-minecraft-on-the-raspberry-pi/
(in short)
wget https://s3.amazonaws.com/assets.minecraft.net/pi/minecraft-pi-0.1.1.tar.gz
tar -zxvf minecraft-pi-0.1.1.tar.gz
mkdir ~/mcpi-api
cp -r ~/mcpi/api/python/mcpi ~/mcpi-api/

For quick testing:

Start minecraft
cd mcpi
./minecraft-pi


python monte_carlo.py


