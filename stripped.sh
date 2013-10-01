for file in *.nex; 
do 
sed '1,18d' $file > stripped/$file; 
done