#! /usr/bin/bash

echo "creating rjdl directory in ~/.locale/share/ ..."
mkdir -p "$HOME/.local/share/rjdl"

echo "copy all files directory to rjdl directory ..."
dir=$(pwd)
cp -rv "$dir/radiojavan-dl.py" "$HOME/.local/share/rjdl"

chmod +x "$HOME/.local/share/rjdl/radiojavan-dl.py"

echo "make symbolic link for radiojavan-dl.py"
sudo ln -s "$HOME/.local/share/rjdl/radiojavan-dl.py" "/usr/local/bin/rjdl"

sudo pip install -r requirements.txt