for file in *.nex; 
do 
sed '1,19d' $file > no_para/$file; 
done