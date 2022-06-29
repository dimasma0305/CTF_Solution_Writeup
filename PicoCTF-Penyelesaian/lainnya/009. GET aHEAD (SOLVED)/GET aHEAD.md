# GET aHEAD

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:21939/](http://mercury.picoctf.net:21939/)

## Hints

1.  Maybe you have more than 2 choices
    
2.  Check out tools like Burpsuite to modify your requests and look at the responses

## Solving
Kita lihat element dari websitenya  menggunakan Developer Tools di chrome, terlihat output seperti berikut:

	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red">
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue">
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
	
bisa dilihat bahwa "Red" bermethod "GET" sedangkan "Blue" bermethod "POST". Dilihat dari hint yang di berikan bisa ada lebih dari 2 method yang dapat digunakan, kita akan menggunakan method "HEAD" karena judulnya "GET aHEAD" memberikan kita hint bahwa method ketiga adalah HEAD.

### Menggunakan Burpsuite
Buka Burpsuite lalu ke Proxy
![](CTF/PicoCTF-Penyelesaian/lainnya/009.%20GET%20aHEAD%20(SOLVED)/Screenshot%20from%202021-12-11%2011-02-28.png)
pastikan "intercept on", open browser lalu masukkan link http://mercury.picoctf.net:21939/index.php? ke searchbar.
![](CTF/PicoCTF-Penyelesaian/lainnya/009.%20GET%20aHEAD%20(SOLVED)/Screenshot%20from%202021-12-11%2011-14-14.png)
Setelah itu kita ubah method menjadi HEAD seperti gambar di atas

kemudian kita masukk lagi ke browser disitu kita buka developer tools 
![](CTF/PicoCTF-Penyelesaian/lainnya/009.%20GET%20aHEAD%20(SOLVED)/Screenshot%20from%202021-12-11%2011-20-15.png)
lalu masukke panel network, cari index.php lalu respone header, disana terletak CTF-nya.
### Menggunakan Postman
>Postman bisa di download sebagai extensi di Chrome Store

menggunakan postman kita perlu membuat folder terlebih dahulu, setelah di menu utama kita masukka url tadi ke "enter request url" lalu ubah methodnya menjadi HEAD.
setelah itu kita masuk ke bagaian header yang ada di bawahnya.
![](CTF/PicoCTF-Penyelesaian/lainnya/009.%20GET%20aHEAD%20(SOLVED)/Screenshot%20from%202021-12-11%2011-26-41.png)
### Menggunakan curl
Ketik di terminal:
>curl -I HEAD -i http://mercury.picoctf.net:21939
## Flag
picoCTF{r3j3ct_th3_du4l1ty_.......}

## Referensi
https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/f06a4b377dad2238b33c9f5fcb038333ed815bde/Web%20Exploitation/Get%20aHead/Get%20aHead.md
