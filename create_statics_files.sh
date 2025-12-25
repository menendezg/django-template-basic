#!/bin/bash
# way to use
# ./create_statics_files.sh "create static"

COMMAND="$1"

case $COMMAND in
  "create static")
    echo "Creating static files and folders..."
    mkdir static
    mkdir static/css
    mkdir static/js
    mkdir static/images
    touch static/css/base.css
    touch static/js/base.js
    touch static/images/.keep
    ;;
  "create allauth files")
    echo "Creating allauth templates files..."
    mkdir templates/account
    ;;
  *)
    echo "Usage: $0 {create static|create allauth files}"
    exit 1
    ;;
esac