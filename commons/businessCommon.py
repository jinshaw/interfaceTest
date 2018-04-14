from commons import common
from commons import configHttp
import readConfig as readConfig
import json

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = common.get_xls("userCase.xlsx", "dLogin")
localAddAddress_xls = common.get_xls("userCase.xlsx", "dLogin")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = common.get_url_from_xml('dLogin')
    localConfigHttp.set_url(url)

    # set header
    # 改token
    token = common.get_visitor_token()
#    token = localReadConfig.get_headers("X-CSRF-TOKEN")
    header = {"token": token}
    localConfigHttp.set_headers(header)

    # set param
    # webForm中的参数
    data = {"mobile": localLogin_xls[0][3], "code": int(localLogin_xls[0][4])}
    localConfigHttp.set_params(data)

    # login
    response = localConfigHttp.post().json()
    token = common.get_visitor_token()
    print(response)
    return token

def checkUsername():
    """
    login
    :return: token
    """
    # set url
    url = common.get_url_from_xml('checkUsername')
    localConfigHttp.set_url(url)

    # set header
    # 改token
    token = common.get_visitor_token()
#    token = localReadConfig.get_headers("X-CSRF-TOKEN")
    header = {"token": token}
    localConfigHttp.set_headers(header)

    # set param
    # webForm中的参数
    data = {"username": localLogin_xls[0][3]}
    localConfigHttp.set_data(data)

    # login
    response = localConfigHttp.post().json()
#    token = common.get_value_from_return_json(response, "member", "token")
    token = common.get_visitor_token()
    print(response)
    return token

# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = common.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_headers(header)

    # logout
    localConfigHttp.get()

if __name__ == "__main__":
    print(login())

