Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
NameError: name 'sieve' is not defined
>>> def sieve(mx=1000000):
	mx += 1
	nums = set(range(2,mx))
	for i in range(2,mx):
		if i in nums:
			nums.difference_update(range(i+i,mx,i))
	return nums

>>> sieve(100)
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
  File "<pyshell#10>", line 1, in <lambda>
    nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
NameError: name 'tens' is not defined
>>> from math import log10
>>> tens = tuple(map(int(10).__pow__,range(1,9)))
>>> tens
(10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)
>>> tens = tuple(map(int(10).__pow__,range(1,9)))
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
11
>>> nums=sieve(100000);len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
10
>>> nums=sieve(1000000);len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
11
>>> nums=sieve(700000);len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
10
>>> nums=sieve();len(tuple(filter((lambda n:all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
15
>>> nums=sieve();len(tuple(filter((lambda n:all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
KeyboardInterrupt
>>> nums=sieve();sum(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
748317
>>> nums=sieve();len(tuple(filter((lambda n:all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
15
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
11
>>> nums=sieve();sum(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
KeyboardInterrupt
>>> nums=sieve();sum(tuple(filter((lambda n:all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
748334
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
11
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> sieve(100)
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
>>> nums=sieve();len(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
11
>>> nums=sieve();(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
(23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397)
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 
>>> 10 % 6
4
>>> 10 / 6
1.6666666666666667
>>> 10 //
SyntaxError: invalid syntax
>>> 10 // 6
1
>>> divmod(10,6)
(1, 4)
>>> divmod(10,4)
(2, 2)
>>> divmod(40,6)
(6, 4)
>>> divmod(0,6)
KeyboardInterrupt
>>> nums=sieve();(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
KeyboardInterrupt
>>> from timeit import
SyntaxError: invalid syntax
>>> from timeit import Timer
>>> t = Timer(stmt='sum(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums))',setup='nums=sieve()',globals=globals())
>>> t.timeit(10)
1.324605460740192
>>> t.timeit(1)
0.13196097112550476
>>> t.timeit(1)
0.1375064984905645
>>> t.timeit(1)
0.13495931331314637
>>> t.timeit(10)
1.328833216936907
>>> t.timeit(10)
1.3246924791546277
>>> t.timeit(20)
2.67198966488985
>>> t.timeit(20) / 20
0.1335531849855304
>>> t.timeit(20) / 20
0.13337258830695653
>>> t.timeit(100) / 100
0.1351933259107369
>>> divmod(10,6)
(1, 4)
>>> divmod(10,10-4)
(1, 4)
>>> divmod(10,10-4)
(1, 4)
>>> divmod(10,10-4)
(1, 4)
>>> divmod(10,7)
(1, 3)
>>> divmod(10,4)
(2, 2)
>>> divmod(2,2)
(1, 0)
>>> divmod(10,2)
(5, 0)
>>> divmod(10,4)
(2, 2)
>>> divmod(20,2)
(10, 0)
>>> divmod(8,2)
(4, 0)
>>> divmod(20,4)
(5, 0)
>>> divmod(10,5)
(2, 0)
>>> divmod(10,8)
(1, 2)
>>> divmod(10,2)
(5, 0)
>>> divmod(10,6)
(1, 4)
>>> divmod(10-4,4)
(1, 2)
>>> divmod(10-4,6)
(1, 0)
>>> divmod(1,6)
(0, 1)
>>> divmod(1,6)
KeyboardInterrupt
>>> 1 // 6
0
>>> ((1 - 6*l))
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    ((1 - 6*l))
NameError: name 'l' is not defined
>>> l = 0
>>> (10*(1 - 6*l) // 6)
1
>>> (10*(1 - 6*l) // 6)
1
>>> l = 1
>>> (10*(1 - 6*l) // 6)
-9
>>> (10*(1 - 6*l) // 6)
KeyboardInterrupt
>>> (10*(1 - 6*l) // 6)
KeyboardInterrupt
>>> l = 10
>>> (10*(1 - 6*l) // 6)
-99
>>> (10*1 - 6*l) // 6)
SyntaxError: invalid syntax
>>> ((10*1 - 6*l) // 6)
-9
>>> l = 1
>>> ((10*1 - 6*l) // 6)
0
>>> (10*(1 - 6*l) // 6)
-9
>>> l = 0
>>> (10*(1 - 6*l) // 6)
1
>>> (10*(1 - 6*l) // 6) - 6*l
1
>>> (10*(1 - 6*l) // 6) - 6
-5
>>> (10*(1 - 6*l) // 6)
KeyboardInterrupt
>>> divmod(425,25)
(17, 0)
>>> divmod(1,6)
(0, 1)
>>> divmod(10,6)
(1, 4)
>>> divmod(10-4,6)
(1, 0)
>>> divmod(10-6,6)
(0, 4)
>>> divmod(100,6*4)
(4, 4)
>>> divmod(100,6*4)
(4, 4)
>>> divmod(100-6,6*4)
(3, 22)
>>> divmod(6,100)
(0, 6)
>>> divmod(6,1000)
(0, 6)
>>> divmod(6,1000)
(0, 6)
>>> divmod(1000,6)
(166, 4)
>>> divmod(10000,6)
(1666, 4)
>>> divmod(10,6)
(1, 4)
>>> divmod(100,60)
(1, 40)
>>> divmod(100,40)
(2, 20)
>>> 6//1000
0
>>> (2, 20)
KeyboardInterrupt
>>> 6/1000
0.006
>>> divmod(60,10)
(6, 0)
>>> divmod(6,10)
(0, 6)
>>> divmod(60,100)
(0, 60)
>>> divmod(6,10)
(0, 6)
>>> divmod(60,40)
(1, 20)
>>> divmod(60,40)
KeyboardInterrupt
>>> divmod(1,6)
(0, 1)
>>> divmod(10,6)
(1, 4)
>>> divmod((1-0)*10,6*1)
(1, 4)
>>> divmod((1-)*10,6*1)
KeyboardInterrupt
>>> divmod(10,6*1)
(1, 4)
>>> divmod(100,6*4)
(4, 4)
>>> divmod(100,6*4)
KeyboardInterrupt
>>> 1/6*10
1.6666666666666665
>>> 10/60
0.16666666666666666
>>> 10/6
1.6666666666666667
>>> divmod(10,6)
(1, 4)
>>> divmod(100,6)
(16, 4)
>>> 1/6
0.16666666666666666
>>> 10/6
1.6666666666666667
>>> divmod(4,6)
(0, 4)
>>> divmod(40,6)
(6, 4)
>>> a,b = divmod(1,6)
>>> divmod(b*10,6)
(1, 4)
>>> a,b=divmod(b*10,6)
>>> a
1
>>> a,b=divmod(b*10,6)
>>> a
6
>>> a,b=divmod(b*10,6)
>>> a
6
>>> a,b=divmod(b*10,6)
>>> a
6
>>> divmod(1,6)
(0, 1)
>>> divmod(10,6)
(1, 4)
>>> divmod(40,6)
(6, 4)
>>> divmod(40,6)
(6, 4)
>>> divmod(40,6)
(6, 4)
>>> def recip(n):
	b = (0,1)
	count = 0
	rec = []
	while b[1] and count < 100:
		count += 1
		b = divmod(b[1]*10,n)
		rec.append(b)
	return tuple(zip(rec))

>>> recip(2)
(((5, 0),),)
>>> recip(3)
(((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),))
>>> def recip(n):
	b = (0,1)
	count = 0
	rec = []
	while b[1] and count < 100:
		count += 1
		b = divmod(b[1]*10,n)
		rec.append(b)
	return tuple(rec)

>>> recip(3)
((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1))
>>> zip((1,2),(3,4),(5,6))
<zip object at 0x000002154AD82F48>
>>> recip(3)[:]
((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1))
>>> list(zip(recip(3)[:]))
[((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),)]
>>> list(zip(recip(3)))
[((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),), ((3, 1),)]
>>> help(zip)
Help on class zip in module builtins:

class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> def recip(n):
	b = (0,1)
	count = 0
	rec = []
	while b[1] and count < 100:
		count += 1
		b = divmod(b[1]*10,n)
		rec.extend(b)
	return tuple(rec)

>>> recip(3)
(3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1)
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b[1] and count < 100:
		count += 1
		b = divmod(b*10,n)[1]
		rec.append(b)
	return tuple(rec)

>>> recip(3)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    recip(3)
  File "<pyshell#193>", line 5, in recip
    while b[1] and count < 100:
TypeError: 'int' object is not subscriptable
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b[1] and count < 100:
		count += 1
		b = divmod(b*10,n)
		rec.append(b)
	return tuple(rec)

>>> recip(3)
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    recip(3)
  File "<pyshell#196>", line 5, in recip
    while b[1] and count < 100:
TypeError: 'int' object is not subscriptable
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b and count < 100:
		count += 1
		b = divmod(b*10,n)[1]
		rec.append(b)
	return tuple(rec)

>>> recip(3)
(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b and count < 100:
		count += 1
		b = divmod(b*10,n)[0]
		rec.append(b)
	return tuple(rec)

>>> recip(3)
(3, 10, 33, 110, 366, 1220, 4066, 13553, 45176, 150586, 501953, 1673176, 5577253, 18590843, 61969476, 206564920, 688549733, 2295165776, 7650552586, 25501841953, 85006139843, 283353799476, 944512664920, 3148375549733, 10494585165776, 34981950552586, 116606501841953, 388688339473176, 1295627798243920, 4318759327479733, 14395864424932443, 47986214749774810, 159954049165916033, 533180163886386776, 1777267212954622586, 5924224043182075286, 19747413477273584286, 65824711590911947620, 219415705303039825400, 731385684343466084666, 2437952281144886948886, 8126507603816289829620, 27088358679387632765400, 90294528931292109218000, 300981763104307030726666, 1003272543681023435755553, 3344241812270078119185176, 11147472707566927063950586, 37158242358556423546501953, 123860807861854745155006510, 412869359539515817183355033, 1376231198465052723944516776, 4587437328216842413148389253, 15291457760722808043827964176, 50971525869076026812759880586, 169905086230253422709199601953, 566350287434178075697332006510, 1887834291447260252324440021700, 6292780971490867507748133405666, 20975936571636225025827111352220, 69919788572120750086090371174066, 233065961907069166953634570580220, 776886539690230556512115235267400, 2589621798967435188373717450891333, 8632072663224783961245724836304443, 28773575544082613204152416121014810, 95911918480275377347174720403382700, 319706394934251257823915734677942333, 1065687983114170859413052448926474443, 3552293277047236198043508163088248143, 11840977590157453993478360543627493810, 39469925300524846644927868478758312700, 131566417668416155483092894929194375666, 438554725561387184943642983097314585553, 1461849085204623949812143276991048618510, 4872830284015413166040477589970162061700, 16242767613384710553468258633233873539000, 54142558711282368511560862110779578463333, 180475195704274561705202873702598594877776, 601583985680915205684009579008661982925920, 2005279952269717352280031930028873276419733, 6684266507565724507600106433429577588065776, 22280888358552415025333688111431925293552586, 74269627861841383417778960371439750978508620, 247565426206137944725929867904799169928362066, 825218087353793149086432893015997233094540220, 2750726957845977163621442976719990776981800733, 9169089859486590545404809922399969256606002443, 30563632864955301818016033074666564188686674810, 101878776216517672726720110248888547295622249366, 339595920721725575755733700829628490985407497886, 1131986402405751919185779002765428303284691659620, 3773288008019173063952596675884761010948972198733, 12577626693397243546508655586282536703163240662443, 41925422311324145155028851954275122343877468874810, 139751407704413817183429506514250407812924896249366, 465838025681379390611431688380834692709749654164553, 1552793418937931302038105627936115642365832180548510, 5175978063126437673460352093120385474552773935161700, 17253260210421458911534506977067951581842579783872333)
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b and count < 100:
		count += 1
		b = divmod(b*10,n)[1]
		rec.append(b)
	return tuple(rec)

>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b and count < 100:
		count += 1
		a,b = divmod(b*10,n)[1]
		rec.append(a)
	return tuple(rec)

>>> recip(3)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    recip(3)
  File "<pyshell#207>", line 7, in recip
    a,b = divmod(b*10,n)[1]
TypeError: 'int' object is not iterable
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while b and count < 100:
		count += 1
		a,b = divmod(b*10,n)
		rec.append(a)
	return tuple(rec)

>>> recip(3)
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
>>> recip(6)
(1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
>>> def recip(n):
	b = 1
	count = 0
	rec = []
	while (b not in rec) and count < 100:
		count += 1
		a,b = divmod(b*10,n)
		rec.append(a)
	return tuple(rec)

>>> recip(6)
(1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = {}
	while (b not in rem) and count < 100:
		count += 1
		num.append(a)
		rem.add(b)
		a,b = divmod(b*10,n)
	return tuple(rec)

>>> recip(6)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    recip(6)
  File "<pyshell#217>", line 8, in recip
    num.append(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = {}
	while (b not in rem) and count < 100:
		count += 1
		rem.add(b)
		a,b = divmod(b*10,n)
		num.append(a)
	return tuple(rec)

>>> recip(6)
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    recip(6)
  File "<pyshell#220>", line 8, in recip
    rem.add(b)
AttributeError: 'dict' object has no attribute 'add'
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = set()
	while (b not in rem) and count < 100:
		count += 1
		rem.add(b)
		a,b = divmod(b*10,n)
		num.append(a)
	return tuple(rec)

>>> recip(6)
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    recip(6)
  File "<pyshell#223>", line 11, in recip
    return tuple(rec)
NameError: name 'rec' is not defined
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = set()
	while (b not in rem) and count < 100:
		count += 1
		rem.add(b)
		a,b = divmod(b*10,n)
		num.append(a)
	return tuple(num)

>>> recip(6)
(1, 6)
>>> recip(7)
(1, 4, 2, 8, 5, 7)
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while (b not in rem) and count < 100:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	return len(rem)-rem.index(b)

>>> recip(7)
6
>>> recip(2)
1
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while (b not in rem) and count < 100:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	return len(rem)-rem.index(b)
KeyboardInterrupt
>>> divmod(1,8)
(0, 1)
>>> divmod(10,8)
(1, 2)
>>> divmod(20,8)
(2, 4)
>>> divmod(40,8)
(5, 0)
>>> recip(8)
1
>>> a,b = divmod(b*10,n)
KeyboardInterrupt
>>> recip(9)
1
>>> return len(rem)-rem.index(b)
KeyboardInterrupt
>>> def recip(n):
KeyboardInterrupt
>>> a,b = divmod(b*10,n)
KeyboardInterrupt
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 100:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		return len(rem)-rem.index(b)
	else:
		return 0

	
>>> recip(8)
0
>>> recip(2)
0
>>> recip(3)
1
>>> recip(4)
0
>>> recip(6)
1
>>> recip(7)
6
>>> recip(19)
18
>>> recip(11)
2
>>> recip(37)
3
>>> max(map(recip,range(2,1000)))
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    max(map(recip,range(2,1000)))
  File "<pyshell#242>", line 12, in recip
    return len(rem)-rem.index(b)
ValueError: 26 is not in list
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		return len(rem)-rem.index(b)
	else:
		return 0

	
>>> max(map(recip,range(2,1000)))
982
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		return (len(rem)-rem.index(b),n)
	else:
		return (0,n)

	
>>> max(map(recip,range(2,1000)))
(982, 983)
>>> recip(982)
(490, 982)
>>> recip(983)
(982, 983)
>>> 1/983
0.001017293997965412
>>> 
KeyboardInterrupt
>>> max(map(recip,range(2,1000)))
KeyboardInterrupt
>>> Timer(stmt='x=(5)**0.5;y=(5)**0.5').timeit()
0.021083892445403762
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.0485178979029115
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.022618986525685614
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.021128071025032114
>>> Timer(stmt='x=(5)**0.5;y=(5)**0.5').timeit()
0.02330174639246252
>>> Timer(stmt='x=(5)**0.5;y=(5)**0.5').timeit()
0.021640810297412827
>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.021211965701240842
>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.022943409024719585
>>> 6**0.5
2.449489742783178
>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.0389244523976231
>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.021380201302690693
>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.022512333186568867

>>> Timer(stmt='x=(5)**0.5;y=(6)**0.5').timeit()
0.022443610951540904
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.022977323893428547
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.02279480834795322
>>> Timer(stmt='x=(5)**0.5;y=x').timeit()
0.022187910687534895
>>> Timer(stmt='x=(5)**0.5').timeit()
0.015469196596768597
>>> Timer(stmt='x=(5)**0.5').timeit()
0.015744085536880448
>>> Timer(stmt='x=5;x*=2').timeit()
0.03890838745928704
>>> Timer(stmt='x=5;x*=2').timeit()
0.06397504579581437
>>> Timer(stmt='x=5;x*=2').timeit()
0.04036360309783049
>>> Timer(stmt='x=5;x*=2').timeit(1000000000)
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    Timer(stmt='x=5;x*=2').timeit(1000000000)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\timeit.py", line 178, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
KeyboardInterrupt
>>> Timer(stmt='x=5;x*=2').timeit(100000000)
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    Timer(stmt='x=5;x*=2').timeit(100000000)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\timeit.py", line 178, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
KeyboardInterrupt
>>> Timer(stmt='x=5;x*=2').timeit(10000000)
0.38555762069336197
>>> Timer(stmt='x=5;x*=2').timeit(100000000)
3.847590593979021
>>> Timer(stmt='x=5;x*=2').timeit(100000000)
4.1563439770989135
>>> Timer(stmt='x=5;x+=x').timeit(100000000)
3.827136804103702
>>> Timer(stmt='x=5;x+=x').timeit(100000000)
KeyboardInterrupt
>>> def recip(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		return (len(rem)-rem.index(b),n)
	else:
		return (0,n)

	
>>> Timer(stmt='max(map(recip,range(2,1000)))',globals=globals()).timeit()
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    Timer(stmt='max(map(recip,range(2,1000)))',globals=globals()).timeit()
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\timeit.py", line 178, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
  File "<pyshell#290>", line 8, in recip
    rem.append(b)
KeyboardInterrupt
>>> Timer(stmt='max(map(recip,range(2,1000)))',globals=globals()).timeit(10)
3.3220216832037295
>>> Timer(stmt='max(map(recip,range(2,1000)))',globals=globals()).timeit(1)
0.3686238372442858
>>> Timer(stmt='max(map(recip,range(2,1000)))',globals=globals()).timeit(1)
0.33276332553168686
>>> int(True)
1
>>> int(False)
0
>>> int.to_bytes(10)
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    int.to_bytes(10)
TypeError: Required argument 'length' (pos 1) not found
>>> int(10).to_bytes(8)
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    int(10).to_bytes(8)
TypeError: Required argument 'byteorder' (pos 2) not found
>>> int(10).to_bytes(8)
KeyboardInterrupt
>>> int.to_bytes(
KeyboardInterrupt
>>> int(10).to_bytes(8,'big')
b'\x00\x00\x00\x00\x00\x00\x00\n'
>>> int(10).to_bytes(8,'small')
Traceback (most recent call last):
  File "<pyshell#300>", line 1, in <module>
    int(10).to_bytes(8,'small')
ValueError: byteorder must be either 'little' or 'big'
>>> int(10).to_bytes(8,'little')
b'\n\x00\x00\x00\x00\x00\x00\x00'
>>> int(10).to_bytes(1,'little')
b'\n'
>>> bytes(int(10).to_bytes(1,'little'))
b'\n'
>>> bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> list(bytes(10))
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> list(bytes(3))
[0, 0, 0]
>>> bytes(range(7))
b'\x00\x01\x02\x03\x04\x05\x06'
>>> list(bytes(range(7)))
[0, 1, 2, 3, 4, 5, 6]
>>> list((range(7)))
[0, 1, 2, 3, 4, 5, 6]
>>> int(7,2)
Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    int(7,2)
TypeError: int() can't convert non-string with explicit base
>>> list(filter(bytes(3)))
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    list(filter(bytes(3)))
TypeError: filter expected 2 arguments, got 1
>>> list(filter(bytes(3),None))
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    list(filter(bytes(3),None))
TypeError: 'NoneType' object is not iterable
>>> list(filter(bool,bytes(3)))
[]
>>> list(filter(None,bytes(3)))
[]
>>> [1,2,3]*[1,10,100]
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    [1,2,3]*[1,10,100]
TypeError: can't multiply sequence by non-int of type 'list'
>>> str(7, bytes)
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    str(7, bytes)
TypeError: str() argument 2 must be str, not type
>>> str(7, 'bin')
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    str(7, 'bin')
TypeError: coercing to str: need a bytes-like object, int found
>>> str(7)
'7'
>>> int(str(7),2)
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    int(str(7),2)
ValueError: invalid literal for int() with base 2: '7'
>>> int('1011',2)
11
>>> int('1011',2)
11
>>> bin(7)
'0b111'
>>> int(bin(7))
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    int(bin(7))
ValueError: invalid literal for int() with base 10: '0b111'
>>> int(bin(7)[2:])
111
>>> map((lambda n: int(bin(n)[2:])),range(7))
<map object at 0x000002154AD86E80>
>>> list(map((lambda n: int(bin(n)[2:])),range(7)))
[0, 1, 10, 11, 100, 101, 110]
>>> primes = sieve()
>>> primes = sieve(10000000)
>>> primestrs = set(map(str,primes))
>>> len(primes)
664579
>>> len(primestrs)
664579
>>> psdict = dict(
	map(str,primes))
Traceback (most recent call last):
  File "<pyshell#332>", line 2, in <module>
    map(str,primes))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> psdict = dict(map(lambda n:(n,str(n)),primes))
>>> len(psdict)
664579
>>> psdict[7]
'7'
>>> psdict['7']
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    psdict['7']
KeyError: '7'
>>> psdict = dict(map(lambda n:(n,str(n)),primes))
KeyboardInterrupt
>>> psdict.update(dict(map(lambda n:(str(n),n),primes)))
>>> psdict['7']
7
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'012'))),primes)

	      
KeyboardInterrupt
>>> int(100).__lt__(9)
False
>>> int(100).__gt__(9)
True
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'012'))),filter(int(100).__gt__,primes)))
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'012'))),filter(int(10000).__gt__,primes)))
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'012'))),filter(int(1000000).__gt__,primes)))
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'012'))),primes))
>>> 56003 in repeats
True
>>> len(primes)
664579
>>> len(repeats)
596897
>>> rp0 = set(filter(lambda n:(len(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    rp0 = set(filter(lambda n:(len(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
  File "<pyshell#352>", line 1, in <lambda>
    rp0 = set(filter(lambda n:(len(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
TypeError: object of type 'filter' has no len()
>>> rp0 = set(filter(lambda n:(len(map(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
Traceback (most recent call last):
  File "<pyshell#353>", line 1, in <module>
    rp0 = set(filter(lambda n:(len(map(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
  File "<pyshell#353>", line 1, in <lambda>
    rp0 = set(filter(lambda n:(len(map(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890')))>=8),filter(int(10000).__gt__,primes)))
TypeError: object of type 'map' has no len()

>>> rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(10000).__gt__,primes)))
>>> rp0
{2, 3, 5, 7, 6151, 11, 13, 4111, 17, 19, 6163, 23, 8219, 29, 6173, 31, 4127, 4129, 8221, 37, 4133, 8231, 41, 8233, 43, 4139, 8237, 47, 8243, 53, 6197, 6199, 4153, 59, 61, 4157, 2111, 4159, 2113, 67, 6211, 71, 8263, 73, 6217, 6221, 8269, 79, 2129, 4177, 83, 2131, 6229, 8273, 89, 2137, 2141, 2143, 8287, 97, 8291, 8293, 6247, 2153, 8297, 113, 2161, 4211, 6257, 6263, 8311, 4217, 4219, 6269, 8317, 127, 6271, 131, 2179, 4229, 6277, 4231, 137, 8329, 139, 6287, 4241, 4243, 149, 151, 6299, 157, 4253, 8353, 163, 4259, 2213, 4261, 167, 6311, 8363, 173, 2221, 4271, 6317, 4273, 8369, 179, 6323, 181, 6329, 8377, 4283, 2237, 191, 2239, 193, 4289, 2243, 6337, 197, 8387, 199, 6343, 4297, 8389, 2251, 6353, 211, 6359, 6361, 2267, 2269, 223, 6367, 2273, 227, 8419, 229, 6373, 4327, 8423, 233, 2281, 6379, 8429, 239, 2287, 241, 4337, 4339, 8431, 2293, 6389, 2297, 251, 8191, 4349, 6397, 8443, 8447, 257, 4357, 263, 2311, 4363, 269, 8461, 271, 8467, 277, 4373, 6421, 281, 283, 6427, 2333, 2339, 293, 2341, 4391, 2347, 4397, 2351, 6449, 6451, 2357, 311, 313, 317, 8513, 2371, 4421, 6469, 4423, 2377, 6473, 331, 8521, 2381, 2383, 8527, 337, 6481, 2389, 2393, 4441, 347, 6491, 349, 8537, 2399, 4447, 353, 8539, 4451, 8543, 359, 4457, 2411, 367, 4463, 2417, 8563, 373, 2423, 6521, 379, 8573, 383, 4481, 6529, 4483, 389, 2437, 8581, 2441, 397, 4493, 2447, 6547, 8597, 6551, 8599, 6553, 2459, 4513, 419, 2467, 421, 4517, 4519, 6563, 2473, 6569, 4523, 6571, 2477, 431, 8623, 433, 6577, 8627, 6581, 8629, 439, 443, 449, 8641, 4547, 4549, 6599, 8647, 457, 461, 463, 4561, 467, 4567, 8663, 2521, 6619, 8669, 479, 2531, 8677, 487, 4583, 8681, 491, 2539, 6637, 2543, 4591, 8689, 499, 2549, 4597, 2551, 8693, 8699, 2557, 6653, 6659, 6661, 521, 8713, 523, 4621, 8719, 6673, 2579, 6679, 8731, 541, 4637, 2591, 4639, 2593, 6689, 547, 4643, 6691, 8737, 8741, 4649, 4651, 8747, 557, 4657, 8753, 563, 4663, 569, 2617, 571, 8761, 2621, 6719, 577, 4673, 4679, 2633, 587, 8779, 6733, 8783, 593, 6737, 4691, 599, 2647, 2657, 2659, 613, 2663, 617, 6761, 619, 6763, 2671, 4721, 4723, 8819, 2677, 8821, 631, 4729, 2683, 6779, 4733, 6781, 2687, 8831, 641, 2689, 643, 2693, 8837, 647, 6791, 6793, 8839, 2699, 653, 4751, 8849, 659, 661, 2711, 4759, 2713, 8861, 2719, 8863, 673, 8867, 677, 6823, 2729, 683, 2731, 6827, 6829, 4783, 6833, 691, 4787, 2741, 4789, 8887, 4793, 6841, 2749, 8893, 4799, 2753, 6857, 4813, 719, 2767, 4817, 6863, 6869, 727, 6871, 2777, 8923, 733, 4831, 8929, 739, 6883, 2789, 8933, 743, 2791, 2797, 8941, 751, 6899, 757, 8951, 761, 4861, 6911, 769, 2819, 8963, 773, 6917, 4871, 8969, 8971, 4877, 2833, 787, 2837, 4889, 2843, 797, 2851, 6947, 6949, 8999, 2857, 811, 2861, 6959, 6961, 821, 823, 4919, 6967, 827, 6971, 829, 2879, 6977, 4931, 4933, 839, 2887, 4937, 6983, 4943, 6991, 2897, 853, 6997, 4951, 857, 859, 4957, 863, 2917, 4967, 4969, 877, 4973, 2927, 881, 883, 887, 2939, 4987, 4993, 4999, 2953, 2957, 911, 2963, 919, 2969, 2971, 929, 9127, 937, 941, 9133, 9137, 947, 2999, 953, 9151, 9157, 967, 9161, 971, 977, 7121, 9173, 983, 7127, 7129, 9181, 991, 9187, 997, 7151, 9199, 7159, 5113, 5119, 9221, 7177, 9227, 7187, 9239, 7193, 9241, 5147, 5153, 9257, 7211, 7213, 3119, 5167, 3121, 5171, 7219, 5179, 7229, 9277, 3137, 9281, 9283, 5189, 7237, 7243, 5197, 9293, 7247, 7253, 3163, 1117, 3167, 9311, 3169, 1123, 9319, 1129, 5227, 9323, 3181, 5231, 5233, 3187, 7283, 5237, 3191, 9337, 9341, 1151, 9343, 1153, 7297, 9349, 1163, 5261, 3217, 1171, 3221, 5273, 7321, 9371, 1181, 3229, 5279, 5281, 9377, 1187, 7331, 7333, 1193, 9391, 5297, 3251, 3253, 7349, 7351, 9397, 3257, 3259, 1213, 1217, 9413, 1223, 3271, 7369, 5323, 9419, 1229, 9421, 1231, 1237, 5333, 9431, 9433, 9437, 9439, 1249, 7393, 3299, 5347, 5351, 1259, 3313, 7411, 9461, 3319, 9463, 7417, 3323, 9467, 1277, 1279, 3329, 9473, 1283, 3331, 5381, 9479, 1289, 7433, 1291, 5387, 3343, 1297, 5393, 3347, 9491, 5399, 9497, 7451, 3359, 3361, 7457, 7459, 5413, 1319, 9511, 1321, 5417, 3371, 5419, 3373, 1327, 9521, 7477, 5431, 7481, 3389, 5437, 3391, 7487, 5441, 7489, 5443, 9533, 9539, 5449, 7499, 9547, 9551, 1361, 3413, 1367, 1373, 7517, 5471, 7523, 1381, 5477, 5479, 3433, 7529, 5483, 7537, 9587, 7541, 1399, 3449, 7547, 7549, 3457, 3461, 3463, 7559, 7561, 3467, 3469, 9613, 1423, 5519, 5521, 1427, 9619, 1429, 7573, 5527, 9623, 1433, 7577, 5531, 9629, 1439, 7583, 9631, 3491, 7589, 1447, 7591, 1451, 3499, 1453, 9643, 9649, 1459, 5557, 3511, 5563, 3517, 9661, 1471, 5569, 5573, 7621, 3527, 1481, 3529, 1483, 3533, 5581, 1487, 9677, 1489, 9679, 3539, 1493, 3541, 5591, 7639, 9689, 1499, 3547, 7643, 7649, 9697, 3557, 1511, 3559, 1523, 3571, 7669, 5623, 9719, 7673, 9721, 1531, 3581, 3583, 7681, 9733, 1543, 5639, 3593, 5641, 7687, 7691, 1549, 9739, 5647, 9743, 1553, 5651, 7699, 5653, 9749, 1559, 5657, 5659, 3613, 1567, 3617, 1571, 5669, 7717, 3623, 9767, 9769, 1579, 7723, 1583, 3631, 7727, 5683, 3637, 9781, 5689, 3643, 9787, 1597, 5693, 7741, 9791, 7753, 3659, 1613, 7757, 5711, 7759, 1619, 9811, 1621, 5717, 3671, 3673, 9817, 1627, 3677, 1637, 9829, 5737, 9833, 3691, 5741, 7789, 5743, 9839, 3697, 7793, 5749, 1657, 9851, 1663, 9857, 1667, 9859, 1669, 3719, 7817, 3727, 7823, 9871, 5779, 3733, 7829, 5783, 3739, 9883, 1693, 5791, 9887, 1697, 7841, 1699, 7853, 3761, 5813, 3767, 1721, 3769, 1723, 7867, 5821, 7873, 3779, 5827, 1733, 7877, 7879, 9923, 9929, 7883, 9931, 1741, 5839, 3793, 1747, 5843, 3797, 9941, 1753, 5849, 5851, 9949, 1759, 5857, 5861, 5867, 3821, 5869, 3823, 7919, 1777, 9967, 9973, 1783, 5879, 3833, 5881, 1787, 7927, 1789, 7933, 7937, 3847, 5897, 3851, 3853, 7949, 7951, 1811, 3863, 7963, 1823, 5923, 3877, 1831, 5927, 3881, 3889, 5939, 1847, 7993, 5953, 1861, 3911, 1867, 3917, 1871, 3919, 1873, 3923, 1877, 1879, 3929, 3931, 5981, 1889, 5987, 3943, 3947, 1913, 3967, 1931, 1933, 3989, 1949, 1951, 8111, 1973, 8117, 1979, 8123, 1987, 1993, 1997, 1999, 8147, 6113, 8161, 8167, 6121, 8171, 6131, 8179, 6133, 6143}
>>> rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(10000).__gt__,repeats)))
>>> len(rp0)
649
>>> rp0
{2, 6151, 11, 13, 4111, 17, 19, 6163, 23, 8219, 29, 6173, 31, 4127, 4129, 8221, 4133, 8231, 41, 8233, 4139, 8237, 8243, 6197, 6199, 4153, 61, 4157, 2111, 4159, 2113, 6211, 71, 8263, 6217, 6221, 8269, 2129, 4177, 2131, 8273, 6229, 2137, 2141, 2143, 8287, 8291, 8293, 6247, 2153, 8297, 113, 2161, 4211, 6257, 6263, 8311, 4217, 4219, 6269, 8317, 127, 6271, 131, 2179, 4229, 6277, 4231, 137, 8329, 139, 6287, 4241, 4243, 149, 151, 6299, 157, 4253, 163, 4259, 2213, 4261, 167, 6311, 173, 2221, 4271, 6317, 4273, 179, 6323, 181, 6329, 4283, 2237, 191, 2239, 193, 4289, 2243, 197, 199, 4297, 2251, 211, 6361, 2267, 2269, 223, 2273, 227, 8419, 229, 4327, 8423, 233, 2281, 8429, 239, 2287, 241, 8431, 2293, 2297, 251, 8191, 257, 263, 2311, 269, 8461, 271, 277, 6421, 281, 283, 6427, 2333, 2339, 293, 2341, 4391, 2347, 2351, 6451, 2357, 311, 313, 317, 8513, 2371, 4421, 4423, 2377, 8521, 331, 2381, 2383, 8527, 6481, 2389, 2393, 4441, 6491, 2399, 4451, 2411, 2417, 2423, 6521, 4481, 6529, 2437, 8581, 2441, 2447, 6551, 2459, 4513, 419, 2467, 421, 4517, 4519, 2473, 4523, 6571, 2477, 431, 8623, 8627, 6581, 8629, 8641, 461, 4561, 2521, 6619, 2531, 8681, 491, 2539, 2543, 4591, 2549, 2551, 2557, 6661, 521, 8713, 523, 4621, 8719, 2579, 8731, 541, 2591, 2593, 6691, 8741, 4651, 2617, 8761, 571, 2621, 6719, 2633, 4691, 2647, 2657, 2659, 613, 2663, 617, 6761, 619, 2671, 4721, 4723, 8819, 2677, 8821, 631, 4729, 2683, 6781, 2687, 8831, 641, 2689, 2693, 6791, 2699, 4751, 661, 2711, 2713, 8861, 2719, 6823, 2729, 2731, 6827, 6829, 691, 2741, 6841, 2749, 2753, 4813, 719, 2767, 4817, 727, 6871, 2777, 8923, 4831, 8929, 2789, 2791, 2797, 8941, 751, 8951, 761, 4861, 6911, 2819, 6917, 4871, 8971, 2833, 2837, 2843, 2851, 2857, 811, 2861, 6961, 821, 823, 4919, 827, 6971, 829, 2879, 4931, 2887, 6991, 2897, 4951, 2917, 2927, 881, 2939, 2953, 2957, 911, 2963, 919, 2969, 2971, 929, 9127, 941, 9133, 9137, 2999, 9151, 9157, 9161, 971, 7121, 9173, 7127, 7129, 9181, 991, 9187, 7151, 9199, 7159, 5113, 5119, 9221, 7177, 9227, 7187, 9239, 7193, 9241, 5147, 5153, 9257, 7211, 7213, 3119, 5167, 3121, 5171, 7219, 5179, 7229, 9277, 3137, 9281, 9283, 5189, 7237, 7243, 5197, 9293, 7247, 7253, 3163, 1117, 3167, 9311, 3169, 1123, 9319, 1129, 5227, 9323, 3181, 5231, 5233, 3187, 7283, 5237, 3191, 9341, 1151, 1153, 7297, 1163, 5261, 3217, 1171, 3221, 5273, 7321, 9371, 1181, 3229, 5279, 5281, 1187, 7331, 1193, 9391, 5297, 3251, 3253, 7351, 3257, 3259, 1213, 1217, 9413, 1223, 3271, 5323, 9419, 1229, 9421, 1231, 1237, 9431, 1249, 3299, 5351, 1259, 3313, 7411, 9461, 3319, 7417, 3323, 1277, 1279, 3329, 1283, 3331, 5381, 1289, 1291, 1297, 9491, 7451, 3361, 5413, 1319, 9511, 1321, 5417, 3371, 5419, 1327, 9521, 5431, 7481, 3391, 5441, 9551, 1361, 3413, 1367, 1373, 7517, 5471, 7523, 1381, 7529, 7541, 1399, 3461, 7561, 9613, 1423, 5519, 5521, 1427, 9619, 1429, 5527, 9623, 1433, 5531, 9629, 1439, 9631, 3491, 1447, 7591, 1451, 1453, 1459, 3511, 3517, 9661, 1471, 7621, 3527, 1481, 3529, 1483, 5581, 1487, 1489, 1493, 3541, 5591, 1499, 1511, 1523, 3571, 5623, 9719, 9721, 1531, 3581, 7681, 1543, 5641, 7691, 1549, 1553, 5651, 1559, 3613, 1567, 3617, 1571, 7717, 3623, 1579, 7723, 1583, 3631, 7727, 9781, 1597, 7741, 9791, 1613, 5711, 1619, 9811, 1621, 5717, 3671, 9817, 1627, 1637, 9829, 3691, 5741, 1657, 9851, 1663, 1667, 1669, 3719, 7817, 3727, 7823, 9871, 7829, 1693, 5791, 1697, 7841, 1699, 3761, 5813, 1721, 1723, 5821, 5827, 9923, 1733, 9929, 9931, 1741, 1747, 9941, 1753, 5851, 1759, 5861, 3821, 3823, 7919, 1777, 1783, 7927, 5881, 1787, 1789, 3851, 7951, 1811, 1823, 5923, 1831, 5927, 3881, 1847, 1861, 3911, 1867, 3917, 1871, 3919, 1873, 3923, 1877, 1879, 3929, 3931, 5981, 1889, 1913, 1931, 1933, 1949, 1951, 8111, 1973, 8117, 1979, 8123, 1987, 1993, 1997, 1999, 8147, 6113, 8161, 8167, 6121, 8171, 6131, 8179, 6133, 6143}
>>> repeats = set(filter(lambda n:(any(map(psdict[n].count,'0'))),primes))
>>> rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(10000).__gt__,repeats)))
>>> len(rp0)
0
>>> rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))
>>> len(rp0)
0
>>> rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(10000000).__gt__,repeats)))
>>> len(rp0)
3
>>> rp0
{5074009, 2090021, 4004509}
>>> list(map((lambda x:psdict[str(2090021).replace('0',x)],'0123456789')))
Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    list(map((lambda x:psdict[str(2090021).replace('0',x)],'0123456789')))
TypeError: map() must have at least two arguments.
>>> list(map((lambda x:psdict[str(2090021).replace('0',x)]),'0123456789'))
Traceback (most recent call last):
  File "<pyshell#368>", line 1, in <module>
    list(map((lambda x:psdict[str(2090021).replace('0',x)]),'0123456789'))
  File "<pyshell#368>", line 1, in <lambda>
    list(map((lambda x:psdict[str(2090021).replace('0',x)]),'0123456789'))
KeyError: '2393321'
>>> list(map((lambda x:int(str(2090021).replace('0',x))),'0123456789'))
[2090021, 2191121, 2292221, 2393321, 2494421, 2595521, 2696621, 2797721, 2898821, 2999921]
>>> list(filter(primes.__contains__,map((lambda x:int(str(2090021).replace('0',x))),'0123456789')))
[2090021, 2191121, 2292221, 2494421, 2595521, 2696621, 2898821, 2999921]
>>> len(primes)
664579
>>> max(primes)
9999991
>>> def isprime(n):
	sq = int(n**0.5)+1
	return not any(n.__mod__,range(2,sq))

>>> isprime(7)
Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    isprime(7)
  File "<pyshell#376>", line 3, in isprime
    return not any(n.__mod__,range(2,sq))
TypeError: any() takes exactly one argument (2 given)
>>> def isprime(n):
	sq = int(n**0.5)+1
	return not any(map(n.__mod__,range(2,sq)))

>>> isprime(7)
False
>>> isprime(6)
True
>>> def isprime(n):
	sq = int(n**0.5)+1
	return all(map(n.__mod__,range(2,sq)))

>>> isprime(9999991)
True
>>> isprime(2090021)
True
>>> for c in '012':
	repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
	rp0 = set(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace('0',x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))

	
Traceback (most recent call last):
  File "<pyshell#389>", line 2, in <module>
    repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
  File "<pyshell#389>", line 2, in <lambda>
    repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
KeyboardInterrupt
>>> def find():
	rp = set()
	for c in '012':
		repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
		rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))

		
>>> find()
Traceback (most recent call last):
  File "<pyshell#393>", line 1, in <module>
    find()
  File "<pyshell#392>", line 5, in find
    rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))
  File "<pyshell#392>", line 5, in <lambda>
    rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))
  File "<pyshell#392>", line 5, in <lambda>
    rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))
KeyboardInterrupt
>>> def find():
	rp = set()
	for c in '012':
		repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
		rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'1234567890'))))>=8),filter(int(1000000).__gt__,repeats)))
	return rp

>>> rp = find()
>>> len(rp)
1
>>> rp
{121313}
>>> def find():
	rp = set()
	for c in '012':
		repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
		rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'0123456789'))))>=8),repeats)
	return rp
			  
SyntaxError: invalid syntax
>>> def find():
	rp = set()
	for c in '012':
		repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
		rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'0123456789'))))>=8),repeats))
	return rp

