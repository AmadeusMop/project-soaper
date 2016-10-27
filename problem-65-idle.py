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
>>> int(1.2).numerator
1
>>> int(1.2).denominator
1
>>> int.denominator(1.2)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    int.denominator(1.2)
TypeError: 'getset_descriptor' object is not callable
>>> x = int(5)
>>> x.numerator
5
>>> x.denominator
1
>>> x.denominator = 2
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    x.denominator = 2
AttributeError: attribute 'denominator' of 'int' objects is not writable
>>> x
5
>>> x.__setattr__('denominator',2)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    x.__setattr__('denominator',2)
AttributeError: attribute 'denominator' of 'int' objects is not writable
>>> help(int)
Help on class int in module builtins:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      default object formatter
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> 
>>> from numbers import Rational
>>> Rational(2,3)
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    Rational(2,3)
TypeError: object() takes no parameters
>>> Rational()
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    Rational()
TypeError: Can't instantiate abstract class Rational with abstract methods __abs__, __add__, __ceil__, __eq__, __floor__, __floordiv__, __le__, __lt__, __mod__, __mul__, __neg__, __pos__, __pow__, __radd__, __rfloordiv__, __rmod__, __rmul__, __round__, __rpow__, __rtruediv__, __truediv__, __trunc__, denominator, numerator
>>> Rational.denominator
<property object at 0x0000015EFB201188>
>>> x = Rational()
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    x = Rational()
TypeError: Can't instantiate abstract class Rational with abstract methods __abs__, __add__, __ceil__, __eq__, __floor__, __floordiv__, __le__, __lt__, __mod__, __mul__, __neg__, __pos__, __pow__, __radd__, __rfloordiv__, __rmod__, __rmul__, __round__, __rpow__, __rtruediv__, __truediv__, __trunc__, denominator, numerator
>>> fractions
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    fractions
NameError: name 'fractions' is not defined
>>> from fractions import Fraction
>>> Fraction(3,4)
Fraction(3, 4)
>>> Fraction(6,4)
Fraction(3, 2)
>>> Fraction(6,1.4)
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    Fraction(6,1.4)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\fractions.py", line 182, in __new__
    raise TypeError("both arguments should be "
TypeError: both arguments should be Rational instances
>>> Fraction(6,)
Fraction(6, 1)
F
>>> Fraction(6,Fraction(1.4))
Fraction(13510798882111488, 3152519739159347)
>>> Fraction(6,Fraction(1,4))
Fraction(24, 1)
>>> Fraction(1,Fraction(1,4))
Fraction(4, 1)
>>> int(Fraction(1,Fraction(1,4)))
4
>>> Fraction(1,2).__rpow__(23)
4.795831523312719
>>> divmod(1,Fraction(1,2).__rpow__(23))
(0.0, 1.0)
>>> Fraction(1,2).__rpow__(23) - 4
0.7958315233127191
>>> 1 / (Fraction(1,2).__rpow__(23) - 4)
1.2565473604732462
>>> x = Fraction(1,2).__rpow__(23)
>>> y = x
>>> for i in range(10):
	print(int(y))
	y = 1/(y - int(y))

	
4
1
3
1
8
1
3
1
8
1
>>> for i in range(10):
	print(y)
	y = 1/(y - int(y))

	
3.897915716211872
1.1136902739811723
8.795827162538156
1.2565542457870738
3.8978111507456643
1.1138199822640475
8.78580351277977
1.2725827560410266
3.6686106433287713
1.4956387697051314
>>> y = x
>>> for i in range(10):
	print(y)
	y = 1/(y - int(y))

	
4.795831523312719
1.2565473604732462
3.897915761656351
1.1136902176161134
8.795831523311897
1.256547360474545
3.8979157616366185
1.113690217640588
8.795831521418377
1.256547363464245
>>> 4 + 1/(1+1/(3+1/(1+1/(8))))
4.795454545454546
>>> 23**0.5
4.795831523312719
>>> 23**0.5 - 4
0.7958315233127191
>>> Fraction(1,23**0.5 - 4)
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    Fraction(1,23**0.5 - 4)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\fractions.py", line 182, in __new__
    raise TypeError("both arguments should be "
TypeError: both arguments should be Rational instances
>>> z = Fraction(1,1)
>>> z
Fraction(1, 1)
>>> z = 1 + Fraction(1,1+z)
>>> z
Fraction(3, 2)
>>> f = lambda q: 1 + Fraction(1,1+q)
>>> z = Fraction(1,1)
>>> for i in range(10):
	print(z)
	z = f(z)

	
1
3/2
7/5
17/12
41/29
99/70
239/169
577/408
1393/985
3363/2378
>>> def e():
	yield 2
	k = 2
	while True:
		yield 1
		yield k
		yield 1
		k += 2

		
>>> conv = e()
>>> [conv for i in range(10)]
[<generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>, <generator object e at 0x0000015EFCE99410>]
>>> [conv() for i in range(10)]
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    [conv() for i in range(10)]
  File "<pyshell#245>", line 1, in <listcomp>
    [conv() for i in range(10)]
TypeError: 'generator' object is not callable
>>> [next(conv) for i in range(10)]
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1]
>>> [next(e()) for i in range(10)]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
>>> def convergents(n=10):
	
KeyboardInterrupt
>>> def e(n=True):
	yield 2
	k = 2
	while True:
		yield 1
		yield k
		yield 1
		k += 2
KeyboardInterrupt
>>> while True:
KeyboardInterrupt
>>> def e(n=1000):
	if not n:
		return False
	yield 2
	k = 2
	thm = int(3).__rmod__
	for i in range(n):
		if thm(i):
			yield 1
		else:
			yield k
			k += 2

			
>>> conv = e(10)
>>> [next(conv) for i in range(10)]
[2, 2, 1, 1, 4, 1, 1, 6, 1, 1]
>>> 0%3
0
>>> def e(n=1000):
	if not n:
		return False
	yield 2
	k = 2
	thm = int(3).__rmod__
	for i in range(1,n):
		if thm(i):
			yield 1
		else:
			yield k
			k += 2

			
>>> conv = e(10)
>>> [next(conv) for i in range(10)]
[2, 1, 1, 2, 1, 1, 4, 1, 1, 6]
>>> def e(n=1000):
	if not n:
		return False
	yield 2
	k = 2
	thm = int(3).__rmod__
	for i in range(-1,n-1):
		if thm(i):
			yield 1
		else:
			yield k
			k += 2

			
>>> conv = e(10)
>>> 
>>> 
>>> [next(conv) for i in range(10)]
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1]
>>> def e(n=1000):
	if not n:
		return False
	yield 2
	k = 2
	thm = lambda x: int(3).__rmod__(x-1)
	for i in range(n):
		if thm(i):
			yield 1
		else:
			yield k
			k += 2

			
