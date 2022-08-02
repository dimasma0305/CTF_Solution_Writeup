poly='x^318 + x^313 + x^312 + x^310 + x^308 + x^306 + x^302 + x^298 + x^297 + x^294 + x^292 + x^289 + x^286 + x^285 + x^284 + x^283 + x^281 + x^280 + x^278 + x^277 + x^274 + x^273 + x^269 + x^268 + x^264 + x^262 + x^261 + x^259 + x^258 + x^257 + x^253 + x^252 + x^248 + x^246 + x^245 + x^244 + x^242 + x^237 + x^236 + x^233 + x^232 + x^230 + x^228 + x^227 + x^226 + x^225 + x^224 + x^222 + x^221 + x^218 + x^217 + x^213 + x^212 + x^208 + x^205 + x^204 + x^201 + x^200 + x^198 + x^197 + x^195 + x^194 + x^190 + x^189 + x^186 + x^182 + x^180 + x^179 + x^178 + x^177 + x^176 + x^173 + x^172 + x^170 + x^166 + x^165 + x^164 + x^161 + x^158 + x^157 + x^155 + x^152 + x^150 + x^149 + x^148 + x^146 + x^142 + x^141 + x^139 + x^134 + x^133 + x^131 + x^130 + x^128 + x^125 + x^124 + x^121 + x^120 + x^118 + x^117 + x^116 + x^114 + x^109 + x^108 + x^104 + x^102 + x^101 + x^97 + x^96 + x^94 + x^92 + x^91 + x^90 + x^89 + x^88 + x^85 + x^84 + x^80 + x^78 + x^77 + x^76 + x^73 + x^72 + x^70 + x^68 + x^67 + x^66 + x^65 + x^64 + x^61 + x^60 + x^58 + x^54 + x^53 + x^51 + x^50 + x^48 + x^45 + x^44 + x^42 + x^38 + x^37 + x^36 + x^35 + x^33 + x^29 + x^28 + x^24 + x^22 + x^21 + x^19 + x^18 + x^17 + x^14 + x^13 + x^10 + x^9 + x^8 + x^6 + x^5 + x^4 + x^3 + x^2 + 1'
# make x^n into n
poly=poly.replace('x^','')
poly=poly.replace(' ','')
#poly seperate by +
poly=poly.split('+')
#make poly int list
poly=[int(i) for i in poly]
#print(poly)
bin_poly=[]
for i in range(0,max(poly)):
    if i in poly:
        #append 1 to bin poly
        bin_poly.append(1)
    elif i == 0:
        bin_poly.append(1)
    else:
        #append 0 to bin poly
        bin_poly.append(0)
#make bin poly reversed
bin_poly=bin_poly[::-1]
#make bin poly merged
bin_poly=''.join(str(i) for i in bin_poly)
#make poly become int list
bin_poly=[int(i) for i in bin_poly]
#remove bin_poly[0]
bin_poly=bin_poly[1:]
bin_poly=bin_poly[1:]
bin_poly=bin_poly[1:]
bin_poly=bin_poly[1:]
bin_poly=bin_poly[1:]
bin_poly=bin_poly[1:]

#merge bin_poly
bin_poly=''.join(str(i) for i in bin_poly)
print(bin_poly)