#coding=utf-8
###################################################################
#Topic：利用Numpy进行历史股价分析
#Author：FlashXT;
#Date :2018.6.4,Monday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
###################################################################
import sys
import numpy as np
#读入文件
c,v=np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
#计算成交量加权平均价格
vwap=np.average(c,weights=v)
print("计算成交量加权平均价格:"+str(vwap))

#算术平均值函数
print("平均价格："+str(np.mean(c)))
#时间加权平均价格，按时间离当前日期的远近加权
t=np.arange(len(c))
print("twap ="+str(np.average(c,weights=t)))
#寻找最大值和最小值
high,low =np.loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True)
print("highest = "+str(np.max(high)))
print("lowest = "+str(np.min(low)))
print("The Mean of highest&lowest = "+str((np.max(high)+np.min(low))/2))
#numpy.ptp()求极值
print("Spread high price:"+str(np.ptp(high)))
print("Spread low price:"+str(np.ptp(low)))

#统计分析
middle = np.loadtxt('data.csv',delimiter=',',usecols=(6),unpack=True)
#利用median()函数计算中位数
print("middle = "+str(np.median(middle)))
sorted = np.msort(c)
print("sorted = ",sorted)
#手动计算中位数
if(len(c/2) ==0):
	print(sorted[len(c)/2])
else:
	print((sorted[len(c)/2]+sorted[len(c)/2-1])/2)
#计算方差var函数
print("variance = %6.3f"%np.var(c))
#利用定义计算方差
var=np.mean((c-c.mean())**2)
print("var = %6.3f"%var)

#股票收益率(普通收益率，对数收益率)
value = np.loadtxt('data.csv',delimiter=',',usecols=(6),unpack=True)
returns = np.diff(value)#/value[:-1]
print(returns)
print("标准差 = "+str(np.std(returns)))
logreturns = np.diff(np.log(value))
posretindices = np.where(returns > 0)
print("Indices with positive returns = "+str(posretindices))
annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1./252.)
print("Annual volatility = "+ str(annual_volatility))
print("Monthly volatility = "+str(annual_volatility * np.sqrt(1./12.)))

#日期分析
from datetime import datetime
#Monday 0
#Tuesday 1
#Wednesday 2
#Thursday 3
#Friday 4
#Saturday 5
#Sunday 6
def datestr2num(s):
	return datetime.strptime(s,"%d-%m-%Y").date().weekday()
dates,close = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),
                         converters={1:datestr2num},unpack=True)
print("Dates = "+str(dates))
averages = np.zeros(5)

for i in range(5):
	indices = np.where(dates == i)
	prices = np.take(close,indices)
	avg = np.mean(prices)
	print("Day "+str(i)+" prices",prices,"Average",avg)
	averages[i] = avg
top =np.max(averages)
print("highest average = "+str(top))
print("Top day of the week = "+str(np.argmax(averages)))

bottom = np.min(averages)
print("Lowest average = "+ str(bottom))
print("Bottom day of the week = "+ str(np.argmin(averages)))

#周汇总

def datestr2num(s):
   return datetime.strptime(s, "%d-%m-%Y").date().weekday()

dates, open, high, low, close=np.loadtxt('data.csv', delimiter=',',
         usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]

#get first Monday
first_Monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is "+str(first_Monday))

#get last Monday
last_Friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is "+str(last_Friday))

weeks_indices = np.arange(first_Monday, last_Friday + 1)
print("Weeks indices initial"+str(weeks_indices))

weeks_indices = np.split(weeks_indices, 3)
print("Weeks indices after split"+str(weeks_indices))
def summarize(arr,open,high,low,closed):
	monday_open =open[arr[0]]
	week_high = np.max(np.take(high,arr))
	week_low = np.min(np.take(low,arr))
	friday_close = closed[arr[-1]]
	return ("APPL",monday_open,week_high,week_low,friday_close)
weeksummary = np.apply_along_axis(summarize,1,weeks_indices,open,high,low,close)
print("Week summary :"+str(weeksummary))
#保存为文件
np.savetxt('WeekSummary.csv',weeksummary,delimiter=",",fmt="%s")
np.savetxt('WeekSummary.txt',weeksummary,delimiter=",",fmt="%s")

#真实波动幅度均值
high,low,close = np.loadtxt('data.csv',delimiter=',',usecols=(4,5,6),unpack=True)
N=5
print("high = "+str(high))
print("low = "+str(low))
high = high[-N:]
low = low[-N:]
print("High = "+str(high))
print("low = "+str(low))
print("len(high)= " +str(len(high))+",len(low) = "+str(len(low)))
print("close = " +str(close))
print("len(close)="+str(len(close)))
previousclose = close[-N-1:-1]
print("previousclose = "+str(previousclose))
print("len(previousclose) =  "+str(len(previousclose)))
truerange = np.maximum(high - low,high-previousclose,previousclose-low)
print("TrueRange :"+str(truerange))
atr = np.zeros(N)
atr[0]=np.mean(truerange)
for i in range(1,N):
	atr[i]=(N-1)*atr[i-1]+ truerange[i]
	atr[i]/=N
print("ATR = "+str(atr))

#简单移动平均线
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = 5

weights = np.ones(N) / N
print("Weights = "+str(weights))

close = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, close)[N-1:-N+1]
t = np.arange(N - 1, len(close))
# plot(t, close[N-1:], lw=1.0)
# plot(t, sma, lw=2.0)
show()

#指数移动平均线
x = np.arange(5)
print("Exp", np.exp(x))
print("Linspace", np.linspace(-1, 0, 5))

N = 5
weights = np.exp(np.linspace(-1., 0., N))
weights /= weights.sum()
print("Weights = ", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, ema, lw=2.0)
show()

# 布林带
N = 5

weights = np.ones(N) / N
print("Weights = "+str(weights))

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N - 1:-N + 1]
deviation = []
C = len(c)

for i in range(N - 1, C):
	if i + N < C:
		dev = c[i: i + N]
	else:
		dev = c[-N:]

	averages = np.zeros(N)
	averages.fill(sma[i - N - 1])
	dev = dev - averages
	dev = dev ** 2
	dev = np.sqrt(np.mean(dev))
	deviation.append(dev)

deviation = 2 * np.array(deviation)
print len(deviation), len(sma)
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N - 1:]
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

print lowerBB[between_bands]
print c[between_bands]
print upperBB[between_bands]
between_bands = len(np.ravel(between_bands))
print "Ratio between bands", float(between_bands) / len(c_slice)

t = np.arange(N - 1, C)
plot(t, c_slice, lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()
