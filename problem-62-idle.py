Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cubes(maxn=1000):
	return set(map(int(3).__rpow__,range(1,maxn+1)))

>>> cubes(10)
{64, 1, 512, 8, 1000, 343, 216, 729, 27, 125}
>>> sorted(cubes(10))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> 8**3
512
>>> 9**3
729
>>> from itertools import permutations
>>> def find:
	
SyntaxError: invalid syntax
>>> def find(target=3):
	for c in cubes:
		perms = permutations(str(c))
		permcubes = []
		for p in perms:
			return p

		
>>> find()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    find()
  File "<pyshell#15>", line 2, in find
    for c in cubes:
TypeError: 'function' object is not iterable
>>> def find(target=3):
	for c in cubes():
		perms = permutations(str(c))
		permcubes = []
		for p in perms:
			return p

		
>>> find()
('4', '0', '9', '6')
>>> def find(target=3):
	for c in cubes():
		perms = permutations(str(c))
		permcubes = []
		for p in perms:
			return ''.join(p)

		
>>> find()
'4096'
>>> def find(target=3):
	for c in cubes():
		perms = permutations(str(c))
		permcubes = []
		for p in perms:
			return int(''.join(p))

		
>>> find()
4096
>>> def find(target=3):
	for c in cubes():
		perms = permutations(str(c))
		permcubes = []
		return len(filter(cubes.__contains__, map((lambda x:int(''.join(x))),perms)))

	
>>> find()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    find()
  File "<pyshell#30>", line 5, in find
    return len(filter(cubes.__contains__, map((lambda x:int(''.join(x))),perms)))
AttributeError: 'function' object has no attribute '__contains__'
>>> def find(target=3):
	cbs = cubes()
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		return len(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms)))

	
>>> find()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    find()
  File "<pyshell#33>", line 6, in find
    return len(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms)))
TypeError: object of type 'filter' has no len()
>>> def find(target=3):
	cbs = cubes()
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		return len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))

	
>>> find()
1
>>> def find(target=3):
	cbs = cubes()
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
		if l == target:
			return c

		
>>> find()
56623104
>>> find(5)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    find(5)
  File "<pyshell#41>", line 6, in find
    l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
  File "<pyshell#41>", line 6, in <lambda>
    l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
KeyboardInterrupt
>>> def find(target=3):
	cbs = cubes()
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
		if l == target:
			return c
	return None

>>> find(5)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    find(5)
  File "<pyshell#46>", line 6, in find
    l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
  File "<pyshell#46>", line 6, in <lambda>
    l = len(set(filter(cbs.__contains__, map((lambda x:int(''.join(x))),perms))))
KeyboardInterrupt

>>> map(int.__mul__,
KeyboardInterrupt
>>> tens = list(map(int(10).__pow__,range(12)))
>>> tens
[1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]
>>> map(int.__mul__,tens,(4, 0, 9, 6))
<map object at 0x0000015EFB1DA128>
>>> list(map(int.__mul__,tens,(4, 0, 9, 6)))
[4, 0, 900, 6000]
>>> sum(map(int.__mul__,tens,(4, 0, 9, 6)))
6904
>>> sum(map(int.__mul__,tens,(4, 0, 9, 6)[::-1]))
4096
>>> sum(map(int.__mul__,tens,map(int,('4', '0', '9', '6')[::-1])))
4096
>>> sum(map(int.__mul__,tens,map(int,('4', '0', '9', '6')[::-1])))
4096
>>> def perm2num(p):
	return sum(map(int.__mul__,tens,map(int,p[::-1])))

>>> def find(target=3):
	cbs = cubes()
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		l = len(set(filter(cbs.__contains__,map(perm2num,perms))))
		if l == target:
			return c
	return None

>>> find()
56623104
>>> find(5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    find(5)
  File "<pyshell#60>", line 6, in find
    l = len(set(filter(cbs.__contains__,map(perm2num,perms))))
  File "<pyshell#58>", line 1, in perm2num
    def perm2num(p):
KeyboardInterrupt
>>> def find(target=3):
	cbs = cubes()
	scbs = set(map(str,cbs))
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		l = len(set(filter(cbs.__contains__,map(''.join,perms))))
		if l == target:
			return c
	return None

>>> find()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    find()
  File "<pyshell#64>", line 7, in find
    l = len(set(filter(cbs.__contains__,map(''.join,perms))))
KeyboardInterrupt
>>> def find(target=3):
	cbs = cubes()
	scbs = set(map(str,cbs))
	for c in cbs:
		perms = permutations(str(c))
		permcubes = []
		l = len(set(filter(scbs.__contains__,map(''.join,perms))))
		if l == target:
			return c
	return None

>>> find()
56623104
>>> find(4)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    find(4)
  File "<pyshell#67>", line 7, in find
    l = len(set(filter(scbs.__contains__,map(''.join,perms))))
KeyboardInterrupt
>>> def find(target=3):
	cbs = cubes()
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return None

>>> find(3)
56623104
>>> find(4)
>>> None
>>> def find(target=3):
	cbs = cubes()
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return False

>>> find(4)
False
>>> find(5)
False
>>> def find(target=3,maxn=1000,minn=0):
	cbs = cubes(maxn)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return False

>>> def cubes(maxn=1000,minn=0):
	return set(map(int(3).__rpow__,range(minn+1,maxn+1)))

>>> def cubes(maxn=1000,minn=0):
	return set(map(int(3).__rpow__,range(minn,maxn+1)))

>>> def find(target=3,maxn=1000,minn=0):
	cbs = cubes(maxn)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return False

>>> find(5)
False
>>> def find(target=3,maxn=1000,minn=0):
	cbs = cubes(maxn,minn)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxn+maxn,maxn)

>>> find(4)
18005329061
>>> find(5)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    find(5)
  File "<pyshell#89>", line 9, in find
    return find(target,maxn+maxn,maxn)
  File "<pyshell#89>", line 9, in find
    return find(target,maxn+maxn,maxn)
  File "<pyshell#89>", line 9, in find
    return find(target,maxn+maxn,maxn)
  File "<pyshell#89>", line 6, in find
    l = len(list(filter(srt.__eq__,map(sorted,scbs))))
KeyboardInterrupt
>>> def find(target=3,maxn=1000,minn=0):
	cbs = cubes(maxn,minn)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxn*10,maxn)

