%run prof_mod
x = randn(3000,3000)
y = randn(3000,3000)
%prun add_and_sum(x,y)
%lprun -f add_and_sum add_and_sum(x,y)

