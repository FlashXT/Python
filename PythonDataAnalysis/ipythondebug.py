run ipythonad.py
%debug
run -d  ipythonad.py
run -d  ipythonad.py
run -d  ipythonad.py
run -d  ipythonad.py
run ipython_bug.py
%debug
run -d ipython_bug.py
run -d ipython_bug.py
run -d ipython_bug.py
c
run -d ipython_bug.py
run -d ipython_bug.py
run -d ipython_bug.py
run -d ipython_bug.py
run -d ipython_bug.py
!a
run -d ipython_bug.py
!a
run -d ipython_bug.py
run -d ipython_bug.py
strings = ['foo','foobar','baz','qux','python','Guido Van Rossum']*100000
method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']
%time method1 = [x for x in strings if x.startswith('foo')]
%time method2 = [x for x in strings if x[:3]=='foo']
%timeit [x for x in strings if x.startswith('foo')]
%timeit [x for x in strings if x[:3]=='foo']
x = 'foobar'
y = 'foo'
%timeit x.startswith(y)
%timeit x[:3]== y
%hist -f ipythondebug.py
