# web_autotest_selenium
Python + Selenium web自动化测试
* 通过unittest框架的discover（）找到匹配测试用例，由HTMLTestRunner的run（）方法执行测试用例并生产最新的测试报告
* 调用new_report()函数找到测试报告目录下最新的测试报告，并返回测试报告的路径
* 将得到的最新测试报告的完整路径传给send_mail（）函数，实现发送邮件