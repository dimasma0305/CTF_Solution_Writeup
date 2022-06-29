# Krypton Level 0 → Level 1
```sh
echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d
# Password: KRYPTONISGREAT
```
# Krypton Level 1 → Level 2
```sh
ssh krypton1@krypton.labs.overthewire.org -p 2231
# Password: KRYPTONISGREAT
cd /krypton/krypton1
cat krypton2 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# Nextpass: ROTTEN
```
# Krypton Level 2 → Level 3
```sh
ssh krypton2@krypton.labs.overthewire.org -p 2231
# Password: ROTTEN
cd /krypton/krypton2
```
Decode with Python
```python
# caesar chiper decoder +14
Decode ="OMQEMDUEQMEK"
Ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(Decode)):
    print(Ascii[(Ascii.index(Decode[i])+14)%26], end="")
```

```
# Nextpass: CAESARISEASY
```
# Krypton Level 3 → Level 4
```sh
ssh krypton3@krypton.labs.overthewire.org -p 2231
# Password: CAESARISEASY
cd /krypton/krypton3
# use: https://quipqiup.com/
# Nextpass: BRUTE
```
# Krypton Level 4 → Level 5
```sh
ssh krypton4@krypton.labs.overthewire.org -p 2231
# Password: BRUTE
cd /krypton/krypton4
# Use: https://www.dcode.fr/vigenere-cipher
# Nextpass: CLEARTEXT
```
# Krypton Level 5 → Level 6
```sh
ssh krypton5@krypton.labs.overthewire.org -p 2231
# Password: CLEARTEXT
cd /krypton/krypton5
# Use: https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx
# Key: keylength
# Nextpass: RANDOM
```
# Krypton Level 6 → Level 7
```sh
ssh krypton6@krypton.labs.overthewire.org -p 2231
# Password: RANDOM
cd /krypton/krypton6
```
- Plaintext: SINGOGODDESSTHEANGEROFACHILLESSONOFPELEUSTHATBROUGHTCOUNTLESSILLSUPONTHEACHAEANSMANYABRAVESOULDIDITSENDHURRYINGDOWNTOHADESANDMANYAHERODIDITYIELDAPREYTODOGSANDVULTURESFORSOWERETHECOUNSELSOFJOVEFULFILLEDFROMTHEDAYONWHICHTHESONOFATREUSKINGOFMENANDGREATACHILL
- Key: ITWASTHEBESTOFTIMESITWASTHEWORSTOFTIMESITWASTHEAGEOFWISDOMITWASTHEAGEOFFOOLISHNESSITWASTHEEPOCHOFBELIEFITWASTHEEPOCHOFINCREDULITYITWASTHESEASONOFLIGHTITWASTHESEASONOFDARKNESSITWASTHESPRINGOFHOPEITWASTHEWINTEROFDESPAIRWEHADEVERYTHINGBEFOREUSWEHADNOTHINGBEF
- Chiper: ABJGGZVHEIKLHMXIZKWZHBAUAPPHSJKHBTYXQPWCLPHSMIVOAKVYYWMQHXMLOIDEZYPURHMJOQSIWHAWESVRWBJTCIWDINKWIJXDMRIPNNRQBUKHDKPACMIQGJEQXXIGWIAARGWPHAXYASYRFAZKFMWWKGKTUHNYLLIESXIOICBAWJMMDEUHBRKTCABLXTCSUYTYELDXKJNWZMLVRFBSFLHQTDXOEVSISWYMYMHYLMSUFJGWJEUDJESTAIPNJPQ
```sh
python3 -c "print('A'*100)" >> /tmp/testcipher
./encrypt6 /tmp/testcipher /tmp/testcipher2
cat /tmp/testcipher2
```
Output:
```
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZ
```

```sh
# Pola: EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
```

```python
# vigenere decoder
crypt = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
ciphertext = "PNUKLYLWRQKGKBE"

for i in range(len(ciphertext)):
    k = ord(ciphertext[i]) - ord(crypt[i])
    if k < 0: k += 26
    k += ord('A')
    print(chr(k), end='')
```

```sh
# Nextpass: LFSRISNOTRANDOM
```
# Krypton Level 7
```sh
ssh krypton7@krypton.labs.overthewire.org -p 2231
# Password: LFSRISNOTRANDOM
```
