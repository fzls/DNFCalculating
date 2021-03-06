from PublicReference.base import *

class 极诣剑魂主动技能(主动技能):
    hit数 = 0
    def 等效CD(self, 武器类型):
        if 武器类型 == '巨剑':
            return round(self.CD / self.恢复 * self.CD倍率 * 1.1, 1)
        if 武器类型 == '太刀':
            return round(self.CD / self.恢复 * self.CD倍率 * 0.95, 1)
        if 武器类型 == '钝器':
            return round(self.CD / self.恢复 * self.CD倍率 * 1.05, 1)
        if 武器类型 == '短剑':
            return round(self.CD / self.恢复 * self.CD倍率 * 1.0, 1)
        if 武器类型 == '光剑':
            return round(self.CD / self.恢复 * self.CD倍率 * 0.90, 1)
    def 额外刺伤层数(self, 武器类型):
        return 0
    def 穿云刺数量(self, 武器类型):
        return 0

class 极诣剑魂流系技能(主动技能):
    hit数 = 0
    def 额外刺伤层数(self, 武器类型):
        return 0
    def 穿云刺数量(self, 武器类型):
        return 0

class 极诣剑魂技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['里鬼剑术','空中连斩']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.472 + 0.0889 * self.等级, 5)

class 极诣剑魂技能1(极诣剑魂主动技能):
    hit数 = 8
    名称 = '里鬼剑术'
    备注 = '(一轮，TP为基础精通)'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    基础 = 0.97
    成长 = 0.03
    CD = 1.0
    TP成长 = 0.1
    TP上限 = 5
    基础百分比 = {'短剑':1004.68, '光剑':890.19, '巨剑':1241.95, '钝器':1225.24, '太刀':1197.49}
    #巨剑不蓄力441.19
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.基础百分比[武器类型] * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
    def 穿云刺数量(self, 武器类型):
        if 武器类型 == '巨剑':
            return 2
        if 武器类型 == '太刀':
            return 4
        if 武器类型 == '钝器':
            return 4
        if 武器类型 == '短剑':
            return 3
        if 武器类型 == '光剑':
            return 3

class 极诣剑魂技能2(被动技能):
    名称 = '武器奥义'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    关联技能 = ['无']

class 极诣剑魂技能3(被动技能):
    名称 = '光剑掌握'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['无']
    冷却关联技能 = ['所有']
    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.0 - 0.01 * self.等级, 5)

class 极诣剑魂技能4(极诣剑魂主动技能):
    名称 = '流心狂'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['流心刺','流心跃','流心升']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20 + 0.02 * self.等级, 5)


class 极诣剑魂技能5(被动技能):
    名称 = '无我剑气'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 极诣剑魂技能6(极诣剑魂流系技能):
    名称 = '流心刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 998.2619048
    成长 = 112.7380952
    TP成长 = 0.10
    TP上限 = 7
    CD = 5.0

    武器倍率 = {'短剑':2 + 1, '光剑':4 * 0.63, '巨剑':2 + 1, '钝器':2 * 1.25, '太刀':4 * 0.63}

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.武器倍率[武器类型] * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    hit数 = 4
    def 额外刺伤层数(self, 武器类型):
        return min((0.01 * self.等级 + 0.17),1) * int(self.等级 / 20)

    def 穿云刺数量(self, 武器类型):
        return 2


class 极诣剑魂技能7(极诣剑魂流系技能):
    名称 = '流心跃'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3665.05
    成长 = 413.95
    TP成长 = 0.10
    TP上限 = 7
    CD = 7.0

    武器倍率 = {'短剑':2 * 0.5, '光剑': 1, '巨剑': 1, '钝器': 1, '太刀':2 * 0.5}

    #钝器冲击波占比 0.271783561  钝器空中释放20%加成

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.武器倍率[武器类型] * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率

    hit数 = 2
    def 额外刺伤层数(self, 武器类型):
        return min((0.01 * self.等级 + 0.34),1) * int(self.等级 / 15)

    def 穿云刺数量(self, 武器类型):
        return 2