>>> rp = find()
>>> len(rp)
9
>>> rp
{121313, 2090021, 5174119, 5282029, 4224529, 4114519, 5074009, 5181019, 4004509}
>>> min(rp)
121313
>>> list(map((lambda x:psdict[str(2090021).replace('0',x)],'0123456789')))
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    list(map((lambda x:psdict[str(2090021).replace('0',x)],'0123456789')))
TypeError: map() must have at least two arguments.
>>> def find():
	rp = set()
	for c in '012':
		repeats = set(filter(lambda n:(any(map(psdict[n].count,c))),primes))
		rp.update(filter(lambda n:(len(tuple(filter(psdict.__contains__,map((lambda x:psdict[n].replace(c,x)),'0123456789'))))>=8),repeats))
	return rp
KeyboardInterrupt
>>> list(filter(primes.__contains__,map((lambda x:int(str(min(rp)).replace('0',x))),'0123456789')))
[121313, 121313, 121313, 121313, 121313, 121313, 121313, 121313, 121313, 121313]
>>> list(filter(primes.__contains__,map((lambda x:int(str(min(rp)).replace('1',x))),'0123456789')))
[121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
>>> 10 // 6
1
>>> 10 % 6
4
>>> 40 % 6
4
>>> 40 // 6
6
>>> 10 % 7
3
>>> for i in range(6):
	
KeyboardInterrupt
>>> 1//7
0
>>> 1%7
1
>>> a,b=(0,1)
>>> for i in range(6):
	a = (10*b) // 7
	b = (10*b) % 7
	print(a)

	
1
4
2
8
5
7
>>> recip(19)
(18, 19)
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		return num
	else:
		return None

	
>>> recip_full(7)
[1, 4, 2, 8, 5, 7]
>>> recip_full(6)
[1, 6]
>>> recip_full(5)
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(...)
	return num

>>> recip_full(5)
[2]
>>> recip_full(6)
[1, 6, Ellipsis]
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(num[num.index(b):])
	return num

>>> recip_full(6)
Traceback (most recent call last):
  File "<pyshell#439>", line 1, in <module>
    recip_full(6)
  File "<pyshell#438>", line 12, in recip_full
    num.append(num[num.index(b):])
ValueError: 4 is not in list
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(num[num.index(a):])
	return num

>>> recip_full(6)
[1, 6, [6]]
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(tuple(num[num.index(a):]))
	return num

>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(tuple(num[num.index(a):]))
	return num
KeyboardInterrupt
>>> recip_full(6)
[1, 6, (6,)]
>>> recip_full(7)
[1, 4, 2, 8, 5, 7, (7,)]
>>> num.append(tuple(num[num.index(a):]))
KeyboardInterrupt
>>> if b:
KeyboardInterrupt
>>> 
>>> count += 1
KeyboardInterrupt
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		num.append(tuple(num[rem.index(b):]))
	return num

>>> recip_full(6)
[1, 6, (6,)]
>>> recip_full(7)
[1, 4, 2, 8, 5, 7, (1, 4, 2, 8, 5, 7)]
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		i = rem.index(b)
		return num[:i] + [tuple(num[i:])]
	else:
		return num

	
>>> recip_full(7)
[(1, 4, 2, 8, 5, 7)]
>>> recip_full(1)
[10]
>>> recip_full(6)
[1, (6,)]
>>> recip_full(6)
KeyboardInterrupt
>>> def recip_full(n):
	b = 1
	count = 0
	num = []
	rem = []
	while b and (b not in rem) and count < 1000:
		count += 1
		rem.append(b)
		a,b = divmod(b*10,n)
		num.append(a)
	if b:
		i = rem.index(b)
		return num[:i] + [list(num[i:])]
	else:
		return num

	
>>> recip_full(6)
[1, [6]]
>>> recip_full(7)
[[1, 4, 2, 8, 5, 7]]
>>> recip_full(19)
[[0, 5, 2, 6, 3, 1, 5, 7, 8, 9, 4, 7, 3, 6, 8, 4, 2, 1]]
>>> recip_full(9)
[[1]]
>>> recip_full(11)
[[0, 9]]
>>> recip_full(15)
[0, [6]]
>>> recip_full(15)
[0, [6]]
>>> 0.066666666666*15
0.9999999999900001
>>> recip_full(5)
[2]
>>> len(recip_full(19)[-1])
18
>>> len(recip_full(23)[-1])
22
>>> len(recip_full(22)[-1])
2
>>> len(recip_full(91)[-1])
6
>>> len(recip_full(97)[-1])
96
>>> recip_full(97)
[[0, 1, 0, 3, 0, 9, 2, 7, 8, 3, 5, 0, 5, 1, 5, 4, 6, 3, 9, 1, 7, 5, 2, 5, 7, 7, 3, 1, 9, 5, 8, 7, 6, 2, 8, 8, 6, 5, 9, 7, 9, 3, 8, 1, 4, 4, 3, 2, 9, 8, 9, 6, 9, 0, 7, 2, 1, 6, 4, 9, 4, 8, 4, 5, 3, 6, 0, 8, 2, 4, 7, 4, 2, 2, 6, 8, 0, 4, 1, 2, 3, 7, 1, 1, 3, 4, 0, 2, 0, 6, 1, 8, 5, 5, 6, 7]]
>>> ''.join(recip_full(97)[-1])
Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    ''.join(recip_full(97)[-1])
TypeError: sequence item 0: expected str instance, int found
>>> ''.join(map(str,recip_full(97)[-1]))
'010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567'
>>> ''.join('0.',map(str,recip_full(97)[-1]))
Traceback (most recent call last):
  File "<pyshell#476>", line 1, in <module>
    ''.join('0.',map(str,recip_full(97)[-1]))
TypeError: join() takes exactly one argument (2 given)
>>> ''.join(['0.']+list(map(str,recip_full(97)[-1]))+['...'])
'0.010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567...'
>>> 97*0.010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567
1.0
>>> 97*0.01030927835051546391752577319587628865979381443298969072164948453608247422680412371134020618556
1.0
>>> ''.join(['0.']+list(map(str,recip_full(97)[-1]))+['...'])
'0.010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567...'
>>> len(recip_full(7)[-1])
6
>>> recip_full(96)
[0, 1, 0, 4, 1, [6]]
>>> len(recip_full(7)[-1])
6
>>> recip_full(13)
[[0, 7, 6, 9, 2, 3]]
>>> recip_full(14)
[0, [7, 1, 4, 2, 8, 5]]
>>> recip_full(15)
[0, [6]]
>>> recip_full(17)
[[0, 5, 8, 8, 2, 3, 5, 2, 9, 4, 1, 1, 7, 6, 4, 7]]
>>> recip_full(18)
[0, [5]]
>>> recip_full(21)
[[0, 4, 7, 6, 1, 9]]
>>> recip_full(12)
[0, 8, [3]]
>>> recip_full(24)
[0, 4, 1, [6]]
>>> recip_full(22)
[0, [4, 5]]
>>> recip_full(66)
[0, [1, 5]]
>>> recip_full(44)
[0, 2, [2, 7]]
>>> 1/44
0.022727272727272728
>>> recip_full(44)
[0, 2, [2, 7]]
>>> recip(44)
(2, 44)
>>> 10**6-1 / 7
999999.8571428572
>>> (10**6 - 1) / 7
142857.0
>>> (10**6 - 1) / 6
166666.5
>>> (10**12 - 1) / 13
76923076923.0
>>> (10**12 - 1) / 44
22727272727.25
>>> (10**45 - 1) / 44
2.2727272727272725e+43
>>> 
KeyboardInterrupt
>>> recip_full(44)
[0, 2, [2, 7]]
>>> recip_full(7)
[[1, 4, 2, 8, 5, 7]]
>>> recip_full(12)
[0, 8, [3]]
>>> 2**32 - 1
4294967295
>>> 2**32 - 1
4294967295
>>> 10**12
1000000000000
>>> 2**64 - 1
18446744073709551615
>>> log10(2**64 - 1)
19.265919722494797
>>> 2**64 - 1
18446744073709551615
>>> log10(2**64 - 1)
19.265919722494797
>>> log10(2**64 - 1)
19.265919722494797
>>> 10**1000
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 10**1000 // 7
1428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428
>>> int(math.log2(10**1000))
Traceback (most recent call last):
  File "<pyshell#517>", line 1, in <module>
    int(math.log2(10**1000))
NameError: name 'math' is not defined
>>> import math
>>> int(math.log2(10**1000))
3321
>>> int(math.log2(10**1000)) // 8
415
>>> int(math.log2(10**1000)) / 8
415.125
>>> math.ceil(int(math.log2(10**1000)) / 8)
416
>>> math.ceil(math.log2(10**1000))
3322
>>> math.ceil(math.log2(10**1000)) / 8
415.25
>>> int(math.log2(10**984))
3268
>>> math.ceil(math.log2(10**984))
3269
>>> 3269 / 8]
SyntaxError: invalid syntax
>>> 3269 / 8
408.625
>>> from math import log2
>>> 3269*log2(3269)*log2(log2(3269))
135304.372480961
>>> f = lambda x: x*log2(x)
>>> f(3269)
38164.37744031719
>>> f(f(3269))
580859.4980260794
>>> 150 % 5
0
>>> 151 % 5
1
>>> f = lambda x: x*log2(x)*log2(log2(x))
>>> f(1000)
33056.34050569791
>>> f(409*8)
135450.14165280326
>>> [1,2,3,4]*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> l
0
>>> q = [1,2,3,4]
>>> len(q)*q
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> z = \(10**1000)/(9999999999999999999)
SyntaxError: unexpected character after line continuation character
>>> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
KeyboardInterrupt
>>> z = (10**1000)/(9999999999999999999)
Traceback (most recent call last):
  File "<pyshell#546>", line 1, in <module>
    z = (10**1000)/(9999999999999999999)