>>> find(4)
992518734375
>>> len(992518734375)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    len(992518734375)
TypeError: object of type 'int' has no len()
>>> len(str(992518734375))
12
>>> len(str(18005329061))
11
>>> def cubes(maxdig=3,mindig=1):
	return set(map(int(3).__rpow__,range(10**mindig,10**maxdig)))

>>> def find(target=3,maxdig=3,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find()
56623104
>>> find(4)
992518734375
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(1,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find(4)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    find(4)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#107>", line 2, in find
    cbs = cubes(1,mindig)
  File "<pyshell#99>", line 2, in cubes
    return set(map(int(3).__rpow__,range(10**mindig,10**maxdig)))
RecursionError: maximum recursion depth exceeded in comparison
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find()
56623104
>>> find(2)
125000
>>> list(filter(sorted(str(125000)).__eq__,map(sorted,set(map(str(cubes()))))))
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    list(filter(sorted(str(125000)).__eq__,map(sorted,set(map(str(cubes()))))))
TypeError: map() must have at least two arguments.
>>> list(filter(sorted(str(125000)).__eq__,map(sorted,set(map(str,cubes())))))
[['0', '0', '0', '1', '2', '5'], ['0', '0', '0', '1', '2', '5']]
>>> list(filter(sorted(str(125000)).__eq__,map(sorted,set(map(str,cubes())))))
[['0', '0', '0', '1', '2', '5'], ['0', '0', '0', '1', '2', '5']]
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(set(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find(2)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    find(2)
  File "<pyshell#117>", line 6, in find
    l = len(set(filter(srt.__eq__,map(sorted,scbs))))
TypeError: unhashable type: 'list'
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = len(list(filter(srt.__eq__,map(sorted,scbs))))
		if(l == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> list(filter((lambda x:sorted(str(x))==['0','0','0','1','2','5']),cubes()))
[512000, 125000]
>>> list(filter((lambda x:sorted(str(x))==sorted(str(125000))),cubes()))
[512000, 125000]
>>> list(filter((lambda x:sorted(str(x))==['0','0','0','1','2','5']),cubes()))
[512000, 125000]
>>> list(filter((lambda x:sorted(str(x))==sorted(str(125000))),cubes()))
[512000, 125000]
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = list(filter((lambda x:sorted(str(x))==srt),cubes()))
		if(len(l) == target):
			return l
	return find(target,maxdig+1,maxdig)

>>> find(2)
[512000, 125000]
>>> find(3)
[56623104, 66430125, 41063625]
>>> find(4)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    find(4)
  File "<pyshell#126>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#126>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#126>", line 9, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#126>", line 6, in find
    l = list(filter((lambda x:sorted(str(x))==srt),cubes()))
KeyboardInterrupt
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	for c in cbs:
		srt = sorted(str(c))
		l = list(filter((lambda x:sorted(x)==srt),scbs))
		if(len(l) == target):
			return l
	return find(target,maxdig+1,maxdig)

>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:tuple(sorted(x))),scbs))
	for c in cbs:
		srt = sorted(str(c))
		l = list(filter((lambda x:x==srt),sscbs))
		if(len(l) == target):
			return l
	return find(target,maxdig+1,maxdig)

>>> find(3)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    find(3)
  File "<pyshell#133>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#133>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#133>", line 7, in find
    l = list(filter((lambda x:x==srt),sscbs))
  File "<pyshell#133>", line 7, in <lambda>
    l = list(filter((lambda x:x==srt),sscbs))
KeyboardInterrupt
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:tuple(sorted(x))),scbs))
	for c in cbs:
		srt = sorted(str(c))
		l = list(filter((lambda x:x==srt),sscbs))
		if(len(l) == target):
			return l
	return False#find(target,maxdig+1,maxdig)

