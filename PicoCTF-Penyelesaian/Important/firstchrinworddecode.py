from colorsys import TWO_THIRD


code_var = "Charlie Tango Foxtrot Romeo { Sierra One Mike Papa Lima Three _ Four Lima Papa Hotel Four Bravo Three Tango }"
name = {
    "One"     : '1',
    "Two"     : '2',
    "Three"   : '3',
    "Four"    : '4',
    "Five"    : '5',

}
'''
name2 = {
    "1"     : 'One',
    "2"     : 'Two',
    "3"   : 'Three',
    "4"    : 'Four',
    "5"    : 'Five',
}
'''
name3 = {"One":"One","Two":"Two","Three":"Three","Four":"Four","Five":"Five"}

output = ""
for w in code_var.split(' '):
    if w == name3.get(w):
        output = output + name.get(w,w)
    else:
        output = output + w.lower()[0]

print(output)
'''
    if a == name.get(a, a):
        print(name.get(a, a))
    else:
        print(a[0])
'''