filename=$(date +%Y%m%d-%H-%m-%S)
cp ./ok/fulldomain.txt ./bak/$filename_fulldomain.txt
cp ./ok/fullpath.txt ./bak/$filename_fullpath.txt
rm -rf ./ok/fullpath.txt
mv -f ./ok/ok.txt in.txt
python url.py