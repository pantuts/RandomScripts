#!/bin/bash
# for macOS only
# save then run
# chmod +x install-update-atom.sh

COMMAND=$1

if ! [ "$#" -eq 1 ]; then
    echo "Usage: ./install-update-atom.sh [install || update]"
    exit
fi

NOW=$(date +'%Y-%m-%d_%H-%M-%S')
TMP_FOLDER=/tmp/atom-$NOW
FILENAME=$TMP_FOLDER/atom-mac.zip
mkdir -p $TMP_FOLDER

download () {
    wget "$LATEST_DOWNLOAD_URL/atom-mac.zip" -O $FILENAME
}

installAtom () {
    unzip $FILENAME -d $TMP_FOLDER
    cp -rf $TMP_FOLDER/Atom.app /Applications
    ln -sf /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom
    atom --version
}

getLatestVersion () {
    echo "Querying latest version..."
    LATEST_DOWNLOAD_URL=$(python -c "import requests;print(requests.get('https://github.com/atom/atom/releases/latest').url)" | sed 's/tag/download/')
    LATEST_DOWNLOAD_VERSION=$(echo $LATEST_DOWNLOAD_URL | cut -d '/' -f 8 | sed 's/v//')
}

getCurrentVersion () {
   CURRENT_VERSION=$(atom --version | grep Atom | cut -d ':' -f 2 | awk '{$1=$1};1')
}

if [ $COMMAND == 'install' ]; then
    if [ -x "$(command -v atom)" ]; then
        getCurrentVersion
        echo "You currently have Atom version $CURRENT_VERSION"
        exit
    fi
    getLatestVersion
    download
    installAtom
elif [ "$COMMAND" == "update" ]; then
    if ! [ -x "$(command -v atom)" ]; then
        echo "You sure you have atom installed?"
        echo "If yes then do this first: ln -sf /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom"
        exit
    fi
    getLatestVersion
    getCurrentVersion
    if [ "$LATEST_DOWNLOAD_VERSION" == "$CURRENT_VERSION" ]; then
        echo "Update not needed."
        exit
    fi
    download
    installAtom
else
    echo 'What?!'
    exit
fi

echo "Done"
exit

