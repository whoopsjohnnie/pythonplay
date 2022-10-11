#!/bin/sh

# set -x

upddatetimestamps()
{
	CWD="$(pwd)"
	FILE=$1
	FOLDER="$(dirname "$1")"
	echo "FILE $FILE"
	echo "FOLDER $FOLDER"
	cd $FOLDER
	pwd
	ls -al 
	ls -al ./timestamps
	cat ./timestamps
	echo "python3.8 ~/Documents/development/jsondecode/timestamps.py ./timestamps"
	python3.8 ~/Documents/development/jsondecode/timestamps.py ./timestamps
	ls -al
	cd $CWD
	pwd
}

# export -f upddatefolder

# find . -type d -newermt 20200101
# find . -type d -newermt 20200101 -exec sh -c 'upddatefolder "$0"' {} \;

#This loop will go to each immediate child and execute dir_command
find . -type f -name "timestamps" | while read file; do
	upddatetimestamps "$file"
done

