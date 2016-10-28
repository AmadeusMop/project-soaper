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
=============================== RESTART: Shell ===============================
>>> def sieve(maxn=10000):
	nums = set(range(2,maxn))
	for i in range(2,maxn):
		if i in nums:
			nums.difference_update(set(range(i+i,maxn,i)))
	return nums

>>> sieve(100)
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
>>> def isprime(n):
	if not f%2:
		return False
	m = int(n**0.5+1)
	return all(map(n.__mod__,range(3,m,2)))

>>> isprime(3)
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    isprime(3)
  File "<pyshell#314>", line 2, in isprime
    if not f%2:
NameError: name 'f' is not defined
>>> def isprime(n):
	if not n%2:
		return False
	m = int(n**0.5+1)
	return all(map(n.__mod__,range(3,m,2)))

>>> isprime(3)
True
>>> isprime(5)
True
>>> isprime(6)
False
>>> isprime(18)
False
>>> isprime(19)
True
>>> def pairsets(n=4):
	return 0

>>> primes = sieve(1000000)
>>> def pairsets(n=4):
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})

	
>>> isprime(109673)
True
>>> isprime(673109)
True
>>> 109673 in primes
True
>>> def sieve(maxn=10000):
	nums = set(range(2,maxn))
	for i in range(2,maxn):
		if i in nums:
			nums.difference_update(range(i+i,maxn,i))
	return nums

>>> primes = sieve(1000000)
>>> primes = sieve(10000000)
>>> def sieve(maxn=10000):
	nums = set(range(2,maxn))
	for i in range(3,maxn,2):
		if i in nums:
			nums.difference_update(range(i+i,maxn,i))
	return nums

>>> primes = sieve(1000000)
>>> def sieve_old(maxn=10000):
	nums = set(range(2,maxn))
	for i in range(2,maxn):
		if i in nums:
			nums.difference_update(range(i+i,maxn,i))
	return nums

>>> primes = sieve(1000000)
>>> primes = sieve_old(1000000)

>>> primes = sieve_old(1000000)
>>> primes = sieve(1000000)
>>> nums = set(range(2,10))
>>> nums
{2, 3, 4, 5, 6, 7, 8, 9}
>>> nums = set(range(2,50))
>>> nums
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49}
>>> filter(nums,int(2).__mod__)
Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    filter(nums,int(2).__mod__)
TypeError: 'method-wrapper' object is not iterable
>>> {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49}
KeyboardInterrupt
>>> filter(int(2).__mod__,nums)
<filter object at 0x0000026F6D088CF8>
>>> set(filter(int(2).__mod__,nums))
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49}
>>> set.union({2},filter(int(2).__mod__,nums))
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49}
>>> set.union({2},filter(int(2).__rmod__,nums))
{2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49}
>>> nums = set.union({2},filter(int(2).__rmod__,nums))
>>> nums = set.union({3},filter(int(3).__rmod__,nums))
>>> nums
{2, 3, 35, 5, 37, 7, 41, 11, 43, 13, 47, 17, 49, 19, 23, 25, 29, 31}
>>> primes(10)
Traceback (most recent call last):
  File "<pyshell#359>", line 1, in <module>
    primes(10)
TypeError: 'set' object is not callable
>>> del nums
>>> sieve(10)
{2, 3, 4, 5, 7, 8}
>>> sieve(11)
{2, 3, 4, 5, 7, 8}
>>> def sieve(maxn=10000):
	nums = set.union({2},range(3,maxn,2))
	for i in range(3,maxn,2):
		if i in nums:
			nums.difference_update(range(i+i,maxn,i))
	return nums

>>> sieve(10)
{2, 3, 5, 7}
>>> sieve(11)
{2, 3, 5, 7}
>>> sieve(12)
{2, 3, 5, 7, 11}
>>> sieve(20)
{2, 3, 5, 7, 11, 13, 17, 19}
>>> all(map(isprime,sieve(100)))
False
>>> filter((not isprime,sieve(100)))
Traceback (most recent call last):
  File "<pyshell#370>", line 1, in <module>
    filter((not isprime,sieve(100)))
TypeError: filter expected 2 arguments, got 1
>>> filter(not isprime,sieve(100))
<filter object at 0x0000026F6D088CC0>
>>> list(filter(not isprime,sieve(100)))
Traceback (most recent call last):
  File "<pyshell#372>", line 1, in <module>
    list(filter(not isprime,sieve(100)))
TypeError: 'bool' object is not callable
>>> list(filter((lambda x: not isprime(x)),sieve(100)))
[2]
>>> def isprime(n):
	if not n%2:
		return False
	m = int(n**0.5+1)
	return all(map(n.__mod__,range(3,m,2)))

>>> 2%2
0
>>> def isprime(n):
	m = int(n**0.5+1)
	return all(map(n.__mod__,range(3,m,2)))

>>> all([])
True
>>> all(map(int(1).__mod__,range(3,int(1**0.5+1),2)))
True
>>> all(map(int(-1).__mod__,range(3,int(int(-1)**0.5+1),2)))
Traceback (most recent call last):
  File "<pyshell#381>", line 1, in <module>
    all(map(int(-1).__mod__,range(3,int(int(-1)**0.5+1),2)))
