#coding=utf-8
#############################################################
#list做函数参数
#Author:FlashXT;Date:2018.5.19,Saturday;
#CopyRight © 2018-2020,FlashXT & turboMan,All right reserved.
#############################################################

################################################################
#                  list做函数参数
#     将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做
# 的任何修改都是永久性的，相当于传地址，这让你能够高效地处理大量的数据。
#     有时候列表传递给函数后，不希望函数对其进行修改。这时需要给函数传
# 递列表的副本。
################################################################

list=[i for i in range(1,20)]
print(list)

def ProceList(list):
    for i in range(len(list)):
        list[i]=list[i]+1

list2=list[:]
ProceList(list2)
print(list)
print(list2)


#print_model函数
def print_model(unprinted_degisns,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止；
    打印每个设计之后，都将其移动到列表completed_models中
    :param unprinted_degisns:
    :param cmpleted_models:
    :return:
    """
    while unprinted_degisns:
        current_design = unprinted_degisns.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Print model:"+current_design)
        completed_models.append(current_design)
#show_models函数
def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    :param completed_models:
    :return:
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t"+completed_model)



#函数调用
unprinted_designs = ["iPhone case","Rboot pendant","XiaoMi6"]
completed_models = []

# 检测列表是否变化
print("unprinted_designs = " + str(unprinted_designs))
print("completed_models = " + str(completed_models))

print_model(unprinted_designs,completed_models)
show_completed_models(completed_models)

# 检测列表是否变化
print("unprinted_designs = " + str(unprinted_designs))
print("completed_models = " + str(completed_models))