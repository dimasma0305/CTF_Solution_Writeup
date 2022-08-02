git clone http://asdasd@venus.picoctf.net:53807/asdasd/aaa.git

git checkout --orphan newbranch
echo "asdasd" > access.conf
git add access.conf
git commit -m "Added a user to the repo"
git push origin @:refs/meta/config