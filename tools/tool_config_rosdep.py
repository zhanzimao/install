# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils,CmdTask,FileUtils,AptUtils,ChooseTask
from .base import osversion
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.type = BaseTool.TYPE_CONFIG
        self.name = "模板工程"
        self.author = '小鱼'

    def install_rosdepc(self):
        CmdTask("sudo apt install python3-pip -y", 0).run()
        cmd_ret = CmdTask("sudo pip3 install -i https://mirrors.aliyun.com/pypi/simple rosdepc").run()
        if cmd_ret[0]!=0:
            # fix: https://fishros.org.cn/forum/topic/2981
            cmd_ret = CmdTask("sudo pip3 install -i https://mirrors.aliyun.com/pypi/simple rosdepc --break-system-packages").run()
        CmdTask("sudo rosdepc init", 0).run()
        CmdTask("sudo rosdepc fix-permissions", 0).run()
        PrintUtils.print_info('已为您安装好rosdepc,请使用:\nrosdepc update \n进行测试更新,最后欢迎关注微信公众号《鱼香ROS》')


    def run(self):
        #正式的运行
        self.install_rosdepc()