OverflowError: integer division result too large for a float
>>> divmod(15,6)
(2, 3)
>>> recip_full(12)
[0, 8, [3]]
>>> mod(10**1,12)
Traceback (most recent call last):
  File "<pyshell#549>", line 1, in <module>
    mod(10**1,12)
NameError: name 'mod' is not defined
>>> (10**1 % 12)
10
>>> (10**2 % 11)
1
>>> (10**2 % 11)
1
>>> 
>>> 
>>> (10**1 % 12)
10
>>> (10**1 % 12)
KeyboardInterrupt
>>> recip_full(13)
[[0, 7, 6, 9, 2, 3]]
>>> len(recip_full(13)[-1])
6
>>> (10**6 % 13)
1
>>> filter(int(12).__mod__,range(2,12))
<filter object at 0x000002154AD86E48>
>>> list(filter(int(12).__mod__,range(2,12)))
[5, 7, 8, 9, 10, 11]
>>> len(list(filter(int(12).__mod__,range(2,12))))
6
>>> 40//6
6
>>> x
Traceback (most recent call last):
  File "<pyshell#563>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = 1
>>> x += 1
>>> lambda x: x+=1; x
SyntaxError: can't assign to lambda
>>> class Test:
	def __init__(self,n):
		self.n = n
		
	def __int__(self):
		return int(n)

	
