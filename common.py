import requests
from seldom.request import check_response


class Common:

    @check_response("获取用户名", 200, ret="headers.Account")
    def get_login_user(self):
        """
        调用接口获得用户名
        status_code: 检查接口返回的状态码
        ret: 定义接口返回的数据，默认 json 格式
        """
        headers = {"Account": "bugmaster"}
        r = requests.get("http://httpbin.org/get", headers=headers)
        return r


if __name__ == '__main__':
    c = Common()
    ret = c.get_login_user()
    print("ret", ret)

#
# from seldom.utils import jsonpath
# from seldom.utils import jmespath
#
# response = {
#     "code": 0,
#     "status": 1,
#     "data": {
#         "list": [
#             {
#                 "stockOutId": "1467422726779043840",
#                 "orderId": "1467422722362441728",
#                 "id": "1467422722362441728",
#                 "orderStatus": {
#                     "name": "待付款",
#                     "value": 0,
#                     "description": "待付款"
#                 },
#                 "orderPayType": {
#                     "name": "货到付款",
#                     "value": 1,
#                     "description": "货到付款"
#                 },
#                 "orderTradeType": {
#                     "name": "即时到帐交易",
#                     "value": 4,
#                     "description": "即时到帐交易"
#                 },
#                 "stockOutType": {
#                     "name": "制单出库",
#                     "value": 1,
#                     "description": "制单出库"
#                 },
#                 "shippingFee": 0,
#                 "sumProductPayment": 629,
#                 "currency": "RMB",
#                 "packageNum": "1/1",
#                 "stockOutToFullName": "张德天",
#                 "stockOutToFullAddress": "湖北省武汉市洪山区街道口",
#             },
#             {
#                 "stockOutId": "1467512423597473792",
#                 "orderId": "1467512420523048960",
#                 "id": "1467512420523048960",
#                 "orderStatus": {
#                     "name": "待发货",
#                     "value": 1,
#                     "description": "待发货"
#                 },
#                 "orderPayType": {
#                     "name": "货到付款",
#                     "value": 1,
#                     "description": "货到付款"
#                 },
#                 "orderTradeType": {
#                     "name": "即时到帐交易",
#                     "value": 4,
#                     "description": "即时到帐交易"
#                 },
#                 "stockOutType": {
#                     "name": "销售出库",
#                     "value": 0,
#                     "description": "销售出库"
#                 },
#                 "status": 0,
#                 "storageId": 101888,
#                 "no": "WD20211205836010001",
#                 "sumProductPayment": 880.6,
#                 "stockOutToFullName": "张德天",
#                 "stockOutToFullAddress": "河北省石家庄市长安区火车站",
#             }
#         ],
#         "pageSize": 50,
#         "total": 2,
#         "pageCount": 1,
#     },
#     "message": "操作成功。",
#     "isSuccessed": True
# }
#
# # ==============常规匹配：====================
# print(response["message"])
# print(response["data"]["list"])
# print(response["data"]["list"][0])
# print(response["data"]["list"][0]["orderId"])
#
# # ========== jmespath提取器 =================
# # jmespath 匹配消息
# print(jmespath(response, 'message'))
#
# # jmespath 匹配list列表
# print(jmespath(response, 'data.list'))
#
# # jmespath 匹配list列表第一个元素
# print(jmespath(response, 'data.list[0]'))
#
# # jmespath 匹配list列表第二个元素下的 orderId
# print(jmespath(response, 'data.list[1].orderId'))
#
# # ============jsonpath用法 =================
# # jsonpath匹配(取出来是个列表)
# print(jsonpath(response, '$..message'))
#
# # 取列表
# print(jsonpath(response, '$..message')[0])
#
# # 匹配list值
# print(jsonpath(response, '$..list')[0])
#
# # 匹配stockOutId值
# print(jsonpath(response, '$..stockOutId'))
#
# # 匹配data下所有的元素
# print(jsonpath(response, '$.data.*'))
#
# # 匹配data下list所有的orderId值
# print(jsonpath(response, '$.data.list[*].orderId'))
# print(jsonpath(response, '$..orderId'))
#
# # 匹配data下list中倒数第一个orderId值
# print(jsonpath(response, '$.data.list[*].orderId')[-1])
#
# # 匹配data--list下所有的stockOutType值
# print(jsonpath(response, '$.data..stockOutType'))
# print(jsonpath(response, '$..stockOutType'))
#
# # 匹配data--list下第二个stockOutType中的description值
# print(jsonpath(response, '$.data..stockOutType.description')[1])
#
# # 匹配data--list下所有orderTradeType中所有的name值
# print(jsonpath(response, '$..orderTradeType.name'))
#
# # 匹配data--list中包含OutOutNo的所有列表值，并返回stockOutOutNo值
# print(jsonpath(response, '$..list[?(@.stockOutOutNo)].stockOutOutNo'))
#
# # 匹配data--list下sumProductPayment>800的所有值，是把list中满足条件的值列出来
# print(jsonpath(response, '$..list[?(@.sumProductPayment>800)]'))
#
# # 匹配data--list下sumProductPayment>800的所有值，并取出sumProductPayment的值
# print(jsonpath(response, '$..list[?(@.sumProductPayment>800)].sumProductPayment'))
#
# # 匹配orderPayType的所有值
# print(jsonpath(response, '$..orderPayType'))
#
# # 匹配orderPayType中所有的valve值
# print(jsonpath(response, '$..orderPayType.*'))
#
# # 匹配orderPayType返回的多个结果中的第一个
# print(jsonpath(response, '$..orderPayType')[0])
#
# # 匹配orderPayType中的description值
# print(jsonpath(response, '$..orderPayType.description'))