>>> find(3)
False
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:tuple(sorted(x))),scbs))
	for c in cbs:
		srt = tuple(sorted(str(c)))
		l = list(filter((lambda x:x==srt),sscbs))
		if(len(l) == target):
			return l
	return False#find(target,maxdig+1,maxdig)

>>> find(3)
False
>>> ('1','2','3') == ('1','2','3')
True
>>> ('1','2','3') == ('1','2','3')
True
>>> tuple(sorted(('2','1','3'))) == ('1','2','3')
True
>>> tuple(sorted(('2','1','3')))
('1', '2', '3')
>>> tuple(sorted(('2','1','3')))tuple(sorted(('2','1','3'))) == ('1','2','3')
KeyboardInterrupt
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:tuple(sorted(x))),scbs))
	for c in cbs:
		srt = tuple(sorted(str(c)))
		l = list(filter((lambda x:x==srt),sscbs))
		if(len(l) == target):
			return l
	return False#find(target,maxdig+1,maxdig)

>>> sorted('12345')
['1', '2', '3', '4', '5']
>>> sorted('54321')
['1', '2', '3', '4', '5']
>>> set(sorted('54321'),sorted('12345'))
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    set(sorted('54321'),sorted('12345'))
TypeError: set expected at most 1 arguments, got 2
>>> set(map(tuple,(sorted('54321'),sorted('12345'))))
{('1', '2', '3', '4', '5')}
>>> set(map((lambda x:tuple(sorted(x))),['12345','54321','12124','53142','12325']))
{('1', '2', '2', '3', '5'), ('1', '1', '2', '2', '4'), ('1', '2', '3', '4', '5')}
>>> set(map((lambda x:''.join(sorted(x)))),['12345','54321','12124','53142','12325']))
SyntaxError: invalid syntax
>>> set(map((lambda x:''.join(sorted(x))),['12345','54321','12124','53142','12325']))
{'12235', '12345', '11224'}
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:''.join(sorted(x))),scbs))
	for c in cbs:
		srt = ''.join(sorted(str(c)))
		l = set(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return l
	return False#find(target,maxdig+1,maxdig)

>>> find()
False
>>> find()
False
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:''.join(sorted(x))),scbs))
	for c in cbs:
		srt = ''.join(sorted(str(c)))
		l = set(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return l
	return find(target,maxdig+1,maxdig)

>>> find()
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    find()
  File "<pyshell#159>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#159>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#159>", line 8, in find
    if(len(l) == target):
KeyboardInterrupt
>>> def find(target=3,maxdig=4,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = set(map((lambda x:''.join(sorted(x))),scbs))
	for c in cbs:
		srt = ''.join(sorted(str(c)))
		l = set(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return l
	return False#find(target,maxdig+1,maxdig)

>>> find()
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    find()
  File "<pyshell#162>", line 8, in find
    if(len(l) == target):
KeyboardInterrupt
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = tuple(map(sorted,scbs))
	for c in cbs:
		srt = ''.join(sorted(str(c)))
		l = set(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    find()
  File "<pyshell#165>", line 7, in find
    l = set(filter(srt.__eq__,sscbs))
TypeError: unhashable type: 'list'
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = tuple(map(sorted,scbs))
	for c in cbs:
		srt = ''.join(sorted(str(c)))
		l = list(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find()
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    find()
  File "<pyshell#168>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#168>", line 10, in find
    return find(target,maxdig+1,maxdig)
  File "<pyshell#168>", line 8, in find
    if(len(l) == target):
KeyboardInterrupt
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = tuple(map(sorted,scbs))
	for c in cbs:
		srt = sorted(str(c))
		l = tuple(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return c
	return find(target,maxdig+1,maxdig)

>>> find()
56623104
>>> def find(target=3,maxdig=2,mindig=1):
	cbs = cubes(maxdig,mindig)
	scbs = set(map(str,cbs))
	sscbs = tuple(map(sorted,scbs))
	for c in cbs:
		srt = sorted(str(c))
		l = tuple(filter(srt.__eq__,sscbs))
		if(len(l) == target):
			return tuple(filter((lambda x:sorted(x)==srt),scbs))
	return find(target,maxdig+1,maxdig)

>>> find()
('66430125', '56623104', '41063625')
>>> find(4)
('517394837952', '581973732549', '939752134875', '992518734375')
>>> find(5)
('352045367981', '569310543872', '589323567104', '373559126408', '127035954683')
>>> 
