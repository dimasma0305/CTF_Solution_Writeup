import hashlib

flag = "C"
dino = open("Dino.jpg", "r").read()

def calc(x):
	res = 0
	for i in x: res += ord(i)
	return res

def hexConv(x):
	res = ""
	for i in x:
		res += hex(ord(i)).replace("0x", "")
	return int(res, 16)

# 1192ba00ff....................
def getMd5():
	md5 = hashlib.md5()
	d = open("Dino.jpg", "r").read()
	md5.update(d)
	return md5.hexdigest()

def getSign():
	return dino[0: 4]

# 14591788 - (10 ** 5 - 7725 + 65537 + (~80) + (462210 / 2))
def getSize():
	# Hidden somewhere
	a=14591788 - (10 ** 5 - 7725 + 65537 + (~80) + (462210 / 2))
	a=a
	return a

def getWave():
	return "-123123"

def cry(c, t, f, r):
	res = []
	for x in flag:
		res.append((432702721765807 * ord(x)))
	return res
encrypted = cry(int(hexConv(getSign())), int(hexConv(str(getSize()))), int(hexConv(getWave())), int(hexConv(getMd5())))
print "Wave: " + str(hexConv(str(getWave())))
print "Size: " + str(getSize())
print "Sign: " + str(hexConv(getSign()))
print "Md5: " + str(hexConv(getMd5()) >> 0xCD) 


print(encrypted)
print(len("237580212311373812586L"))
print(len("28991082358309069L"))

# flag = [28991082358309069L, 36347028628327788L, 30289190523606490L, 35481623184796174L, 53222434777194261L, 43270272176580700L, 21202433366524543L, 47597299394238770L, 20769730644758736L, 49760813003067805L, 20769730644758736L, 50626218446599419L, 49328110281301998L, 50626218446599419L, 22933244253587771L, 41106758567751665L, 47597299394238770L, 52357029333662647L, 22500541531821964L, 41106758567751665L, 46731893950707156L, 22500541531821964L, 44568380341878121L, 21202433366524543L, 41106758567751665L, 47597299394238770L, 24664055140650999L, 22067838810056157L, 45866488507175542L, 22500541531821964L, 49328110281301998L, 41106758567751665L, 42404866733049086L, 50626218446599419L, 49328110281301998L, 50626218446599419L, 47597299394238770L, 24664055140650999L, 41106758567751665L, 45001083063643928L, 22067838810056157L, 45001083063643928L, 22067838810056157L, 54087840220725875L]