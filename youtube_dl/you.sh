#!/usr/bin/bash 

PYTHON_PATH=/cygdrive/c/Python37/python
PIP=/cygdrive/c/Python37/Scripts/pip

function usage() {
    echo "you.sh <name> <url> [mp3]"
    echo "    <name> = name to save"
    echo "    <url> = url"
    echo "    [mp3] = optional convert to mp3"
    exit
}

[ $1 ] && [ $2 ] || usage

case $1 in
    version) 
        echo version
        env PATH=$PYTHON_PATH:/bin /cygdrive/c/Python37/Scripts/youtube-dl --version
        ;;
    update) 
        echo update
        env PATH=$PYTHON_PATH:/bin /cygdrive/c/Python37/Scripts/pip install --upgrade youtube-dl
        ;;
    *)
        echo downloading
        env PATH=$PYTHON_PATH:/bin /cygdrive/c/Python37/Scripts/youtube-dl --no-check-certificate -o $1 $2
        [ $3 ] && [ $3 == mp3 ] && ffmpeg -i $1 -vn -ar 44100 -ac 2 -b:a 192k $1.mp3 # && cp $1.mp3 /cygdrive/g
        ;;
esac

