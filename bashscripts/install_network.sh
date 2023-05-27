sudo apt install linux-headers-generic build-essential dkms git

git clone -b 5.8.7.1_35809.20191129_COEX20191120-7777 https://github.com/cilynx/rtl88x2BU/

sudo dkms add ./rtl88x2BU

sudo dkms install -m rtl88x2bu -v 5.8.7.1

sudo modprobe 88x2bu

sudo apt install network-manager