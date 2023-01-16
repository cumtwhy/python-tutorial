#!/bin/bash

echo "all start ..."
rootdir=$(pwd)
currentDirs=($(find . -maxdepth 3 -type d -print | grep .git$))
echo "repo count: ${#currentDirs[*]}"

for i in "${currentDirs[@]}"; do
  cd $rootdir/$i
  cd ..
  echo -e "[repo: ${PWD##*/}] git pull \n" $(git pull) "\n" & # >/dev/null 2>&1
done

read -n 100
