#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class bike():#类的名字写的不好，应该写ride比较好么？
  def __init__ (self,kind):
    self.kind = kind
    
  def ride(self,day,distance,hour):#这里居然也要声明distance
    speed = float(distance)/hour
    print '%s骑%s平均时速 %0.2fkm/h' %(day,self.kind,speed)






def main():

  distance = 20

  bike1 =bike("电动车")
  bike1.ride ("周一",20,0.5)
  bike2 = bike("自行车")
  bike2.ride("周二",20,2)
  bike2 = bike("电动车")
  bike2.ride("周三",20,0.6)

  """e_bicycle = '电动车'
        bicycle = '自行车'
      
        day1 = '周一'
        hour1 = 0.5
        speed1 = 20/hour1
        print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)
      
        day2 = '周二'
        hour2 = 2
        speed2 = 20/hour2
        print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)
      
        day3 = '周三'
        hour3 = 0.6
        speed3 = 20/hour3
        print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)"""



if __name__ == '__main__':
  main()
