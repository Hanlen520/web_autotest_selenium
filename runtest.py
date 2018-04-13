# @Author: cherong 
# @Date: 2018-04-13 09:49:10 
# @Last Modified by:   cherong 
# @Last Modified time: 2018-04-13 09:49:10 
import unittest,os,time,smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
#=================定义发送邮件=================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body =f.read()
    f.close

    smtpserver = 'smtp.qq.com'
    user = '739965647@qq.com'
    password = 'kerzawlpxyccbbge'
    sender ="739965647@qq.com"
    receiver = "cher@govlan.com"

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('自动化测试报告','utf-8')
    msg["From"]    = sender
    msg["To"]      = receiver

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("email has send out!")


#=====查找测试报告目录，找到最新的测试报告=========
def new_report(testreport):
    list =os.listdir(testreport)
    list.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,list[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':

#定义测试用例的目录为当前目录
    test_dir = './test_case'
    test_report = './report'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')


    #按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H.%M")

    #定义报告存放路径和文件名
    filename =test_report + "\\" + now + 'result.html'

    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况：')

    runner.run(discover)   #运行测试用例
    fp.close() # 关闭报告文件
   
    new_report =new_report(test_report)
    send_mail(new_report)     #发送测试报告