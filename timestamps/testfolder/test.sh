#!/bin/sh

rm -f ./CXterm
rm -f ./3ddimple.xpm
rm -f ./3dfeet.xpm
rm -f ./3dpaint.xpm
rm -rf ./Mail

touch ./CXterm
touch ./3ddimple.xpm
touch ./3dfeet.xpm
touch ./3dpaint.xpm
mkdir ./Mail

ls -al ./CXterm
ls -al ./3ddimple.xpm
ls -al ./3dfeet.xpm
ls -al ./3dpaint.xpm
ls -al ./Mail

echo "parsing timestamps1.txt"
python ../timestamps.py ./timestamps1.txt 

ls -al --full-time ./CXterm
ls -al --full-time ./3ddimple.xpm
ls -al --full-time ./3dfeet.xpm
ls -al --full-time ./3dpaint.xpm
ls -al --full-time ./Mail

echo "parsing timestamps2.txt"
python ../timestamps.py ./timestamps2.txt 

ls -al --full-time ./CXterm
ls -al --full-time ./3ddimple.xpm
ls -al --full-time ./3dfeet.xpm
ls -al --full-time ./3dpaint.xpm
ls -al --full-time ./Mail

echo "parsing timestamps3.txt"
python ../timestamps.py ./timestamps3.txt 

ls -al --full-time ./CXterm
ls -al --full-time ./3ddimple.xpm
ls -al --full-time ./3dfeet.xpm
ls -al --full-time ./3dpaint.xpm
ls -al --full-time ./Mail

echo "parsing timestamps4.txt"
python ../timestamps.py ./timestamps4.txt 

ls -al --full-time ./CXterm
ls -al --full-time ./3ddimple.xpm
ls -al --full-time ./3dfeet.xpm
ls -al --full-time ./3dpaint.xpm
ls -al --full-time ./Mail

echo "parsing timestamps5.txt"
python ../timestamps.py ./timestamps5.txt 

ls -al --full-time ./CXterm
ls -al --full-time ./3ddimple.xpm
ls -al --full-time ./3dfeet.xpm
ls -al --full-time ./3dpaint.xpm
ls -al --full-time ./Mail
