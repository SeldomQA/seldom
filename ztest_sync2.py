from seldom.utils import jsonpath
from jsonpath import jsonpath


testdata = {
    "code": 0,
    "status": 1,
    "data": {
        "list": [
            {
                "stockOutId": "1467422726779043840",
                "orderId": "1467422722362441728",
                "id": "1467422722362441728",
                "stockOutStatus": {
                    "name": "待出库",
                    "value": 0,
                    "description": "待出库"
                },
                "orderStatus": {
                    "name": "待付款",
                    "value": 0,
                    "description": "待付款"
                },
                "orderPayType": {
                    "name": "货到付款",
                    "value": 1,
                    "description": "货到付款"
                },
                "orderDeliveryWay": {
                    "name": "物流配送",
                    "value": 0,
                    "description": "物流配送"
                },
                "orderTradeType": {
                    "name": "即时到帐交易",
                    "value": 4,
                    "description": "即时到帐交易"
                },
                "stockOutType": {
                    "name": "制单出库",
                    "value": 1,
                    "description": "制单出库"
                },
                "creator": 9002257,
                "reviser": 9002257,
                "createTime": "2021-12-05 17:16:55",
                "shippingFee": 0,
                "totalAmount": 629,
                "sumProductPayment": 629,
                "currency": "RMB",
                "toFullName": "张德天",
                "toAddress": None,
                "toFullAddress": "湖北省武汉市洪山区街道口",
                "storageName": "初始仓库",
                "orderTime": "2021-12-05 17:16:55",
                "isSplit": 0,
                "packageNum": "1/1",
                "stockOutCreateTime": "2021-12-05 17:16:56",
                "stockOutToFullName": "张德天",
                "stockOutToFullAddress": "湖北省武汉市洪山区街道口",
                "creatorName": "监狱账号联系人",
                "stockOutTotalQuantity": 5,
                "stockOutTotalAmount": 629,
                "reviserName": "监狱账号联系人",
                "outNo": "WB20211206171552638541",
                "tenantId": 363635127,
                "orderNo": "WD20211205622150001",
                "stockOutOutNo": "WB20211206171552638541",
                "toReceiveTime": "2021-12-05 17:16:55",
                "stockOutBespeakTime": "2021-12-05 17:15:00",
                "stockOutNo": "CK2021120562128001"
            },
            {
                "stockOutId": "1467512423597473792",
                "orderId": "1467512420523048960",
                "id": "1467512420523048960",
                "stockOutStatus": {
                    "name": "待出库",
                    "value": 0,
                    "description": "待出库"
                },
                "orderStatus": {
                    "name": "待发货",
                    "value": 1,
                    "description": "待发货"
                },
                "orderPayType": {
                    "name": "货到付款",
                    "value": 1,
                    "description": "货到付款"
                },
                "orderDeliveryWay": {
                    "name": "物流配送",
                    "value": 0,
                    "description": "物流配送"
                },
                "orderTradeType": {
                    "name": "即时到帐交易",
                    "value": 4,
                    "description": "即时到帐交易"
                },
                "stockOutType": {
                    "name": "销售出库",
                    "value": 0,
                    "description": "销售出库"
                },
                "creator": 9002257,
                "reviser": 9002257,
                "createTime": "2021-12-05 23:13:20",
                "reviseTime": "2021-12-05 23:14:00",
                "status": 0,
                "storageId": 101888,
                "no": "WD20211205836010001",
                "sumProductPayment": 880.6,
                "refundAmount": 0,
                "buyerFeedback": "发新鲜货，尽快发货",
                "buyerLevel": "",
                "sellerId": "3e703f8e28c54d86b3e67fecc1dbff67",
                "sellerName": "监狱公司-2416",
                "toDivisionCode": "长安区",
                "toTownCode": "",
                "shopName": "监狱公司-2416",
                "toAddress": "火车站",
                "toFullAddress": "河北省石家庄市长安区火车站",
                "payStatus": "未支付",
                "orderPayWay": 0,
                "valetPayStatus": 0,
                "storageName": "初始仓库",
                "stockOutCreateTime": "2021-12-05 23:13:21",
                "stockOutToFullName": "张德天",
                "stockOutToFullAddress": "河北省石家庄市长安区火车站",
                "creatorName": "监狱账号联系人",
                "stockOutTotalQuantity": 7,
                "stockOutTotalAmount": 880.6,
                "orderNo": "WD20211205836010001",
                "stockOutOutNo": "2112058359100014846",
                "stockOutNo": "CK2021120583602001"
            }
        ],
        "pageIndex": 0,
        "pageSize": 50,
        "total": 2,
        "pageCount": 1,
        "data": {
            "addRepairOrder": True,
            "cancelOrder": True
        }
    },
    "message": "操作成功。",
    "isSuccessed": True
}
# 匹配message值
# 常规匹配：
print(testdata["message"])
# jsonpath匹配(取出来是个列表)
print(jsonpath(testdata, '$..message'))
# 去列表
print(jsonpath(testdata, '$..message')[0])
# 匹配list值
print(jsonpath(testdata, '$..list')[0])
# 匹配stockOutId值
print(jsonpath(testdata, '$..stockOutId'))
# 匹配stockOutStatus值
print(jsonpath(testdata, '$..stockOutStatus'))