TypeError: can't convert complex to int
>>> all(map(int(0).__mod__,range(3,int(int(0)**0.5+1),2)))
True
>>> def isprime(n):
	if n < 2:
		raise
	elif not n % 2:
		return n == 2
	else:
		m = int(n**0.5+1)
		return all(map(n.__mod__,range(3,m,2)))

	
>>> 2048 + 4096
6144
>>> 6144/2
3072.0
>>> 6144//2
3072
>>> 3072-2048
1024
>>> 4097-1024
3073
>>> 4096-1024
3072
>>> def isprime(n):
	if n < 2:
		raise ValueError(n)
	if not n % 2:
		return n == 2
	else:
		m = int(n**0.5+1)
		return all(map(n.__mod__,range(3,m,2)))

	
>>> all(map(isprime,sieve(100)))
True
>>> all(map(isprime,sieve(100000)))
True
>>> all(map(isprime,sieve(1000000)))
True
>>> p = sieve(1000000)
>>> p = set(filter(isprime,range(2,1000000)))
>>> p = sieve(1000000)
>>> def sundaram3(max_n):
    numbers = list(range(3, max_n, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

        
>>> sundaram3(10)
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    sundaram3(10)
  File "<pyshell#400>", line 12, in sundaram3
    return [2] + filter(None, numbers)
TypeError: can only concatenate list (not "filter") to list
>>> def sundaram3(max_n):
    numbers = list(range(3, max_n, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))

        
>>> sundaram3(10)
[2, 3, 5, 7]
>>> sundaram3(9)
[2, 3, 5, 7]
>>> sundaram3(11)
[2, 3, 5, 7]
>>> sundaram3(12)
[2, 3, 5, 7, 11]
>>> def sundaram3(max_n):
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))

        
>>> sundaram3(12)
[2, 3, 5, 7, 11]
>>> sundaram3(9)
[2, 3, 5, 7, 9]
>>> def sundaram3(max_n):
    numbers = list(range(3, max_n, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))

        
>>> sundaram3(12)
[2, 3, 5, 7, 11]
>>> sundaram3(13)
[2, 3, 5, 7, 11]
>>> sundaram3(14)
[2, 3, 5, 7, 11, 13]
>>> sundaram3(7072)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069]
>>> p = sieve()
>>> p = sieve(1000000)
>>> p = sundaram3(1000000)
>>> p = sieve(1000000)
>>> p = sundaram3(1000000)
>>> p = sundaram3(1000000)
>>> p = sieve(1000000)
>>> p = sundaram3(10000000)
>>> p = sieve(10000000)
>>> p = sundaram3(10000000)
>>> p = sundaram3(10000000)
>>> p = sieve(10000000)
>>> def pairsets(n=4):
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})

	
>>> def pairsets(n=4):
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))

	
>>> def pairsets(n=4):
	tens = list(map(10.__pow__,range(1,12)))
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	
SyntaxError: invalid syntax
>>> def pairsets(n=4):
	tens = set(map(int(10).__pow__,range(1,12)))
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))

	
>>> def pairsets(n=4):
	tens = set(map(int(10).__pow__,range(1,12)))
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	return len(candidates)

>>> pairsets()
2857
>>> len(sieve(100000))
9592
>>> tens = set(map(int(10).__pow__,range(1,12)))
>>> list(filter(int(356).__gt__,tens))
[100, 10]
>>> divmod(356,100)
(3, 56)
>>> divmod(356,10)
(35, 6)
>>> def pairsets(n=4):
	tens = set(map(int(10).__pow__,range(1,12)))
	primes = sieve(100000)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	return candidates

>>> cand = pairsets()
>>> list(cand)[:10]
[65537, 40961, 57349, 98317, 40973, 24593, 98323, 49171, 32789, 23]
>>> 109 in cand
False
>>> def pairsets(n=4,maxd=6):
	maxn = 10**maxd
	tens = set(map(int(10).__pow__,range(1,maxd+1)))
	primes = sieve(maxn)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	return candidates

>>> 10**6
1000000
>>> divmod(999999,1000000)
(0, 999999)
>>> def pairsets(n=4,maxd=6):
	maxn = 10**maxd
	tens = set(map(int(10).__pow__,range(1,maxd)))
	primes = sieve(maxn)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	return candidates

>>> cand = pairsets()
>>> 7109 in cand
True
>>> len(cand)
21274
>>> len(sieve(1000000))
78498
>>> def pairsets(n=4,maxd=6):
	maxn = 10**maxd
	tens = set(map(int(10).__pow__,range(1,maxd)))
	primes = sieve(maxn)
	sprimes = set(map(str,primes))
	candidates = primes.difference({2,5})
	candidates = set(filter((lambda c: any(map((lambda t: all(map(primes.__contains__,divmod(c,t)))),filter(c.__gt__,tens)))),candidates))
	cdict = dict()
	for c in candidates:
		p = []
		for t in filter(c.__gt__,tens):
			if all(map(primes.__contains__,divmod(c,t))):
				p.append(divmod(c,t))
		cdict[c] = p
	return cdict

