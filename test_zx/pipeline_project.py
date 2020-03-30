#!/usr/env/bin python
# -*- coding: utf-8 -*-
#__author:zhangxiao
#date: 2020-03-26


def SSS = ''   定义变量
pipeline {
    agent all
    parameers{  与input不同，parameters时执行pipeline前输入一些参数

}
    environment{   只能定义在stage或pipeline部分，用于设置环境变量  对全局生效，也可对单个stages做设置
     git_url = 'ddd'
}
    options{   配置Jenkins本身的设置
    XXX {AA:11}
}
    triggers{    定义执行pipeline的触发器

}
    stages{
        when   条件满足的时候，阶段才会执行
        parallel  并行执行多个step
        input  定义在stage部分，会暂停pipeline 提示你输入内容

}


    post{

}
url = https://blog.csdn.net/qq_30758629/article/details/93353437

}

引入变量   ${environment}