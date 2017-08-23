fn=$1
#reading the file name if not given with the input
if [ ! $fn ]; then
    echo "Enter input json file:"
    read filename
    fn=$filename
fi
#adding extension if not given
if ! grep -iq "\.json" <<<$fn; then
    fn=$fn".json"
fi
#Checking if file exists
if [ ! -e $fn ]; then
    echo "File $fn doesn't exist"
fi
if [ ! -r $fn ]; then
    echo "File $fn not readable"
fi
find="f"
replace=""
tmp=tmp_$fn
cp $fn $tmp
sed -i "s#{#$replace#g" $tmp
sed -i "s#}#$replace#g" $tmp
sed -i "s#Dependencies#$replace#g" $tmp
sed -i "s# = #$replace#g" $tmp
sed -i "s# #$replace#g" $tmp
sed -i "s#\"#$replace#g" $tmp
sed -i "s#\'#$replace#g" $tmp
sed -i "s#,#$replace#g" $tmp
errFile="error.txt"
tmpErrFile=tmp_$errFile
echo -n > $tmpErrFile
echo -n > $errFile
cat $tmp | while read LINE
do
    let count++
    if [ $LINE  ]; then
        #Installing by taking each line
        pip  install -Iv $LINE
        # echo $?
        if [ $? != "0" ]; then
            #Inserting to error log incase of any error
            echo $LINE, >> $tmpErrFile
        fi

    fi
done
sed -i "s# #$replace#g" $tmpErrFile
if [ -s $tmpErrFile ]; then
    echo "{" > $errFile
    cat $tmpErrFile >> $errFile
    #To remove final comma
    count=$(wc -l <$errFile)
    sed -i "$count s#,##" $errFile
    echo "}" >> $errFile
else
    #Printing success if no errors
    echo "SUCCESS"
fi
# list=cat $fn
#removing the temporary files created
rm -f $tmpErrFile
rm -f $tmp