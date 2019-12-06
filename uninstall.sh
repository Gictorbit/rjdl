#! /usr/bin/bash

if [ -d "$HOME/.local/share/rjdl" ]
then
    rm -rf "$HOME/.local/share/rjdl"
else
    echo "there is no cpaneltop directory in ~/.local/share"
fi

sudo unlink "/usr/local/bin/rjdl"
