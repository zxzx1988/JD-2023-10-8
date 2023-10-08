# JD-2023-10-8
JD， 京东，茅台，maptai，hw,华为手机 23年 10月8日更新   最新可用
# 本项目项目包需要赞助哈，介意的朋友请勿打扰。
- 👋 目前华为手机一机难求，茅子抢购更是难上加难，需求量超级火爆，闲来无事，研究了一下怎么抢购，成功率还可以。
# 具体思路如下：
- 👀 1.反编译app 获取sign逻辑,uuid和其他参数加密算法；
- 🌱 2.获取CK，协议头，根据data参数提交post请求
- 💞️ 3.抢购时，每个步骤通过session保留上一步的cookies
- 📫 4.获取抢购跳转连接，详细步骤如下：
- 抓包分析过程：
- 1.genToken
- to body 携带参数：{"action":"to","to":"https%3A%2F%2Fdivide.jd.com%2Fuser_routing%3FskuId%3D100012043978%26from%3Dapp"}
- 2.jmp
- https://divide.jd.com/user_routing?skuId=100012043978&from=app
- 3.divide
- 4.captcha
- 5.init.action
- 接口为：POST https://marathon.jd.com/seckillnew/orderService/init.action
- 6.提交订单，
- 提交接口为：POST https://marathon.jd.com/seckillnew/orderService/submitOrder.action?skuId=100012043978 HTTP/1.1提交参数为：
- "num": ,"addressId": "yuShou": "isModifyAddress": "name": "provinceId":"provinceName": "cityId": "cityName": "countyId": "countyName": "townId": "townName": "addressDetail": "mobile": "mobileKey": "email": "","invoiceTitle":"invoiceContent": "invoicePhone": "invoicePhoneKey": "invoice": "codTimeType": "paymentType": "overseas": "token":现在的订单接口已经不需要SK~OK 搞定~~
- 参考big大佬之前提供的解决思路
此次基于原有的代码进行了修改，提高了抢购稳定性； 支持JD 茅台；支持华为手机。
# 赞助邮箱：2972306946@qq.com （如果QQ添加失败可以把你的联系方式发送到邮箱，我会加你。)