>>> class Test:
	def __init__(self,n):
		self.n = n

	def __int__(self):
		return int(n)
	def __iadd__(self, other):
		self.n += other
		return self.n

	
>>> x = Test(0)
>>> x += 1
>>> x
1
>>> type(x)
<class 'int'>
>>> class Test:
	def __init__(self,n):
		self.n = n
	def __int__(self):
		return int(n)
	def __iadd__(self, other):
		self.n += other
		return self.n

	
>>> Test()
Traceback (most recent call last):
  File "<pyshell#586>", line 1, in <module>
    Test()
TypeError: __init__() missing 1 required positional argument: 'n'
>>> Test(0)
<__main__.Test object at 0x0000021569C95DD8>
>>> x=Test(0)
>>> x
<__main__.Test object at 0x00000215643AD5F8>
>>> x+=1
>>> x
1
>>> class Test:
	def __init__(self,n):
		self.n = n
	def __int__(self):
		return int(n)
	def __iadd__(self, other):
		self.n += other
		return self

	
>>> x=Test(0)
>>> x
<__main__.Test object at 0x00000215643AAF98>
>>> x+=1
>>> x
<__main__.Test object at 0x00000215643AAF98>
>>> f = lambda x,y: x+y
>>> f(1,2)
3
>>> map(f,[1,2],[3,4])
<map object at 0x00000215643AD3C8>
>>> list(map(f,[1,2],[3,4]))
[4, 6]
>>> list(map(lambda x: map(print,x),['hello','from','the']))
[<map object at 0x00000215643ADC18>, <map object at 0x00000215643AD4A8>, <map object at 0x00000215643AD8D0>]
>>> list(map((lambda x: list(map(print,x))),['hello','from','the']))
h
e
l
l
o
f
r
o
m
t
h
e
[[None, None, None, None, None], [None, None, None, None], [None, None, None]]
>>> list(map((lambda x: list(map(print,x))),['hello','from','the']))
h
e
l
l
o
f
r
o
m
t
h
e
[[None, None, None, None, None], [None, None, None, None], [None, None, None]]
>>> map(print,map(lambda x: range(x,10)),range(1,11))
Traceback (most recent call last):
  File "<pyshell#605>", line 1, in <module>
    map(print,map(lambda x: range(x,10)),range(1,11))