# 匹配data下所有的元素
print(jsonpath(testdata, '$.data.*'))
# 匹配data下list所有的orderId值
print(jsonpath(testdata, '$.data.list[*].orderId'))
print(jsonpath(testdata, '$..orderId'))
# 匹配data下list中倒数第一个orderId值
print(jsonpath(testdata, '$.data.list[*].orderId')[-1])
# 匹配data--list下所有的stockOutType值
print(jsonpath(testdata, '$.data..stockOutType'))
print(jsonpath(testdata, '$..stockOutType'))
# 匹配data--list下第二个stockOutType中的description值
print(jsonpath(testdata, '$.data..stockOutType.description')[1])
# 匹配data--list下所有orderTradeType中所有的name值

print(jsonpath(testdata, '$..orderTradeType.name'))
# 匹配data--list中包含OutOutNo的所有列表值，并返回stockOutOutNo值
print(jsonpath(testdata, '$..list[?(@.stockOutOutNo)].stockOutOutNo'))
# 匹配data--list下sumProductPayment>800的所有值，是把list中满足条件的值列出来
print(jsonpath(testdata, '$..list[?(@.sumProductPayment>800)]'))
# 匹配data--list下sumProductPayment>800的所有值，并取出sumProductPayment的值
print(jsonpath(testdata, '$..list[?(@.sumProductPayment>800)].sumProductPayment'))
# 匹配orderPayType的所有值
print(jsonpath(testdata, '$..orderPayType'))
# 匹配orderPayType中所有的valve值
print(jsonpath(testdata, '$..orderPayType.*'))
# 匹配orderPayType返回的多个结果中的第一个
print(jsonpath(testdata, '$..orderPayType')[0])
# 匹配orderPayType中的description值
print(jsonpath(testdata, '$..orderPayType.description'))


# import seldom
# from seldom import ChromeConfig
# from seldom import Steps
# from seldom import Seldom,skip
# from selenium import webdriver
# from seldom import data
# # conftest.py
#
#
# class BaiduTest(seldom.TestCase):
#
#     def test_case_one(self):
#         """a simple test case """
#         self.open("https://www.baidu.com")
#         self.type(id_="kw", text="seldom")
#         self.click(css="#su")
#         self.assertTitle("seldom_百度搜索")
#
#     def _search_setting(self):
#         """百度搜索设置"""
#         Steps(url="http://www.baidu.com", desc="百度搜索设置")\
#             .open()\
#             .find("#s-usersetting-top").click()\
#             .find("#s-user-setting-menu > div > a.setpref").click().sleep(2) \
#             .screenshots() \
#             .find('[data-tabid="advanced"]').click().sleep(2) \
#             .find("#q5_1").click().sleep(2) \
#             .screenshots() \
#             .find('[data-tabid="general"]').click().sleep(2) \
#             .screenshots() \
#             .find_text("保存设置").click() \
#             .alert().accept()
#
#
# if __name__ == '__main__':
#     ChromeConfig.command_executor = r"D:\webdriver\chromedriver.exe"
#     seldom.main(path="./test_dir/",
#                 browser="gc",
#                 title="xxx项目",
#                 tester="虫师",
#                 description="adfasd",
#                 rerun=3, save_last_run=False, whitelist=["test"])
#

