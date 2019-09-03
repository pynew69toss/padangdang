# -*- coding: utf-8 -*-

#插件1
from PluginManager import Model_MenuObj

class Plugin1(Model_MenuObj):
    def __init__(self):
        pass

    #实现接入点的接口
    def Start(self):
        print( "I am plugin1 , I am a menu!")
