#/bin/bash

if [ -z "$1" ];then
    lastFileName=`ls -1 -v|tail -1|awk -F . '{print $1}'`
    lastNum=`echo $lastFileName|tr -dc '[0-9]'`
else
    lastNum=`printf '%04d' $1`
    lastFileName="test${lastNum}"
fi

d=10
if [ -n "$2" ];then
    d="$2"
fi

nextNum=`echo "$lastNum $d"|awk '{printf "%04d", $1 + $2}'`

echo $lastFileName, $lastNum, $nextNum

cat "${lastFileName}.py" | sed -e "s/Test${lastNum}/Test${nextNum}/g" > "test${nextNum}.py"
cp "${lastFileName}.kv" "test${nextNum}.kv"
