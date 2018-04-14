import unittest
import paramunittest
import readConfig as readConfig
from commons import Log as Log
from commons import common
from commons import configHttp as ConfigHttp
import json

login_xls = common.get_xls("userCase.xlsx", "dLogin")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class CheckUsername(unittest.TestCase):
    def setParameters(self, case_name, method, token, username, codes, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param mobile:
        :param codes:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.username = str(username)
        self.codes = str(codes)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"测试开始前准备")

    def testCheckUsername(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('checkUsername')
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        # get visitor token
        if self.token == '0':
            token = common.get_visitor_token()
        elif self.token == '1':
            token = None

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        data = {"username": self.username}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[int(str(self.return_json.request).find('['))+1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method)

        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        """

        :return:
        """
        info = self.info
        if info['status'] == 1:
            # get uer token
            token_u = common.get_visitor_token()
            # set user token to config file
            localReadConfig.set_headers("TOKEN_U", token_u)
        else:
            pass
        self.log.build_case_line(self.case_name, str(self.info['status']), str(self.info['msg']))
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        check test result
        :return:
        """

        self.info = self.return_json.json()
       # show return message
        common.show_return_msg(self.return_json)
        print(self.info['data']['status'])
        if self.result.__eq__('0'):
            self.assertEqual(self.info['data']['status'],1,'OK')


if __name__ == "__main__":
    unittest.main()