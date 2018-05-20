#接收任意参数
def make_sandwich(*inners):
    for inner in inners:
        print("Adding "+ str(inner) +"!")
    return inners
make_sandwich("AAA","BBB","CCC","DDD")
print("\n")
make_sandwich("EEE","FFF","GGG")
print("\n")
make_sandwich("HHH")

print("====================================")
#接收任意键值对
def cars(maker,model,**infos):
    carinfo={}
    carinfo["maker"]=maker
    carinfo["model"]=model
    for k,v in infos.items():
        carinfo[k]=v
    return carinfo

info=cars("Tesla","model 3",color="silver",Power="500kw")
for k,v in info.items():
    print(k+" : "+v+ ";")