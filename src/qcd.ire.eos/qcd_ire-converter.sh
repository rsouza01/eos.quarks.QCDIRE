#!/bin/bash



echo "=============================================================================================="
echo "Converting QCD IRE Tables..."
echo "=============================================================================================="


for _FILE_NAME in ../eos/*.dat; do 

    full_filename=$(basename "$_FILE_NAME")
    extension="${full_filename##*.}"
    filename="${full_filename%.*}"

    output=../eos.conv/${filename}.CGS.csv

    echo "Converting '${full_filename}' to '${output}'..."

    tac $_FILE_NAME | ./qcd_ire-converter.py > ${output}

done

echo "=============================================================================================="
echo "Done!"
echo "=============================================================================================="