>>> candict = pairsets()
>>> candict[7109]
[(7, 109)]
>>> max(map(len,candict))
Traceback (most recent call last):
  File "<pyshell#466>", line 1, in <module>
    max(map(len,candict))
TypeError: object of type 'int' has no len()
>>> max(map(len,candict.keys))
Traceback (most recent call last):
  File "<pyshell#467>", line 1, in <module>
    max(map(len,candict.keys))
TypeError: 'builtin_function_or_method' object is not iterable
>>> max(map(len,candict.keys()))
Traceback (most recent call last):
  File "<pyshell#468>", line 1, in <module>
    max(map(len,candict.keys()))
TypeError: object of type 'int' has no len()
>>> max(map(len,candict.v))
Traceback (most recent call last):
  File "<pyshell#469>", line 1, in <module>
    max(map(len,candict.v))
AttributeError: 'dict' object has no attribute 'v'
>>> max(map(len,candict.values()))
5
>>> f = list(filter((lambda x: len(x)>=4),candict.values()))
>>> len(f)
9
>>> f
[[(233, 911), (23, 3911), (2339, 11), (2, 33911)], [(337, 397), (33739, 7), (3373, 97), (3, 37397)], [(79, 6337), (79633, 7), (7963, 37), (7, 96337)], [(733, 331), (73, 3331), (7333, 31), (7, 33331)], [(373, 613), (37, 3613), (37361, 3), (3, 73613)], [(379, 397), (37, 9397), (3793, 97), (3, 79397)], [(739, 397), (73, 9397), (73939, 7), (7393, 97), (7, 39397)], [(233, 347), (23, 3347), (2333, 47), (2, 33347)], [(239, 929), (23, 9929), (2399, 29), (2, 39929)]]
>>> print f
SyntaxError: Missing parentheses in call to 'print'
>>> print(f)
[[(233, 911), (23, 3911), (2339, 11), (2, 33911)], [(337, 397), (33739, 7), (3373, 97), (3, 37397)], [(79, 6337), (79633, 7), (7963, 37), (7, 96337)], [(733, 331), (73, 3331), (7333, 31), (7, 33331)], [(373, 613), (37, 3613), (37361, 3), (3, 73613)], [(379, 397), (37, 9397), (3793, 97), (3, 79397)], [(739, 397), (73, 9397), (73939, 7), (7393, 97), (7, 39397)], [(233, 347), (23, 3347), (2333, 47), (2, 33347)], [(239, 929), (23, 9929), (2399, 29), (2, 39929)]]
>>> map(print,f)
<map object at 0x0000026F03654438>
>>> list(map(print,f))
[(233, 911), (23, 3911), (2339, 11), (2, 33911)]
[(337, 397), (33739, 7), (3373, 97), (3, 37397)]
[(79, 6337), (79633, 7), (7963, 37), (7, 96337)]
[(733, 331), (73, 3331), (7333, 31), (7, 33331)]
[(373, 613), (37, 3613), (37361, 3), (3, 73613)]
[(379, 397), (37, 9397), (3793, 97), (3, 79397)]
[(739, 397), (73, 9397), (73939, 7), (7393, 97), (7, 39397)]
[(233, 347), (23, 3347), (2333, 47), (2, 33347)]
[(239, 929), (23, 9929), (2399, 29), (2, 39929)]
[None, None, None, None, None, None, None, None, None]
>>> isprime(39)
False
>>> 39 in primes
False
>>> isprime(379)
True
>>> isprime(397)
True
>>> def diff(l):
	return list(map(int.__sub__,l[1:],l[:-1]))

