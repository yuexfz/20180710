#!/usr/bin/env python3

class cfg:
        def __init__(self,JiShuL,JiShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin):
                with open('./test.cfg','r') as file:
                        for line in file:
                                _line=(line.split()
                                _cfg.append(_line[2])

                                self._JiShuL=_cfg[0]
                                self._JiShuH=_cfg[1]
                                self._YangLao=_cfg[2]
                                self._YiLiao=_cfg[3]
                                self._ShiYe=_cfg[4]
                                self._GongShang=_cfg[5]
                                self._ShengYu=_cfg[6]
                                self._GongJiJin=_cfg[7]