>>> conv = e(10)
>>> [next(conv) for i in range(10)]
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1]
>>> def convergents(n=10):
	conv = e(n)
	num = 1
	den = 1

	
>>> Fraction.limit_denominator
<function Fraction.limit_denominator at 0x0000015EFC618AE8>
>>> Fraction.limit_denominator()
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    Fraction.limit_denominator()
TypeError: limit_denominator() missing 1 required positional argument: 'self'
>>> Fraction.limit_denominator(Fraction(1,2))
Fraction(1, 2)
>>> Fraction(1,2).limit_denominator
<bound method Fraction.limit_denominator of Fraction(1, 2)>
>>> Fraction(1,2).limit_denominator)
SyntaxError: invalid syntax
>>> Fraction(1,2).limit_denominator()
Fraction(1, 2)
>>> def convergents(n=10):
	conv = e(n)
	num = 1
	den = 1
KeyboardInterrupt
>>> list(e(10))
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1]
>>> conv = e(n)
KeyboardInterrupt
>>> def convergents(n=10):
	l = list(e(n))
	frac = Fraction(1,l.pop())
	while(l):
		frac = l.pop()+Fraction(1,frac)
	return frac

>>> convergents()
Fraction(2721, 1001)
>>> convergents(9)
Fraction(1457, 536)
>>> def convergents(n=10):
	l = list(e(n-1))
	frac = Fraction(1,l.pop())
	while(l):
		frac = l.pop()+Fraction(1,frac)
	return frac

>>> def e(n=1000):
	if not n:
		return False
	yield 2
	k = 2
	thm = lambda x: int(3).__rmod__(x-1)
	for i in range(n-1):
		if thm(i):
			yield 1
		else:
			yield k
			k += 2

			
>>> def convergents(n=10):
	l = list(e(n))
	frac = Fraction(1,l.pop())
	while(l):
		frac = l.pop()+Fraction(1,frac)
	return frac

>>> convergents()
Fraction(1457, 536)
>>> convergents().denominator
536
>>> convergents().numerator
1457
>>> sum(map(int,str(convergents().numerator)))
17
>>> sum(map(int,str(convergents(100).numerator)))
272
>>> 