TypeError: map() must have at least two arguments.
>>> map(print,map((lambda x: range(x,10)),range(1,11)))
<map object at 0x00000215643AD550>
>>> set(map(print,map((lambda x: range(x,10)),range(1,11))))
range(1, 10)
range(2, 10)
range(3, 10)
range(4, 10)
range(5, 10)
range(6, 10)
range(7, 10)
range(8, 10)
range(9, 10)
range(10, 10)
{None}
>>> set(map(print,map((lambda x: range(x,10)),range(1,11))))
range(1, 10)
range(2, 10)
range(3, 10)
range(4, 10)
range(5, 10)
range(6, 10)
range(7, 10)
range(8, 10)
range(9, 10)
range(10, 10)
{None}
>>> set(map((lambda x: map(print,x)),map((lambda x: range(x,10)),range(1,11))))
{<map object at 0x00000215643AD400>, <map object at 0x00000215643ADC18>, <map object at 0x00000215643AD470>, <map object at 0x00000215643ADC88>, <map object at 0x00000215643AD4A8>, <map object at 0x00000215643AD8D0>, <map object at 0x00000215643AD4E0>, <map object at 0x00000215643ADCF8>, <map object at 0x00000215643ADB38>, <map object at 0x00000215643AD3C8>}
>>> set(map((lambda x: set(map(print,x))),map((lambda x: range(x,10)),range(1,11))))
1
2
3
4
5
6
7
8
9
Traceback (most recent call last):
  File "<pyshell#610>", line 1, in <module>
    set(map((lambda x: set(map(print,x))),map((lambda x: range(x,10)),range(1,11))))
