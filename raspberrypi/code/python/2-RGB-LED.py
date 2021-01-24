#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# －－－－湖南创乐博智能科技有限公司－－－－

#  文件名：02_rgb_led.py

#  版本：V2.0

#  author: zhulin

# 说明：RGB-LED传感器实验

#---------------------------------------

import RPi.GPIO as GPIO

import time



colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]

makerobo_R = 11

makerobo_G = 12

makerobo_B = 13



# 初始化程序

def makerobo_setup(Rpin, Gpin, Bpin):

    global pins

    global p_R, p_G, p_B

    pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}

    GPIO.setmode(GPIO.BOARD)        # 采用实际的物理管脚给GPIO口

    GPIO.setwarnings(False)         # 去除GPIO口警告

    for i in pins:

        GPIO.setup(pins[i], GPIO.OUT)   # 设置Pin模式为输出模式

        GPIO.output(pins[i], GPIO.LOW)  # 设置Pin管脚为低电平(0V)关闭LED



    # 由于RGB三色模块每一个LED达到一定的亮度，需要的电流值是不一样，所以设置的频率有区别

    p_R = GPIO.PWM(pins['pin_R'], 2000)  # 设置频率为2KHz

    p_G = GPIO.PWM(pins['pin_G'], 1999)

    p_B = GPIO.PWM(pins['pin_B'], 5000)

    

    # 初始化占空比为0(led关闭)

    p_R.start(0)

    p_G.start(0)

    p_B.start(0)



# 按比例缩放函数

def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):

    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



# 关闭RGB-LED灯

def makerobo_off():

    GPIO.setmode(GPIO.BOARD)   # 采用实际的物理管脚给GPIO口

    for i in pins:

        GPIO.setup(pins[i], GPIO.OUT)     # 设置Pin模式为输出模式

        GPIO.output(pins[i], GPIO.LOW)    #  设置Pin管脚为低电平(0V)关闭LED



# 设置颜色

def makerobo_set_Color(col):   #  例如:col  = 0x112233

    R_val = (col & 0xff0000) >> 16

    G_val = (col & 0x00ff00) >> 8

    B_val = (col & 0x0000ff) >> 0



    # 把0-255的范围同比例缩小到0-100之间

    R_val = makerobo_pwm_map(R_val, 0, 255, 0, 100)

    G_val = makerobo_pwm_map(G_val, 0, 255, 0, 100)

    B_val = makerobo_pwm_map(B_val, 0, 255, 0, 100)

    

    p_R.ChangeDutyCycle(100-R_val)     # 改变占空比

    p_G.ChangeDutyCycle(100-G_val)     # 改变占空比

    p_B.ChangeDutyCycle(100-B_val)     # 改变占空比



# 循环函数

def makerobo_loop():

    while True:

        for col in colors:

            makerobo_set_Color(col)  # 设置颜色

            time.sleep(1)            # 延时1s

# 资源释放

def makerobo_destroy():

    p_R.stop()      # 关闭红色PWM

    p_G.stop()      # 关闭绿色PWM

    p_B.stop()      # 关闭蓝色PWM

    makerobo_off()  # 关闭RGB-LED灯

    GPIO.cleanup()  # 释放资源



# 程序入口

if __name__ == "__main__":

    try:

        makerobo_setup(makerobo_R, makerobo_G, makerobo_B) # 初始化设置函数

        makerobo_loop()                                    # 循环函数

    except KeyboardInterrupt:                              # 当按下Ctrl+C时，将执行destroy()子程序。

        makerobo_destroy()                                 # 资源释放
