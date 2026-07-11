#!/data/data/com.termux/files/usr/bin/bash

echo "Installing WASI AL OS..."

pkg update -y
pkg install wget -y

APK="WASI_AL_OS_Termux_v1.5.apk"

if [ -f "$APK" ]; then
    echo "APK already exists."
else
    wget -O "$APK" https://github.com/WasiaL007/WasiaL007/releases/download/v1.5/WASI_AL_OS_Termux_v1.5.apk
fi

echo "Download Complete!"
echo "Opening WASI AL OS installer..."

am start -a android.intent.action.VIEW -d file://$PWD/$APK -t application/vnd.android.package-archive
