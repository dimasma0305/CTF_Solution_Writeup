1.  Yeah, it's a boolean blind SQL injection attack, which is binary-searching its way to the correct character. So it's a matter of starting with every letter as a candidate, then rejecting those that are larger/smaller than the limit in the query. You should be left with only one possibility for each char, provided you picked the correct length for the "true" and "false" answers. (edited)
    
2.  _[_4:06 PM_]_
    
    It's essentially what SQLmap and friends do. Instead of asking `substring(password, 1, 1) = 'a'`, then 'b', 'c' etc. you can ask `substring(password, 1, 1) <= 'm'` and rule out half the candidates in one guess
    
3.  _[_4:07 PM_]_
    
    Reducing it from `(len(printable)/2) * len(password)` queries on average, to a maximum of `log2(len(printable)) * len(password)` queries

