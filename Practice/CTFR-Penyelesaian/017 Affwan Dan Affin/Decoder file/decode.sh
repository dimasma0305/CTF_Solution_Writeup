for i in {3000..4000}
do
    python3 decode.py $i >> decode.txt
    echo "Decode $i\n" >> decode.txt
done