# sha didapat dari konversi "PRITCHARD" ke sha256
sha = "496e54f222f256b023f33cdda0270853f39d7bf24fa1ca6b72d4b4fd1a9cae56"
# nomor 4, 5, 6, dan seterusnya diperoleh dari "hexdigest()" di function "check_key"
print(sha[4] + sha[5] + sha[3] + sha[6] + sha[2] + sha[7] + sha[1] + sha[8])