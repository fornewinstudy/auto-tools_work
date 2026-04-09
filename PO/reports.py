import unittest,time
from unittestreport import TestRunner
import os,sys

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

# 定制测试报告的名称
report_name = time.strftime("%Y-%m-%d_%H_%M_%S")+"_report.html" #保存的文件是已html结尾

#调用单元测试框架中的方法testcass目录下发现以点py结尾文件，将其放置在test_suite中
case_path = os.path.join(os.path.dirname(__file__),'testcases')
test_suite = unittest.defaultTestLoader.discover(case_path,pattern="*.py")



#定制测试报告内容
report  =  TestRunner(suite=test_suite,
                      filename=report_name,
                      report_dir="report",
                      title="Pimow割草机测试报告(DVT3)",
                      tester="陈嘉鸿",
                      desc="Pimow割草机接口自动化测试报告",
                      templates=3)

#运行并生成测试报告
report.run()
