var_skrip="cat somuchdasar64.txt | base64"
for a in {1..7}
do
    eval $var_skrip > decode/decode$a.txt
    var_skrip="$var_skrip | base64 -d"
done
var_skrip="cat decode/decode6.txt | xxd -r -p"
for a in {1..5}
do
    eval $var_skrip > decode2/decode$a.txt
    var_skrip="$var_skrip | base64 -d"
done
var_skrip="cat decode2/decode5.txt | xxd -r -p"
for a in {1..5}
do
    eval $var_skrip > decode3/decode$a.txt
    var_skrip="$var_skrip | base64 -d"
done
var_skrip="cat decode3/decode5.txt | xxd -r -p"
for a in {1..5}
do
    eval $var_skrip > decode4/decode$a.txt
    var_skrip="$var_skrip | base64 -d"
done
var_skrip="cat decode4/decode5.txt | xxd -r -p"
for a in {1..5}
do
    eval $var_skrip > decode5/decode$a.txt
    var_skrip="$var_skrip | base64 -d"
done
var_skrip="cat decode5/decode5.txt | xxd -r -p"
eval $var_skrip