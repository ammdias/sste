#!/usr/bin/env bash

DIR="`dirname \"$0\"`"
DIR="`( cd \"$DIR\" && pwd )`"
PROG="`basename \"$DIR\"`"
BIN="$HOME/.local/bin"
LIB="$HOME/.local/lib"
ICO="$HOME/.local/share/icons"
APP="$HOME/.local/share/applications"

mkdir -p "$BIN" "$LIB" "$ICO" "$APP"
cp -r "$DIR" "$LIB"

chmod +x "$LIB/$PROG/sste.py"

ln -sf "$LIB/$PROG/sste.py" "$BIN/sste"
ln -sf "$LIB/$PROG/sste.svg" "$ICO/sste.svg"
ln -sf "$LIB/$PROG/sste.desktop" "$APP/sste.desktop"
