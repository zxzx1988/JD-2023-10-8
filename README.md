# 更新日期2023.10.10目前JD 的PC端无法使用，（只支持APP协议）
# 本项目项目包赞助388(好货不便宜，便宜没好货)，介意的朋友请勿打扰。
# 赞助邮箱：2972306946@qq.com （如果QQ添加失败可以把你的联系方式发送到邮箱，我会加你。)
- 👋 目前华为手机一机难求，茅子抢购更是难上加难，需求量超级火爆，闲来无事，研究了一下怎么抢购，成功率还可以。
# 注意点：
- JDplus积分越高越好：（查询方式赞助后咨询）
- 下单时间设定：11.59.59.800（根据个点电脑动态修正）
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
- 参考big大佬之前提供的解决思路
此次基于原有的代码进行了修改，提高了抢购稳定性； JD 茅台；华为手机。

