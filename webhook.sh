#!/bin/bash

project=$1
origin_branch=$2
local_branch=$3

echo $project, $origin_branch, $local_branch

cd /autodeploy/$project

command="/usr/bin/git branch"

/usr/bin/git fetch --all

/usr/bin/git checkout .

if [[ $(${command} | /usr/bin/grep $local_branch) ]]
then
        git checkout $local_branch
        git pull
else
        git checkout origin/$origin_branch  -b $local_branch
        git pull
fi

