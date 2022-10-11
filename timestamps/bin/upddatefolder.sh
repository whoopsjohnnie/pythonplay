#!/bin/sh

# set -x

upddatefolder()
{
	FOLDER=$1
	# echo "FOLDER $1"
	# cd $FOLDER
	# pwd
	# ls -alt $1
	LATESTFILE=`ls -Art $FOLDER | tail -n 1`
	# echo "LATEST FILE $LATESTFILE"
	# ls -alt ${FOLDER}/${LATESTFILE}
	if [ -f "${FOLDER}/${LATESTFILE}" ];
	then
		# echo "LATEST FILE IS FILE"
		echo "touch -r ${FOLDER}/${LATESTFILE} $FOLDER"
		touch -r "${FOLDER}/${LATESTFILE}" $FOLDER
	fi
	if [ -d "${FOLDER}/${LATESTFILE}" ];
	then
		# echo "LATEST FILE IS A FOLDER"
		echo "touch -r ${FOLDER}/${LATESTFILE} $FOLDER"
		touch -r "${FOLDER}/${LATESTFILE}" $FOLDER
	fi
}

# export -f upddatefolder

# find . -type d -newermt 20200101
# find . -type d -newermt 20200101 -exec sh -c 'upddatefolder "$0"' {} \;

#This loop will go to each immediate child and execute dir_command
find . -type d -newermt 20200101 | while read dir; do
	upddatefolder "$dir/"
done

