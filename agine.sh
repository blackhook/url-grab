filename=$(date +%Y%m%d-%H-%m-%S)
cp in.txt ./bak/$filename.txt
mv -f ./ok/ok.txt in.txt
python url.py