TypeError: unhashable type: 'set'
>>> list(map((lambda x: set(map(print,x))),map((lambda x: range(x,10)),range(1,11))))
1
2
3
4
5
6
7
8
9
2
3
4
5
6
7
8
9
3
4
5
6
7
8
9
4
5
6
7
8
9
5
6
7
8
9
6
7
8
9
7
8
9
8
9
9
[{None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}, {None}, set()]
>>> exec(map((lambda x: set(map(print,x))),map((lambda x: range(x,10)),range(1,11))))
Traceback (most recent call last):
  File "<pyshell#612>", line 1, in <module>
    exec(map((lambda x: set(map(print,x))),map((lambda x: range(x,10)),range(1,11))))
TypeError: exec() arg 1 must be a string, bytes or code object
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> set(map(print,map((lambda x: range(x,10)),range(1,11))))
range(1, 10)
range(2, 10)
range(3, 10)
range(4, 10)
range(5, 10)
range(6, 10)
range(7, 10)
range(8, 10)
range(9, 10)
range(10, 10)
{None}
>>> print(range(10))
range(0, 10)
>>> print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> set(map(print,map((lambda x: list(range(x,10))),range(1,11))))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9]
[4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[6, 7, 8, 9]
[7, 8, 9]
[8, 9]
[9]
[]
{None}
>>> set(map((lambda x: map(print,range(x,10))),range(1,11)))
{<map object at 0x00000215643AD400>, <map object at 0x00000215643ADE10>, <map object at 0x00000215643ADE48>, <map object at 0x00000215643AD470>, <map object at 0x00000215643ADEB8>, <map object at 0x00000215643ADCC0>, <map object at 0x00000215643ADCF8>, <map object at 0x00000215643ADF28>, <map object at 0x00000215643ADB38>, <map object at 0x00000215643ADDD8>}
>>> set(map((lambda x: list(map(print,range(x,10)))),range(1,11)))
1
2
3
4
5
6
7
8
9
Traceback (most recent call last):
  File "<pyshell#620>", line 1, in <module>
    set(map((lambda x: list(map(print,range(x,10)))),range(1,11)))
TypeError: unhashable type: 'list'
>>> list(map((lambda x: list(map(print,range(x,10)))),range(1,11)))
1
2
3
4
5
6
7
8
9
2
3
4
5
6
7
8
9
3
4
5
6
7
8
9
4
5
6
7
8
9
5
6
7
8
9
6
7
8
9
7
8
9
8
9
9
[[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None], [None, None, None, None], [None, None, None], [None, None], [None], []]
>>> list(map((lambda x: list(map(print,filter(int(10).__gt__,range(1,10))))),range(1,11)))
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
[[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None]]
>>> list(map((lambda x: list(map(print,range(x,10)))),range(1,11)))
KeyboardInterrupt
>>> list(map((lambda x: list(map(print,filter(int(10).__gt__,range(x,11))))),range(1,11)))
1
2
3
4
5
6
7
8
9
2
3
4
5
6
7
8
9
3
4
5
6
7
8
9
4
5
6
7
8
9
5
6
7
8
9
6
7
8
9
7
8
9
8
9
9
[[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None], [None, None, None, None], [None, None, None], [None, None], [None], []]
>>> nums=sieve();(tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums)))
(23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397)
>>> tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums))
(23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397)
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums))
(23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397)
>>> tuple(filter((lambda n: n>10 and all(map((lambda x: all(map(nums.__contains__, divmod(n,x)))),tens[:int(log10(n))]))),nums))
(23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397)
>>> 10!
SyntaxError: invalid syntax
>>> nCr = lambda n,k: math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
>>> nCr(5,3)
10.0
>>> nCr = lambda n,k: math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
>>> nCr(5,3)
10
>>> nCr(500,3)
20708500
>>> nCr(500,5)
255244687600
>>> nCr(500000,5)
Traceback (most recent call last):
  File "<pyshell#642>", line 1, in <module>
    nCr(500000,5)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\idlelib\rpc.py", line 613, in displayhook
    sys.stdout.write(text)
  File "C:\Users\cilli\AppData\Local\Programs\Python\Python35\lib\idlelib\PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