class 极诣剑魂技能8(极诣剑魂流系技能):
    名称 = '流心升'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2505.891892
    成长 = 283.1081081
    TP成长 = 0.10
    TP上限 = 7
    CD = 9.0

    武器倍率 = {'短剑':1 + 1.1, '光剑':3 * 0.8, '巨剑':1 + 1.1, '钝器':1 + 1.1, '太刀':3 * 0.8}

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.武器倍率[武器类型] * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率

    hit数 = 3
    def 额外刺伤层数(self, 武器类型):
        if self.等级 >= 15:
            return min((0.05 * self.等级 - 0.25), 1) * int(self.等级 / 15 + 1)
        else:
            return 0

    def 穿云刺数量(self, 武器类型):
        return 2

class 极诣剑魂技能9(极诣剑魂主动技能):
    名称 = '破军升龙击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38

    冲撞基础 = 1125.810811
    冲撞成长 = 127.1891892
    上斩基础 = 1738.783784
    上斩成长 = 196.2162162
  
    TP成长 = 0.10
    TP上限 = 7
    CD = 10.0

    冲撞倍率 = {'短剑':2 * 1.45, '光剑':4 * 0.89, '巨剑':2, '钝器':2, '太刀':2}
    上斩倍率 = {'短剑':1 * 1.45, '光剑':1, '巨剑':2, '钝器':2, '太刀':2}

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (self.冲撞倍率[武器类型] * (self.冲撞基础 + self.冲撞成长 * self.等级) + self.上斩倍率[武器类型] * (self.上斩基础 + self.上斩成长 * self.等级))* (1 + self.TP成长 * self.TP等级) * self.倍率
    
    #极神剑术被动相关
    def 上斩百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (self.上斩基础 + self.上斩成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率

    hit数 = 3
    def 额外刺伤层数(self, 武器类型):
        if self.等级 >= 4:
            return min((0.01 * self.等级 + 0.27), 1) * 2
        else:
            return 0


class 极诣剑魂技能10(极诣剑魂主动技能):
    名称 = '拔刀斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5560.914286
    成长 = 628.0857143
    TP成长 = 0.10
    TP上限 = 7
    CD = 15.0
    是否有护石 = 1
    触发神影手 = 0

    武器倍率 = {'短剑':1.4, '光剑':1.3, '巨剑':1.3, '钝器':1.3, '太刀':1.25}

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return self.武器倍率[武器类型] * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.武器倍率 = {'短剑':1.4 + 0.28, '光剑':1.3 + 0.26, '巨剑':1.3 + 0.26, '钝器':1.3 + 0.26, '太刀':1.25 + 0.25}
        #不确定，待核对
        self.倍率 *= 1.05
        self.触发神影手 = 1


    hit数 = 2
    def 额外刺伤层数(self, 武器类型):
        if self.等级 >= 5:
            x1 = min((0.02 * self.等级 + 0.31), 1) * int(self.等级 / 5)
        else:
            x1 = 0
        if self.等级 >= 10:
            x2 = min((0.02 * self.等级 + 0.22), 1) * int(self.等级 / 10)
        else:
            x2 = 0
        return x1 + x2


class 极诣剑魂技能11(极诣剑魂主动技能):
    名称 = '破军斩龙击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 11354.8125
    成长 = 1282.1875
    TP成长 = 0.10
    TP上限 = 7
    CD = 25.0
    hit数 = 4
    def 额外刺伤层数(self, 武器类型):
        return min((0.03 * self.等级 + 0.33), 1) * int(self.等级 / 10 + 1)
    def 穿云刺数量(self, 武器类型):
        return 5

class 极诣剑魂技能12(极诣剑魂主动技能):
    名称 = '猛龙断空斩'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8226.5
    成长 = 929.5
    TP成长 = 0.10
    TP上限 = 7
    CD = 20.0
    hit数 = 4 + 8
    旋风倍率 = 4 * 2
    是否有护石 = 1

    #极神剑术被动相关
    def 突进百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if 武器类型 != '短剑':
                return (1665.78125 + 188.21875 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
            else:
                return 1.25 * (1665.78125 + 188.21875 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    def 装备护石(self):
        self.hit数 = 4 + 11 * 3
        self.旋风倍率 = 11 * 3 * 0.43

class 极诣剑魂技能13(极诣剑魂主动技能):
    名称 = '幻影剑舞'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    斩击基础 = 618.9333333
    斩击成长 = 70.06666667
    斩击倍率 = {'短剑':12*0.9, '光剑':24*0.75, '巨剑':12*1.5, '钝器':12, '太刀':24*0.75}

    剑气基础 = 2481.833333
    剑气成长 = 280.1666667
    剑气倍率 = {'短剑':4*1.2, '光剑':3, '巨剑':3, '钝器':4.2, '太刀':3}

    TP成长 = 0.10
    TP上限 = 7
    CD = 45.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (self.斩击倍率[武器类型] * (self.斩击基础 + self.斩击成长 * self.等级) + self.剑气倍率[武器类型] * (self.剑气基础 + self.剑气成长 * self.等级))* (1 + self.TP成长 * self.TP等级) * self.倍率
    
    #极神剑术被动相关
    def 斩击百分比(self, 武器类型):
        return (self.斩击基础 + self.斩击成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
    #极神剑术被动相关
    def 剑气百分比(self, 武器类型):
        return (self.剑气基础 + self.剑气成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率

    hit数 = 24 + 3 + 4 + 3
    def 额外刺伤层数(self, 武器类型):
        return min((0.005 * self.等级 + 0.005), 1) * 2 * (24 + 3)

    def 穿云刺数量(self, 武器类型):
        return 4

    是否有护石 = 1
    影子多段攻击次数 = 4

    def 装备护石(self):
        self.影子多段攻击次数 = 4 + 13
        self.hit数 = 24 + 3 + 17 + 3


class 极诣剑魂技能14(极诣剑魂主动技能):
    名称 = '极鬼剑术暴风式'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 42467 * 1.1
    成长 = 12666 * 1.1
    CD = 145.0
    hit数 = 26

class 极诣剑魂技能15(被动技能):
    名称 = '极鬼剑术斩铁式'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.995 + 0.02 * self.等级, 5)

class 极诣剑魂技能16(被动技能):
    名称 = '极鬼剑术斩钢式'
    所在等级 = 48
    等级上限 = 1
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.083

class 极诣剑魂技能17(极诣剑魂主动技能):
    名称 = '极神剑术流星落'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 7821.5
    成长 = 883.5
    攻击次数 = 1
    基础2 = 478.6363636
    成长2 = 54.36363636
    攻击次数2 = 38
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 7
    hit数 = 40
    天剑刺伤层数 = 0
    def 额外刺伤层数(self, 武器类型):
        return min((0.03 * self.等级 + 0.26), 1) * 1 + self.天剑刺伤层数

    是否有护石 = 1
    天剑倍率 = 1.0
    def 装备护石(self):
        self.hit数 += 9
        self.攻击次数2 += 9
        self.天剑倍率 = 1.35


class 极诣剑魂技能18(极诣剑魂主动技能):
    名称 = '破空拔刀斩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 28828.23529
    成长 = 3254.764706
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    hit数 = 1
    def 额外刺伤层数(self, 武器类型):
        return min((0.04 * self.等级 + 0.27), 1) * (int((self.等级 - 1) / 3) * 2 + 3)

    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.11
        self.CD *= 0.9


class 极诣剑魂技能19(极诣剑魂主动技能):
    名称 = '极神剑术破空斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    多段基础 = 4431.533333
    多段成长 = 500.4666667
    多段倍率 = {'短剑':5, '光剑':6, '巨剑':5*1.08, '钝器':5, '太刀':6}

    爆炸基础 = 14772.86667
    爆炸成长 = 1668.133333
    爆炸倍率 = {'短剑':1, '光剑':1, '巨剑':1.08, '钝器':1, '太刀':1}

    CD = 35.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (self.多段倍率[武器类型] * (self.多段基础 + self.多段成长 * self.等级) + self.爆炸倍率[武器类型] * (self.爆炸基础 + self.爆炸成长 * self.等级)) * self.倍率
    
    #极神剑术被动相关
    def 爆炸百分比(self, 武器类型):
        return self.爆炸倍率[武器类型] * (self.爆炸基础 + self.爆炸成长 * self.等级) * self.倍率

    hit数 = 7
    def 额外刺伤层数(self, 武器类型):
        return min((0.02 * self.等级 + 0.51), 1) * 3

    def 穿云刺数量(self, 武器类型):
        return 4


class 极诣剑魂技能20(极诣剑魂主动技能):
    名称 = '极神剑术瞬斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 55483.75
    成长 = 6264.25
    CD = 50.0

    hit数 = 7

class 极诣剑魂技能21(极诣剑魂主动技能):
    名称 = '万剑归宗(终结)'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 76652.24096
    成长 = 23227.95181
    CD = 180.0

    hit数 = 16

class 极诣剑魂技能22(极诣剑魂主动技能):
    名称 = '万剑归宗(穿云刺)'
    所在等级 = 85
    等级上限 = 1
    基础等级 = 1
    基础 = 751.4457831
    成长 = 227.7108434
    CD = 0.5

    hit数 = 1

class 极诣剑魂技能23(极诣剑魂主动技能):
    名称 = '极神剑术无形斩'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 86480.2
    成长 = 9765.8
    CD = 60.0
    hit数 = 15

class 极诣剑魂技能24(极诣剑魂主动技能):
    名称 = '万剑极诣开天斩'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 257764
    成长 = 77814
    CD = 290
    hit数 = 14

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

class 极诣剑魂技能25(被动技能):
    名称 = '极神剑术'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['拔刀斩','破军斩龙击','极鬼剑术暴风式','破空拔刀斩','极神剑术瞬斩','万剑归宗(终结)','万剑归宗(穿云刺)','极神剑术无形斩','万剑极诣开天斩']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 极诣剑魂技能26(被动技能):
    名称 = '无形剑意'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣剑魂技能27(被动技能):
    名称 = '短剑精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 1.0
        else:
            if self.等级 <= 22:
                return 1 + round(11.3 + 1.5 * self.等级, 1) / 100
            else:
                return 1 + round(44.3 + 2 * (self.等级 - 22), 1) / 100

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 里鬼附加百分比(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '短剑':
            return 0
        else:
            return (376.0526316 + 11.31578947 * self.等级) * 3
    #里鬼额外百分比 376.0526316 + 11.31578947 * self.等级  3段

class 极诣剑魂技能28(被动技能):
    名称 = '太刀精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['所有']
    刺伤层数 = 0

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 1.0
        else:
            if self.等级 <= 22:
                return 1 + round(3.7 + 1.5 * self.等级, 1) / 100
            else:
                return 1 + round(36.7 + 2 * (self.等级 - 22), 1) / 100

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 刺伤概率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 0
        else:
            return 0.325 + 0.005 * self.等级

    def 刺伤百分比(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 0
        else:
            return self.刺伤层数 / 20 * (-3075.666667 + 1050.666667 * self.等级)

    def 太刀附加(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '太刀':
            return 0
        else:
            return round(63.13833992 + 3.612648221 * self.等级, 0)

    #不了解刺伤百分比区间浮动算法  17层结算一次 但/20比较接近期望

class 极诣剑魂技能29(被动技能):
    名称 = '巨剑精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 1.0
        else:
            if self.等级 <= 22:
                return 1 + round(5.4 + 1.5 * self.等级, 1) / 100
            else:
                return 1 + round(38.4 + 2 * (self.等级 - 22), 1) / 100

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 里鬼附加百分比(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '巨剑':
            return 0
        else:
            return (376.0526316 + 11.31578947 * self.等级)*3

    #里鬼额外百分比 174.7442344 + 62.23625649 * self.等级 1段

class 极诣剑魂技能30(被动技能):
    名称 = '光剑精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            if self.等级 <= 22:
                return 1 + round(8.0 + 1.5 * self.等级, 1) / 100
            else:
                return 1 + round(41.0 + 2 * (self.等级 - 22), 1) / 100

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣剑魂技能31(被动技能):
    名称 = '钝器精通'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '钝器':
            return 1.0
        else:
            if self.等级 <= 22:
                return 1 + round(5.8 + 1.5 * self.等级, 1) / 100
            else:
                return 1 + round(38.8 + 2 * (self.等级 - 22), 1) / 100

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 极诣剑魂技能32(极诣剑魂主动技能):
    hit数 = 2
    名称 = '空中连斩'
    备注 = '(一刀，TP为基础精通)'
    所在等级 = 5
    等级上限 = 11
    基础等级 = 1
    基础 = 168
    成长 = 12
    CD = 1.0
    TP成长 = 0.1
    TP上限 = 5
    太刀附加 = 0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if 武器类型 != '太刀':
                return (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率
            else:
                return (self.基础 + self.成长 * self.等级 - 100 + self.太刀附加) * (1 + self.TP成长 * self.TP等级) * self.倍率 * 2 * 1.5

    def 穿云刺数量(self, 武器类型):
            return 1

class 极诣剑魂技能33(被动技能):
    名称 = '神影手'
    所在等级 = 70
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    百分比 = 3760


极诣剑魂技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣剑魂技能列表.append(极诣剑魂技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣剑魂技能序号 = dict()
for i in range(len(极诣剑魂技能列表)):
    极诣剑魂技能序号[极诣剑魂技能列表[i].名称] = i

极诣剑魂一觉序号 = 0
极诣剑魂二觉序号 = 21
极诣剑魂三觉序号 = 0
for i in 极诣剑魂技能列表:
    if i.所在等级 == 50:
        极诣剑魂一觉序号 = 极诣剑魂技能序号[i.名称]
    if i.所在等级 == 100:
        极诣剑魂三觉序号 = 极诣剑魂技能序号[i.名称]

极诣剑魂护石选项 = ['无']
for i in 极诣剑魂技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣剑魂护石选项.append(i.名称)

极诣剑魂符文选项 = ['无']
for i in 极诣剑魂技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣剑魂符文选项.append(i.名称)

class 极诣剑魂角色属性(角色属性):

    职业名称 = '极诣剑魂'

    武器选项 = ['光剑','巨剑','钝器','太刀','短剑']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']
    武器类型 = '光剑'

    主BUFF = 1.82
   
    #基础属性(含唤醒)
    基础力量 = 923.0
    基础智力 = 827.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    流心刺状态 = 0
    流心跃状态 = 0
  
    def __init__(self):
        self.技能栏= copy.deepcopy(极诣剑魂技能列表)
        self.技能序号= copy.deepcopy(极诣剑魂技能序号)

    def 被动倍率计算(self):

        if self.技能栏[self.技能序号['武器奥义']].等级 != 0:
            for i in ['太刀精通','短剑精通','巨剑精通','光剑精通','钝器精通']:
                if self.技能栏[self.技能序号[i]].等级 != 0:
                    self.技能栏[self.技能序号[i]].等级 += (self.技能栏[self.技能序号['武器奥义']].等级 + 1)
                if self.武器类型 not in i:
                    self.技能栏[self.技能序号[i]].关联技能 = ['无']

        super().被动倍率计算()

        self.技能栏[self.技能序号['万剑归宗(穿云刺)']].等级 = self.技能栏[self.技能序号['万剑归宗(终结)']].等级
        self.技能栏[self.技能序号['空中连斩']].太刀附加 = self.技能栏[self.技能序号['太刀精通']].太刀附加(self.武器类型)

        if self.流心跃状态 == 1:
            self.技能栏[self.技能序号['流心跃']].武器倍率['钝器'] = 1.2

        if self.流心刺状态 == 1:
            self.技能栏[self.技能序号['流心刺']].武器倍率['短剑'] = 2

            self.技能栏[self.技能序号['流心刺']].武器倍率['太刀'] = 2
            self.技能栏[self.技能序号['流心刺']].hit数 = 2
            
            self.技能栏[self.技能序号['流心刺']].武器倍率['巨剑'] = 2

            self.技能栏[self.技能序号['流心刺']].武器倍率['光剑'] = 2

        无形剑意等级 = self.技能栏[self.技能序号['无形剑意']].等级
        if 无形剑意等级 != 0:
            基础倍率 = 1.18 + 0.02 * 无形剑意等级
            if self.武器类型 == '短剑':
                self.技能栏[self.技能序号['流心刺']].被动倍率 /= 基础倍率
                if self.流心刺状态 == 1:
                    self.技能栏[self.技能序号['流心刺']].被动倍率 *= 1 + 3 * (round(0.120 + 0.013 * 无形剑意等级, 2)) / 2
                else:
                    self.技能栏[self.技能序号['流心刺']].被动倍率 *= 1 + 2 * (0.27 + 0.03 * 无形剑意等级) / 3
    
            if self.武器类型 == '太刀':
                self.技能栏[self.技能序号['流心跃']].被动倍率 /= 基础倍率
                self.技能栏[self.技能序号['流心升']].被动倍率 /= 基础倍率
    
                self.技能栏[self.技能序号['流心跃']].hit数 +=5
                self.技能栏[self.技能序号['流心跃']].被动倍率 *= 1 + int(3.5 + 0.5 * 无形剑意等级) / 100 * 5 
                
                self.技能栏[self.技能序号['流心升']].hit数 +=4
                self.技能栏[self.技能序号['流心升']].被动倍率 *= 1 + 4 * round(0.105 + 0.013 * 无形剑意等级, 2) / (3 * 0.8)
    
            if self.武器类型 == '钝器':
                self.技能栏[self.技能序号['流心刺']].被动倍率 /= 基础倍率
                self.技能栏[self.技能序号['流心刺']].被动倍率 *= 1 + (0.45 + 0.05 * 无形剑意等级) / (2 * 1.25)
    
            if self.武器类型 == '巨剑':
                self.技能栏[self.技能序号['流心刺']].被动倍率 /= 基础倍率

                if self.流心刺状态 == 1:
                    self.技能栏[self.技能序号['流心刺']].被动倍率 *= (2.36 + 0.04 * 无形剑意等级) / 2
                else:
                    self.技能栏[self.技能序号['流心刺']].被动倍率 *= ((2 + 1) * (1.09 + 0.01 * 无形剑意等级)  + (0.07 + 0.02 * 无形剑意等级) * 3) / (2 + 1)
    
            if self.武器类型 == '光剑':
                self.技能栏[self.技能序号['流心升']].被动倍率 /= 基础倍率
                self.技能栏[self.技能序号['流心升']].被动倍率 *= 1 + round(0.435 + 0.047 * 无形剑意等级, 2) / (3 * 0.8)

    def 伤害计算(self, x = 0):
        
        self.所有属性强化(self.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)

        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int(self.时间输入/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
            else:
                技能释放次数.append(0)

        #剑魂穿云刺数量计算
        if self.次数输入[self.技能序号['万剑归宗(穿云刺)']] == '/CD':
            穿云刺数量 = 0
            for i in self.技能栏:
                if i.是否主动 == 1:
                    if 技能释放次数[self.技能序号[i.名称]] <= 1:
                        穿云刺数量 += i.穿云刺数量(self.武器类型) * 技能释放次数[self.技能序号[i.名称]]
                    else:
                        穿云刺数量 += i.穿云刺数量(self.武器类型) * int(技能释放次数[self.技能序号[i.名称]] * 0.6)
            技能释放次数[self.技能序号['万剑归宗(穿云刺)']] = 穿云刺数量

        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)

        #剑魂特殊效果
        
        if self.技能栏[self.技能序号['极神剑术']].等级 != 0:

            极神剑术序号 = self.技能序号['极神剑术']
    
            技能释放次数[极神剑术序号] = 1
            
            if 技能总伤害[self.技能序号['破军升龙击']] != 0:
                temp = 技能总伤害[self.技能序号['破军升龙击']] * self.技能栏[self.技能序号['破军升龙击']].上斩百分比(self.武器类型) / self.技能栏[self.技能序号['破军升龙击']].等效百分比(self.武器类型) * (0.36 + 0.04 * self.技能栏[极神剑术序号].等级)
                if self.装备检查('奔流不息之狂风'):
                    技能总伤害[极神剑术序号] += temp / 0.7
                else:
                    技能总伤害[极神剑术序号] += temp
            
            if 技能总伤害[self.技能序号['猛龙断空斩']] != 0:
                temp =  技能总伤害[self.技能序号['猛龙断空斩']] * self.技能栏[self.技能序号['猛龙断空斩']].突进百分比(self.武器类型) / self.技能栏[self.技能序号['猛龙断空斩']].等效百分比(self.武器类型) * self.技能栏[self.技能序号['猛龙断空斩']].旋风倍率 * (0.19 + 0.02 * self.技能栏[极神剑术序号].等级)
                if self.装备检查('奔流不息之伽蓝'):
                    技能总伤害[极神剑术序号] += temp / 0.7
                else:
                    技能总伤害[极神剑术序号] += temp
    
            if 技能总伤害[self.技能序号['幻影剑舞']] != 0:
                temp = 技能总伤害[self.技能序号['幻影剑舞']] * self.技能栏[self.技能序号['幻影剑舞']].斩击百分比(self.武器类型) / self.技能栏[self.技能序号['幻影剑舞']].等效百分比(self.武器类型) * self.技能栏[self.技能序号['幻影剑舞']].影子多段攻击次数 * (0.50 + 0.05 * self.技能栏[极神剑术序号].等级)
                if self.武器类型 != '钝器':
                    if self.武器类型 == '短剑':
                        剑气次数 = 4
                    else:
                        剑气次数 = 3 
                    temp += 技能总伤害[self.技能序号['幻影剑舞']] * self.技能栏[self.技能序号['幻影剑舞']].剑气百分比(self.武器类型) / self.技能栏[self.技能序号['幻影剑舞']].等效百分比(self.武器类型) * 剑气次数 * (0.50 + 0.05 * self.技能栏[极神剑术序号].等级)
                else:
                    temp += 技能总伤害[self.技能序号['幻影剑舞']] * self.技能栏[self.技能序号['幻影剑舞']].剑气百分比(self.武器类型) / self.技能栏[self.技能序号['幻影剑舞']].等效百分比(self.武器类型) * 4.2 * (0.36 + 0.05 * self.技能栏[极神剑术序号].等级)
                
                if self.装备检查('奔流不息之岁月') or self.装备检查('英明循环之生命'):
                    技能总伤害[极神剑术序号] += temp / 0.7
                else:
                    技能总伤害[极神剑术序号] += temp
    
            if 技能总伤害[self.技能序号['极神剑术破空斩']] != 0:
                技能总伤害[self.技能序号['极神剑术破空斩']] += 技能总伤害[self.技能序号['极神剑术破空斩']] * self.技能栏[self.技能序号['极神剑术破空斩']].爆炸百分比(self.武器类型) / self.技能栏[self.技能序号['极神剑术破空斩']].等效百分比(self.武器类型) * (0.54 + 0.06 * self.技能栏[极神剑术序号].等级)
            
            if 技能总伤害[self.技能序号['极神剑术流星落']] != 0:
                temp = 技能总伤害[self.技能序号['极神剑术流星落']] / self.技能栏[self.技能序号['极神剑术流星落']].等效百分比(self.武器类型) * 3 * (2864.5 + 260.5 * self.技能栏[极神剑术序号].等级) * self.技能栏[self.技能序号['极神剑术流星落']].天剑倍率
        
                self.技能栏[self.技能序号['极神剑术流星落']].hit数 += 3
                self.技能栏[self.技能序号['极神剑术流星落']].天剑刺伤层数 = min((0.61 + 0.03 * self.技能栏[极神剑术序号].等级),1) * int((self.技能栏[极神剑术序号].等级 - 1) / 3 + 3)
        
                #极神剑术流星落护石效果：仅计基础3把天剑计算了加成，武器(钝器光剑)额外冲击波未计算加成
        
                if self.武器类型 == '巨剑':
                    temp += 技能总伤害[self.技能序号['极神剑术流星落']] / self.技能栏[self.技能序号['极神剑术流星落']].等效百分比(self.武器类型) * 3 * (2864.5 + 260.5 * self.技能栏[极神剑术序号].等级) * (0.10 + 0.01 * self.技能栏[极神剑术序号].等级)
        
                if self.武器类型 == '钝器':
                    temp += 技能总伤害[self.技能序号['极神剑术流星落']] / self.技能栏[self.技能序号['极神剑术流星落']].等效百分比(self.武器类型) * 3 * (1772.7 + 163.3 * self.技能栏[极神剑术序号].等级)
        
                if self.武器类型 == '光剑':
                    # 大概只有74%  temp += 技能总伤害[self.技能序号['极神剑术流星落']] / self.技能栏[self.技能序号['极神剑术流星落']].等效百分比(self.武器类型) * 3 * (1098.8 + 197.2 * self.技能栏[极神剑术序号].等级)             
                    temp += 技能总伤害[self.技能序号['极神剑术流星落']] / self.技能栏[self.技能序号['极神剑术流星落']].等效百分比(self.武器类型) * 3 * 74 
        
                if '永恒不息之路[2]' in self.套装栏:
                    技能总伤害[极神剑术序号] += temp / 1.2
                else:
                    技能总伤害[极神剑术序号] += temp

        通用倍率 = 1.0
        通用倍率 *= self.技能栏[self.技能序号['光剑精通']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['短剑精通']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['巨剑精通']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['太刀精通']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['钝器精通']].加成倍率(self.武器类型)

        通用倍率 *= self.技能栏[self.技能序号['无我剑气']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['极鬼剑术斩铁式']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['极鬼剑术斩钢式']].加成倍率(self.武器类型)
        通用倍率 *= self.技能栏[self.技能序号['无形剑意']].加成倍率(self.武器类型)
        通用倍率 *= 1 + self.白兔子技能*0.20 + self.斗神之吼秘药*0.12 #默认无宠物

        if 技能总伤害[self.技能序号['里鬼剑术']] != 0:
            if self.武器类型 == '巨剑':
                技能释放次数[self.技能序号['巨剑精通']] = 1
                技能总伤害[self.技能序号['巨剑精通']] += self.技能栏[self.技能序号['巨剑精通']].里鬼附加百分比(self.武器类型) * 通用倍率 / self.技能栏[self.技能序号['里鬼剑术']].等效百分比(self.武器类型) / self.技能栏[self.技能序号['里鬼剑术']].被动倍率 * 技能总伤害[self.技能序号['里鬼剑术']]
            if self.武器类型 == '短剑':
                技能释放次数[self.技能序号['短剑精通']] = 1
                技能总伤害[self.技能序号['短剑精通']] += self.技能栏[self.技能序号['短剑精通']].里鬼附加百分比(self.武器类型) * 通用倍率 / self.技能栏[self.技能序号['里鬼剑术']].等效百分比(self.武器类型) / self.技能栏[self.技能序号['里鬼剑术']].被动倍率 * 技能总伤害[self.技能序号['里鬼剑术']]
        
        if self.武器类型 == '太刀':
            总hit = 0
            太刀精通序号 = self.技能序号['太刀精通']
            for i in self.技能栏:
                if i.是否主动 == 1 and i.等级 != 85:
                    总hit+= i.hit数 * 技能释放次数[self.技能序号[i.名称]]  
                    self.技能栏[太刀精通序号].刺伤层数 += i.额外刺伤层数(self.武器类型) * 技能释放次数[self.技能序号[i.名称]]
            self.技能栏[太刀精通序号].刺伤层数 += 总hit * self.技能栏[太刀精通序号].刺伤概率(self.武器类型)
            技能释放次数[太刀精通序号] = 1
            技能总伤害[太刀精通序号] = self.技能栏[太刀精通序号].刺伤百分比(self.武器类型) * 通用倍率 *self.伤害指数

        if self.技能栏[self.技能序号['拔刀斩']].触发神影手 == 1 and 技能总伤害[self.技能序号['拔刀斩']] != 0:
            技能释放次数[self.技能序号['神影手']] = 技能释放次数[self.技能序号['拔刀斩']]
            神影手倍率 = 1.0
            神影手倍率 *= self.技能栏[self.技能序号['光剑精通']].加成倍率(self.武器类型)
            神影手倍率 *= self.技能栏[self.技能序号['短剑精通']].加成倍率(self.武器类型)
            神影手倍率 *= self.技能栏[self.技能序号['巨剑精通']].加成倍率(self.武器类型)
            神影手倍率 *= self.技能栏[self.技能序号['太刀精通']].加成倍率(self.武器类型)
            神影手倍率 *= self.技能栏[self.技能序号['钝器精通']].加成倍率(self.武器类型)

            比例 = self.技能栏[self.技能序号['神影手']].百分比 * self.伤害指数 * 神影手倍率 /self.主BUFF / 技能单次伤害[self.技能序号['拔刀斩']]
            技能总伤害[self.技能序号['神影手']] = 比例 * 技能总伤害[self.技能序号['拔刀斩']]
            
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据

class 极诣剑魂(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣剑魂角色属性()
        self.角色属性A = 极诣剑魂角色属性()
        self.角色属性B = 极诣剑魂角色属性()
        self.一觉序号 = 极诣剑魂一觉序号
        self.二觉序号 = 极诣剑魂二觉序号
        self.三觉序号 = 极诣剑魂三觉序号
        self.护石选项 = copy.deepcopy(极诣剑魂护石选项)
        self.符文选项 = copy.deepcopy(极诣剑魂符文选项)


    def 界面(self):
        super().界面()

        self.流心刺状态=QCheckBox('空中释放流心刺',self.main_frame2)
        self.流心刺状态.resize(120,20)
        self.流心刺状态.move(315,595)
        self.流心刺状态.setStyleSheet(复选框样式)
        self.流心刺状态.setToolTip('除钝器外其它武器生效')

        self.流心跃状态=QCheckBox('空中释放流心跃',self.main_frame2)
        self.流心跃状态.resize(120,20)
        self.流心跃状态.move(315,625)
        self.流心跃状态.setStyleSheet(复选框样式)
        self.流心跃状态.setToolTip('仅钝器生效')

    def 输入属性(self, 属性):
        super().输入属性(属性)
        if self.流心刺状态.isChecked():
            属性.流心刺状态 = 1
        if self.流心跃状态.isChecked():
            属性.流心跃状态 = 1