>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(l[1:])
9
>>> len(l[:-1])
9
>>> l[:-1]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> diff(l)
[1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> list(map(int.__add__,l[1:],l[:-1]))
[1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> list(map(int.__add__,l[1:],l[:-1]))
[1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> l = list(map(int.__add__,l[1:],l[:-1]))
>>> list(map(int.__add__,l[1:],l[:-1]))
[4, 8, 12, 16, 20, 24, 28, 32]
>>> l = list(range(1,10))
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(map(int.__add__,l[1:],l[:-1]))
[3, 5, 7, 9, 11, 13, 15, 17]
>>> list(itertools.accumulate(l,int.__add__))
Traceback (most recent call last):
  File "<pyshell#498>", line 1, in <module>
    list(itertools.accumulate(l,int.__add__))
NameError: name 'itertools' is not defined
>>> import itertools
>>> list(itertools.accumulate(l,int.__add__))
[1, 3, 6, 10, 15, 21, 28, 36, 45]
>>> len(filter(int(10).__lt__,range(100)))
Traceback (most recent call last):
  File "<pyshell#501>", line 1, in <module>
    len(filter(int(10).__lt__,range(100)))
TypeError: object of type 'filter' has no len()
>>> len(list(filter(int(10).__lt__,range(100))))
89
>>> 89**6
496981290961
>>> polyg = dict(3=(lambda n:n*(n+1)/2
KeyboardInterrupt
>>> polyg = dict()
>>> polyg[3]=(lambda n:n*(n+1)/2)
>>> polyg[4]=(lambda n:n*n)
>>> polyg[5]=(lambda n:n*(3*n-1)/2)
>>> polyg[6]=(lambda n:n*(2*n-1))
>>> polyg[7]=(lambda n:n*(5*n-3)/2)
>>> polyg[3]=(lambda n:n*(n+1)//2)
>>> polyg[5]=(lambda n:n*(3*n-1)//2)
>>> polyg[7]=(lambda n:n*(5*n-3)//2)
>>> polyg[8]=(lambda n:n*(3*n-2))
>>> map(list,map((lambda f:list(map(f,range(5)))),polyg))
<map object at 0x0000026F03654CC0>
>>> list(map(list,map((lambda f:list(map(f,range(5)))),polyg)))
Traceback (most recent call last):
  File "<pyshell#516>", line 1, in <module>
    list(map(list,map((lambda f:list(map(f,range(5)))),polyg)))
  File "<pyshell#516>", line 1, in <lambda>
    list(map(list,map((lambda f:list(map(f,range(5)))),polyg)))
TypeError: 'int' object is not callable
>>> list(map(list,map((lambda f:list(map(f,range(5)))),map(polyg.get,range(3,9)))))
[[0, 1, 3, 6, 10], [0, 1, 4, 9, 16], [0, 1, 5, 12, 22], [0, 1, 6, 15, 28], [0, 1, 7, 18, 34], [0, 1, 8, 21, 40]]
>>> map(print,list(map(list,map((lambda f:list(map(f,range(5)))),map(polyg.get,range(3,9))))))
<map object at 0x0000026F03654898>
>>> set(map(print,list(map(list,map((lambda f:list(map(f,range(5)))),map(polyg.get,range(3,9)))))))
[0, 1, 3, 6, 10]
[0, 1, 4, 9, 16]
[0, 1, 5, 12, 22]
[0, 1, 6, 15, 28]
[0, 1, 7, 18, 34]
[0, 1, 8, 21, 40]
{None}
>>> set(map(print,list(map(list,map((lambda f:list(map(f,range(1,6)))),map(polyg.get,range(3,9)))))))
[1, 3, 6, 10, 15]
[1, 4, 9, 16, 25]
[1, 5, 12, 22, 35]
[1, 6, 15, 28, 45]
[1, 7, 18, 34, 55]
[1, 8, 21, 40, 65]
{None}
>>> P = list(list()*8)
>>> P
[]
>>> list()*8
[]
>>> [list()]*8
[[], [], [], [], [], [], [], []]
>>> P = list()*8
>>> P
[]
>>> P = [list()]*8
>>> P
[[], [], [], [], [], [], [], []]
>>> P[0]
[]
>>> P[1]
[]
>>> P = [list()]*6
>>> for i in range(6):
	P[i] = 
KeyboardInterrupt
>>> P = [set()]*8
>>> P
[set(), set(), set(), set(), set(), set(), set(), set()]
>>> for i in range(6):
	P[i] = set(filter((lambda x: x >= 1000 and x < 10000),map(polyg[i+3],range(1000))))

	
>>> len(P[0])
96
>>> len(P[5])
40
>>> P[5]
{1408, 1281, 3201, 8321, 1541, 2821, 4485, 1160, 6533, 8965, 1680, 9976, 1045, 3605, 7701, 4256, 1825, 2465, 6816, 9633, 1976, 3008, 4033, 7105, 8640, 3400, 8008, 2640, 9296, 2133, 5461, 5208, 5720, 4961, 5985, 3816, 7400, 4720, 6256, 2296}
>>> def getP(d=4):
	polyg = dict()
	polyg[3]=(lambda n:n*(n+1)//2)
	polyg[4]=(lambda n:n*n)
	polyg[5]=(lambda n:n*(3*n-1)//2)
	polyg[6]=(lambda n:n*(2*n-1))
	polyg[7]=(lambda n:n*(5*n-3)//2)
	polyg[8]=(lambda n:n*(3*n-2))
	P = [set()]*8
	mint = (10**d)-1
	maxt = 10**(d+1)
	dig = (lambda x: mint < x and maxt > x)
	for i in range(6):
		P[i] = set(filter(dig,map(polyg[i+3],range(1000))))
	return P

>>> P = getP()
>>> len(P[5])
124
>>> P[5]
{22016, 21505, 49665, 11781, 22533, 48133, 21000, 68101, 23056, 13333, 20501, 29205, 39445, 51221, 56856, 64533, 79381, 95765, 37408, 23585, 46625, 20008, 15408, 24120, 41536, 19521, 52801, 78408, 96840, 10325, 24661, 45141, 71765, 19040, 32865, 35425, 29800, 25208, 67200, 77441, 97921, 14981, 18565, 61061, 12936, 54405, 11408, 58520, 25761, 43681, 63656, 18096, 70840, 76480, 30401, 38081, 99008, 40136, 26320, 33496, 14560, 17633, 56033, 36080, 48896, 12545, 66305, 26885, 42245, 75525, 50440, 47376, 17176, 31008, 11041, 69921, 52008, 60208, 45880, 27456, 14145, 62785, 74576, 16725, 34133, 57685, 86360, 87381, 88408, 53600, 85345, 89441, 38760, 84336, 90480, 44408, 12160, 28033, 40833, 31621, 36741, 83333, 65416, 91525, 69008, 16280, 82336, 73633, 92576, 13736, 55216, 10680, 81345, 93633, 28616, 42960, 34776, 61920, 15841, 59361, 80360, 94696, 32240, 72696}
>>> def getP(d=4):
	polyg = dict()
	polyg[3]=(lambda n:n*(n+1)//2)
	polyg[4]=(lambda n:n*n)
	polyg[5]=(lambda n:n*(3*n-1)//2)
	polyg[6]=(lambda n:n*(2*n-1))
	polyg[7]=(lambda n:n*(5*n-3)//2)
	polyg[8]=(lambda n:n*(3*n-2))
	P = [set()]*8
	mint = 10**(d-1) - 1
	maxt = 10**d
	dig = (lambda x: mint < x and maxt > x)
	for i in range(6):
		P[i] = set(filter(dig,map(polyg[i+3],range(1000))))
	return P

>>> P = getP()
>>> len(P[5])
40
>>> P[5]
{1408, 1281, 3201, 8321, 1541, 2821, 4485, 1160, 6533, 8965, 1680, 9976, 1045, 3605, 7701, 4256, 1825, 2465, 6816, 9633, 1976, 3008, 4033, 7105, 8640, 3400, 8008, 2640, 9296, 2133, 5461, 5208, 5720, 4961, 5985, 3816, 7400, 4720, 6256, 2296}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	p = P[5]
	p = list(filter((lambda o: prune(o,P[4])),P[5]))
	return len(p)

>>> find()
18
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	p = P[5]
	p = list(filter((lambda o: prune(o,P[4])),P[5]))
	return p

>>> find()
[1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720]
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	pp = dict()
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i])),pp[i+1]))		pp[5] = list(filter((lambda o: prune(o,pp[5])),pp[0]))
	return pp[5]
SyntaxError: invalid syntax
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	pp = dict()
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,pp[5])),pp[0]))
	return pp[5]

>>> find()
Traceback (most recent call last):
  File "<pyshell#571>", line 1, in <module>
    find()
  File "<pyshell#570>", line 7, in find
    pp[i] = list(filter((lambda o: prune(o,pp[i])),pp[i+1]))
  File "<pyshell#570>", line 7, in <lambda>
    pp[i] = list(filter((lambda o: prune(o,pp[i])),pp[i+1]))
KeyError: 4
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	pp = dict()
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp[5]

>>> find()
[]
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	pp = dict()
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
{0: [], 1: [], 2: [4033, 8008, 2640], 3: [2821, 1160, 4033, 7105, 8640, 8008, 2640, 2133], 4: [1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720], 5: []}
>>> str(8128)[2:]
'28'
>>> str(2882).startswith(str(8128)[2:])
True
>>> str(8281).startswith(str(2882)[2:])
True
>>> str(2882).startswith(str(8281)[2:])
False
>>> str(8128).startswith(str(8281)[2:])
True
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter(str(n).startswith,map((lambda k:str(k)[2:]),p))))
	pp = dict()
	print(prune(8128,P[1]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
{'81'}
{0: [], 1: [], 2: [4033, 8008, 2640], 3: [2821, 1160, 4033, 7105, 8640, 8008, 2640, 2133], 4: [1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720], 5: []}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(8128,P[1]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
{8281, 1681, 3481}
{0: [], 1: [], 2: [4033, 8008, 2640], 3: [2821, 1160, 4033, 7105, 8640, 8008, 2640, 2133], 4: [1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720], 5: []}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(8281,P[2]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
{2882}
{0: [], 1: [], 2: [4033, 8008, 2640], 3: [2821, 1160, 4033, 7105, 8640, 8008, 2640, 2133], 4: [1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720], 5: []}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
set()
{0: [], 1: [], 2: [4033, 8008, 2640], 3: [2821, 1160, 4033, 7105, 8640, 8008, 2640, 2133], 4: [1408, 1281, 2821, 4485, 1160, 1045, 7701, 1825, 4033, 7105, 8640, 8008, 2640, 2133, 5208, 5985, 7400, 4720], 5: []}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(map((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
set()
{0: [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()], 1: [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()], 2: [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()], 3: [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()], 4: [{8614}, {2512}, set(), set(), set(), {9828}, {3744}, {9211}, set(), set(), set(), set(), {3010, 8910}, set(), {1177}, set(), {1918}, set(), set(), set(), set(), set(), {3940}, {1071}, {3186}, set(), {7480}, {6426}, set(), {5221}, set(), {5452}, set(), set(), {2059}, set(), {4774}, {4347}, set(), set()], 5: []}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = set(map((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
set()
Traceback (most recent call last):
  File "<pyshell#600>", line 1, in <module>
    find()
  File "<pyshell#599>", line 8, in find
    pp[i] = set(map((lambda o: prune(o,P[i])),pp[i+1]))
TypeError: unhashable type: 'set'
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(map((lambda o: prune(o,P[i])),pp[i+1]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
>>> P[5]
{1408, 1281, 3201, 8321, 1541, 2821, 4485, 1160, 6533, 8965, 1680, 9976, 1045, 3605, 7701, 4256, 1825, 2465, 6816, 9633, 1976, 3008, 4033, 7105, 8640, 3400, 8008, 2640, 9296, 2133, 5461, 5208, 5720, 4961, 5985, 3816, 7400, 4720, 6256, 2296}
>>> list(map((lambda o: prune(o,P[1])),P[0]))
[set(), set(), set(), set(), set(), set(), set(), {7056, 1156, 4356}, set(), set(), set(), set(), set(), set(), {1936, 3136, 8836}, set(), set(), set(), {5041, 6241}, set(), {3721, 1521, 7921}, set(), set(), {9216, 2916, 2116}, set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), {1089, 4489, 6889}, set(), set(), set(), set(), set(), set(), set(), set(), {1369, 3969, 7569}, set(), set(), set(), set(), set(), set(), {8464, 3364, 1764}, set(), set(), set(), set(), set(), set(), set(), set(), set(), {3249, 8649, 1849}, set(), set(), set(), set(), {5929, 5329}, {1024, 4624, 6724}, {7744, 1444, 3844}, set(), set(), set(), set(), set(), set(), {1024, 4624, 6724}, set(), set(), set(), {8281, 1681, 3481}, set(), {5776, 5476}, set(), set(), {4761, 6561}, set(), set(), set(), set(), {9025, 4225, 1225, 2025, 3025, 5625, 7225}, set()]
>>> list(filter((lambda o: prune(o,P[1])),P[0]))
[5671, 3655, 4186, 2145, 1653, 8911, 6903, 6441, 4950, 2926, 2415, 4465, 2485, 8128, 7626, 6105, 2556]
>>> ptest = list(filter((lambda o: prune(o,P[1])),P[0]))
>>> list(map((lambda o: prune(o,P[1])),ptest))
[{7056, 1156, 4356}, {1936, 3136, 8836}, {5041, 6241}, {3721, 1521, 7921}, {9216, 2916, 2116}, {1089, 4489, 6889}, {1369, 3969, 7569}, {8464, 3364, 1764}, {3249, 8649, 1849}, {5929, 5329}, {1024, 4624, 6724}, {7744, 1444, 3844}, {1024, 4624, 6724}, {8281, 1681, 3481}, {5776, 5476}, {4761, 6561}, {9025, 4225, 1225, 2025, 3025, 5625, 7225}]
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[:] = P[:]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
set()
Traceback (most recent call last):
  File "<pyshell#611>", line 1, in <module>
    find()
  File "<pyshell#610>", line 6, in find
    pp[:] = P[:]
TypeError: unhashable type: 'slice'
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp[:] = P[:]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp
KeyboardInterrupt
>>> l = [1,5,3,2]
>>> ll = l[:]
>>> ll
[1, 5, 3, 2]
>>> l[0] = 4
>>> l
[4, 5, 3, 2]
>>> ll
[1, 5, 3, 2]
>>> ll = l
>>> l
[4, 5, 3, 2]
>>> ll
[4, 5, 3, 2]
>>> l[0] = 2
>>> l
[2, 5, 3, 2]
>>> ll
[2, 5, 3, 2]
>>> for i in range(4,-1,-1):
KeyboardInterrupt
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	print(prune(1681,P[2]))
	pp = P[:]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
set()
[[1653], [9216, 2601, 6084], [8626, 2501, 5192, 9560], [5151, 1225, 4186, 5995], [2059, 6175, 3367, 4141, 5688, 4558, 2512, 8037, 1651], [1653], set(), set()]
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	pp = P[:]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[5])),pp[0]))
	return pp

>>> find()
[[1653], [9216, 2601, 6084], [8626, 2501, 5192, 9560], [5151, 1225, 4186, 5995], [2059, 6175, 3367, 4141, 5688, 4558, 2512, 8037, 1651], [1653], set(), set()]
>>> prune(8128,P[1])
{8281, 1681, 3481}
>>> prune(8128,P[1])
{8281, 1681, 3481}
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	pp[5] = P[5]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[0])),pp[5]))
	return pp

>>> find()
Traceback (most recent call last):
  File "<pyshell#634>", line 1, in <module>
    find()
  File "<pyshell#633>", line 7, in find
    pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
KeyError: 4
>>> def find():
	P = getP()
	prune = (lambda n, p: set(filter((lambda k:str(n).startswith(str(k)[2:])),p)))
	pp = dict()
	pp = P[:]
	for i in range(4,-1,-1):
		pp[i] = list(filter((lambda o: prune(o,pp[i+1])),pp[i]))
	pp[5] = list(filter((lambda o: prune(o,P[0])),pp[5]))
	return pp

>>> find()
[[1653], [9216, 2601, 6084], [8626, 2501, 5192, 9560], [5151, 1225, 4186, 5995], [2059, 6175, 3367, 4141, 5688, 4558, 2512, 8037, 1651], [1541, 2821, 1160, 6533, 1680, 9633, 3008, 4033, 7105, 8640, 8008, 2640, 2133], set(), set()]
>>> 
=============================== RESTART: Shell ===============================
>>> 1!
SyntaxError: invalid syntax
>>> fact(1)
Traceback (most recent call last):
  File "<pyshell#639>", line 1, in <module>
    fact(1)
NameError: name 'fact' is not defined
>>> math.factorial(1)
Traceback (most recent call last):
  File "<pyshell#640>", line 1, in <module>
    math.factorial(1)
NameError: name 'math' is not defined
>>> import math
>>> math.factorial(1)
1
>>> math.factorial('1')
Traceback (most recent call last):
  File "<pyshell#643>", line 1, in <module>
    math.factorial('1')
TypeError: an integer is required (got type str)
>>> sum(map(math.factorial,map(int,map(str,[145]))))
804792605747199194484902925779806277109997439007500616344745281047115412373646521410850481879839649227439298230298915019813108221651663659572441609408556917739149315905992811411866635786075524601835815642793302504243200000000000000000000000000000000000
>>> list(map(int,map(str,[145])))
[145]
>>> sum(map(math.factorial,map(int,map(str,145))))
Traceback (most recent call last):
  File "<pyshell#646>", line 1, in <module>
    sum(map(math.factorial,map(int,map(str,145))))
TypeError: 'int' object is not iterable
>>> sum(map(math.factorial,map(int,str(145)))))
SyntaxError: invalid syntax
>>> sum(map(math.factorial,map(int,str(145))))
145
>>> def digfact(n):sum(map(math.factorial,map(int,str(145)))))
SyntaxError: invalid syntax
>>> def digfact(n):
	return sum(map(math.factorial,map(int,str(n))))

>>> digfact(145)
145
>>> digfact(169)
363601
>>> df = digfact
>>> df(df(169))
1454
>>> df(df(df(169)))
169
>>> def dfchain(startn):
	l = [startn]
	for i in range(10):
		l[i+1] = digfact(l[i])
	return l

>>> dfchain(169)
Traceback (most recent call last):
  File "<pyshell#665>", line 1, in <module>
    dfchain(169)
  File "<pyshell#664>", line 4, in dfchain
    l[i+1] = digfact(l[i])
IndexError: list assignment index out of range
>>> def dfchain(startn):
	l = [startn]
	for i in range(10):
		l.append(digfact(l[i]))
	return l

>>> dfchain(169)
[169, 363601, 1454, 169, 363601, 1454, 169, 363601, 1454, 169, 363601]
>>> dfchain(69)
[69, 363600, 1454, 169, 363601, 1454, 169, 363601, 1454, 169, 363601]
>>> def dfchain(startn):
	l = [startn]
	while len(l) < 10000:
		f = digfact(l[-1])
		if f in l:
			return len(l)-l.index(f)
		l.append(digfact(l[i]))
	return False

>>> dfchain(169)
Traceback (most recent call last):
  File "<pyshell#672>", line 1, in <module>
    dfchain(169)
  File "<pyshell#671>", line 7, in dfchain
    l.append(digfact(l[i]))
NameError: name 'i' is not defined
>>> def dfchain(startn):
	l = [startn]
	while len(l) < 10000:
		f = digfact(l[-1])
		if f in l:
			return len(l)-l.index(f)
		l.append(f)
	return False

>>> dfchain(169)
3
>>> dfchain(69)
3
>>> def dfchain(startn):
	l = [startn]
	while len(l) < 10000:
		f = digfact(l[-1])
		if f in l:
			return l.index(f)
		l.append(f)
	return False

>>> dfchain(69)
2
>>> def dfchain(startn):
	l = set(startn)
	f = startn
	while len(l) < 10000:
		f = digfact(f)
		if f in l:
			return len(l)
		l.add(f)
	return False

>>> dfchain(69)
Traceback (most recent call last):
  File "<pyshell#682>", line 1, in <module>
    dfchain(69)
  File "<pyshell#681>", line 2, in dfchain
    l = set(startn)
TypeError: 'int' object is not iterable
>>> def dfchain(startn):
	s = {startn}
	f = startn
	while len(s) < 10000:
		f = digfact(f)
		if f in s:
			return len(s)
		s.add(f)
	return False

>>> dfchain(69)
5
>>> len(set(filter(int(60).__eq__,map(dfchain,range(1000000)))))
Traceback (most recent call last):
  File "<pyshell#686>", line 1, in <module>
    len(set(filter(int(60).__eq__,map(dfchain,range(1000000)))))
  File "<pyshell#684>", line 5, in dfchain
    f = digfact(f)
  File "<pyshell#653>", line 2, in digfact
    return sum(map(math.factorial,map(int,str(n))))
KeyboardInterrupt
>>> dfchdict = dict()
>>> def dfchain(startn):
	global dfchdict
	if startn in dfchdict:
		return dfchdict[startn]
	s = {startn}
	f = startn
	l = False
	while len(s) < 10000 and not l:
		f = digfact(f)
		if f in dfchdict:
			l = len(s) + dfchdict[f]
		if f in s:
			l = len(s)
		s.add(f)
	if l:
		dfchdict[startn] = l
		return l
	return False

>>> dfchain(69)
5
>>> dfchdict
{69: 5}
>>> dfchain(871)
2
>>> dfchdict
{69: 5, 871: 2}
>>> dfchain(78)
4
>>> dfchdict
{69: 5, 78: 4, 871: 2}
>>> len(set(filter(int(60).__eq__,map(dfchain,range(1000000)))))
1
>>> len(dfchdict)
1000000
>>> set(filter(int(60).__eq__,map(dfchain,range(1000000))))
{60}
>>> set(filter((lambda x: dfchain(x) == 60),range(1000000)))
{479232, 4097, 272394, 329742, 243729, 227349, 423972, 272439, 229437, 227394, 923724, 243792, 4179, 479322, 739422, 923742, 229473, 4197, 239724, 272493, 397422, 227439, 247923, 247932, 239742, 374922, 473229, 729234, 432279, 493722, 729243, 942237, 227493, 432297, 372924, 942273, 473292, 372942, 243927, 729324, 327924, 223479, 942327, 729342, 243972, 327942, 342279, 223497, 297234, 342297, 297243, 942372, 723249, 729423, 934227, 379224, 729432, 723294, 237924, 229734, 379242, 297324, 229743, 237942, 297342, 293247, 934272, 932247, 293274, 973224, 932274, 973242, 297423, 297432, 723429, 274923, 422379, 743922, 274932, 422397, 223749, 379422, 723492, 272934, 272943, 223794, 293427, 932427, 924237, 432729, 227934, 293472, 4709, 227943, 973422, 4719, 924273, 932472, 942723, 793224, 942732, 432792, 793242, 924327, 4790, 4791, 324279, 279234, 324297, 342729, 223947, 242379, 279243, 492237, 924372, 242397, 223974, 922347, 492273, 922374, 342792, 279324, 432927, 234279, 492327, 4907, 279342, 4917, 234297, 473922, 934722, 922437, 432972, 793422, 422739, 492372, 9047, 293724, 742239, 273249, 922473, 4970, 4971, 293742, 9074, 932724, 279423, 932742, 279432, 7049, 422793, 273294, 342927, 423927, 742293, 322479, 7094, 742329, 9147, 342972, 439227, 322497, 723924, 9174, 723942, 439272, 7149, 437229, 394227, 742392, 734229, 273429, 947223, 422937, 7194, 232479, 394272, 947232, 349227, 437292, 232497, 242739, 924723, 392247, 924732, 422973, 392274, 273492, 734292, 349272, 732249, 347229, 242793, 922734, 922743, 324729, 947322, 224379, 943227, 732294, 224397, 347292, 943272, 472239, 492723, 429237, 324792, 492732, 322749, 9407, 9417, 429273, 472293, 427239, 234729, 322794, 392427, 7409, 242937, 7419, 9470, 9471, 937224, 472329, 732429, 429327, 724239, 392472, 937242, 242973, 427293, 234792, 232749, 429372, 324927, 427329, 7490, 7491, 724293, 472392, 732492, 232794, 294237, 724329, 324972, 423279, 427392, 294273, 423297, 322947, 974223, 249237, 974232, 322974, 724392, 439722, 722349, 234927, 294327, 249273, 1479, 247239, 972234, 937422, 972243, 374229, 1497, 722394, 234972, 394722, 224739, 294372, 9704, 249327, 9714, 232947, 974322, 292347, 247293, 927234, 273924, 722439, 742923, 9740, 9741, 232974, 927243, 374292, 392724, 273942, 292374, 742932, 224793, 349722, 372249, 249372, 329247, 247329, 972324, 392742, 972342, 329274, 722493, 372294, 497223, 243279, 497232, 327249, 292437, 927324, 247392, 243297, 943722, 927342, 794223, 923247, 794232, 292473, 327294, 972423, 923274, 239247, 972432, 429723, 437922, 429732, 749223, 224937, 239274, 493227, 497322, 792234, 749232, 792243, 927423, 237249, 927432, 734922, 224973, 372429, 794322, 329427, 1749, 493272, 7904, 7914, 237294, 732924, 329472, 1794, 7940, 7941, 327429, 792324, 749322, 372492, 732942, 347922, 792342, 923427, 423729, 743229, 274239, 239427, 294723, 327492, 294732, 923472, 472923, 472932, 792423, 239472, 423792, 792432, 237429, 274293, 249723, 743292, 292734, 249732, 292743, 427923, 739224, 274329, 1947, 427932, 397224, 739242, 237492, 1974, 397242, 724923, 724932, 274392, 272349, 229347, 4079, 722934, 479223, 329724, 229374, 722943}
>>> len(set(filter((lambda x: dfchain(x) == 60),range(1000000))))
402
>>> 