filter(int(10000).__gt__,primes))
>>> def prod(n*):
	
SyntaxError: invalid syntax
>>> def prod(*n):
	p = 1
	for i in n:
		p *= i
	return p

>>> set(map(prod,range(2,10)))
{2, 3, 4, 5, 6, 7, 8, 9}
>>> prod(range(2,10))
Traceback (most recent call last):
  File "<pyshell#651>", line 1, in <module>
    prod(range(2,10))
  File "<pyshell#649>", line 4, in prod
    p *= i
TypeError: unsupported operand type(s) for *=: 'int' and 'range'
>>> def prod(*n):
	p = 1
	for k in n:
		for i in k:
			p *= i
	return p

>>> prod(1,2)
Traceback (most recent call last):
  File "<pyshell#654>", line 1, in <module>
    prod(1,2)
  File "<pyshell#653>", line 4, in prod
    for i in k:
TypeError: 'int' object is not iterable
>>> def prod(*n):
	p = 1
	for k in n:
		if 
		for i in k:
			p *= i
	return p
KeyboardInterrupt
>>> issubclass(range)
Traceback (most recent call last):
  File "<pyshell#655>", line 1, in <module>
    issubclass(range)
TypeError: issubclass expected 2 arguments, got 1
>>> issubclass(range,iter)
Traceback (most recent call last):
  File "<pyshell#656>", line 1, in <module>
    issubclass(range,iter)
