# coding:utf-8
# 模块 -- 调用方法一 import 
import my_module

celsius = float(raw_input ("Enter a temperature in Celsius:"))
#fahrenheit = c_to f(celsius)
fahrenheit = my_module.c_to_f(celsius)
print "That's ",fahrenheit," degree Fahrenheit"