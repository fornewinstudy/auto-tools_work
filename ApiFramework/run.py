#!/usr/bin/env python3
# @Time : 2026/1/30 17:29
# @Author : 潘璐璐
import unittest,time
from unittestreport import TestRunner

# 定制测试报告的名称
report_name = time.strftime("%Y-%m-%d_%H_%M_%S") + "_report.html"

# 调用单元测试框架中的方法去testcases目录下发现以test开头，点py结尾文件，将其放置到test_suite中
test_suite = unittest.defaultTestLoader.discover("testcases",pattern="test*.py")

# 定制测试报告的内容
report = TestRunner(suite=test_suite,
                    filename=report_name,
                    report_dir="report",
                    title="生鲜超市测试报告",
                    tester="潘璐璐",
                    desc="生鲜超市接口自动化测试报告",
                    templates=2)
# 运行并生成测试报告
report.run()