TypeError: issubclass() arg 2 must be a class or tuple of classes
>>> issubclass(range,iter)
Traceback (most recent call last):
  File "<pyshell#657>", line 1, in <module>
    issubclass(range,iter)
TypeError: issubclass() arg 2 must be a class or tuple of classes
>>> isinstance(range,iterable)
Traceback (most recent call last):
  File "<pyshell#658>", line 1, in <module>
    isinstance(range,iterable)
NameError: name 'iterable' is not defined
>>> isinstance(range,iter)
Traceback (most recent call last):
  File "<pyshell#659>", line 1, in <module>
    isinstance(range,iter)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(range,type(iter))
False
>>> type(iter)
<class 'builtin_function_or_method'>
>>> type(iter())
Traceback (most recent call last):
  File "<pyshell#662>", line 1, in <module>
    type(iter())
TypeError: iter expected at least 1 arguments, got 0
>>> type(iter([]))
<class 'list_iterator'>
>>> type(iter(range))
Traceback (most recent call last):
  File "<pyshell#664>", line 1, in <module>
    type(iter(range))
TypeError: 'type' object is not iterable
>>> type(range)
<class 'type'>
>>> type(range())
Traceback (most recent call last):
  File "<pyshell#666>", line 1, in <module>
    type(range())
TypeError: range expected 1 arguments, got 0
>>> type(range(5))
<class 'range'>
>>> help(reduce)
Traceback (most recent call last):
  File "<pyshell#668>", line 1, in <module>
    help(reduce)
NameError: name 'reduce' is not defined
>>> help('reduce')
No Python documentation found for 'reduce'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('functools')
Help on module functools:

NAME
    functools - functools.py - Tools for working with functions and callable objects

CLASSES
    builtins.object
        partial
        partialmethod
    
    class partial(builtins.object)
     |  partial(func, *args, **keywords) - new function with partial application
     |  of the given arguments and keywords.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |  
     |  args
     |      tuple of arguments to future partial calls
     |  
     |  func
     |      function object to use in future partial calls
     |  
     |  keywords
     |      dictionary of keyword arguments to future partial calls
    
    class partialmethod(builtins.object)
     |  Method descriptor with partial application of the given arguments
     |  and keywords.
     |  
     |  Supports wrapping existing descriptors and handles non-descriptor
     |  callables as instance methods.
     |  
     |  Methods defined here:
     |  
     |  __get__(self, obj, cls)
     |  
     |  __init__(self, func, *args, **keywords)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __isabstractmethod__
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    cmp_to_key(...)
        Convert a cmp= function into a key= function.
    
    lru_cache(maxsize=128, typed=False)
        Least-recently-used cache decorator.
        
        If *maxsize* is set to None, the LRU features are disabled and the cache
        can grow without bound.
        
        If *typed* is True, arguments of different types will be cached separately.
        For example, f(3.0) and f(3) will be treated as distinct calls with
        distinct results.
        
        Arguments to the cached function must be hashable.
        
        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.
        
        See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    
    singledispatch(func)
        Single-dispatch generic function decorator.
        
        Transforms a function into a generic function, which can have different
        behaviours depending upon the type of its first argument. The decorated
        function acts as the default implementation, and additional
        implementations can be registered using the register() attribute of the
        generic function.
    
    total_ordering(cls)
        Class decorator that fills in missing ordering methods
    
    update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
        Update a wrapper function to look like the wrapped function
        
        wrapper is the function to be updated
        wrapped is the original function
        assigned is a tuple naming the attributes assigned directly
        from the wrapped function to the wrapper function (defaults to
        functools.WRAPPER_ASSIGNMENTS)
        updated is a tuple naming the attributes of the wrapper that
        are updated with the corresponding attribute from the wrapped
        function (defaults to functools.WRAPPER_UPDATES)
    
    wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
        Decorator factory to apply update_wrapper() to a wrapper function
        
        Returns a decorator that invokes update_wrapper() with the decorated
        function as the wrapper argument and the arguments to wraps() as the
        remaining arguments. Default arguments are as for update_wrapper().
        This is a convenience function to simplify applying partial() to
        update_wrapper().

DATA
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__do...
    WRAPPER_UPDATES = ('__dict__',)
    __all__ = ['update_wrapper', 'wraps', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_...

FILE
    c:\users\cilli\appdata\local\programs\python\python35\lib\functools.py


>>> from functools import reduce
>>> from operator import mul
>>> def prod(l):
	return reduce(mul,l)

>>> prod(range(5))
0
>>> def prod(l):
	return reduce(mul,list(l))

>>> prod(range(5))
0
>>> prod(range(2,5))
24
>>> def prod(l):
	return reduce(mul,l)
prod(range(2,5))
SyntaxError: invalid syntax
>>> def prod(l):
	return reduce(mul,l)

>>> def prod(l):
	return reduce(mul,l)
prod(range(2,5))
KeyboardInterrupt
>>> prod(range(2,5))
24
>>> nCr = lambda n,k: prod(range(n,k,-1))//(math.factorial(n-k))
>>> 20708500
20708500
>>> nCr(500,3)
20708500
>>> nCr(500,3)
20708500
>>> nCr(500,5)
255244687600
>>> nCr(10000,5)
832500291625002000
>>> nCr(1000000,5)

=============================== RESTART: Shell ===============================
>>> 
