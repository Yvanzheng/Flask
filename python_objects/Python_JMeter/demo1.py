# coding=utf-8

import os
import subprocess
import time
from string import Template

currpath = os.path.dirname(os.path.realpath(__file__))

JmxTemlFileName = r"/Users/Administrator/Desktop/apache-jmeter-3.2/test/test1.jmx"

JMETER_Home = r'''"/Users/Administrator/Desktop/apache-jmeter-3.2/bin/jmeter.sh"'''


def getDateTime():
	'''
	获取当前日期时间，格式'20170708085159'
	'''
	return time.strftime(r'%Y%m%d%H%M%S', time.localtime(time.time()))


def execcmd(command):
	print(f"command={command}")

	output = subprocess.Popen(
		command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
		universal_newlines=True)

	stderrinfo, stdoutinfo = output.communicate()
	print(f"stderrinfo={stderrinfo}")
	print(f"stdoutinfo={stdoutinfo}")
	print("returncode={0}".format(output.returncode))


def execjmxs(Num_Threads, Loops):
	with open(JmxTemlFileName, "r", encoding="utf-8") as file:
		tmpstr = Template(file.read()).safe_substitute(
			num_threads=Num_Threads,
			loops=Loops
		)
	now = getDateTime()
	tmpjmxfile = currpath + r"/T{0}XL{1}{2}.jmx".format(
		Num_Threads, Loops, now)
	with open(tmpjmxfile, "w+", encoding="utf-8") as file:
		file.writelines(tmpstr)
	csvfilename = currpath + "/result{0}.csv".format(now)
	htmlreportpath = currpath + "/htmlreport{0}".format(now)
	if not os.path.exists(htmlreportpath):
		os.makedirs(htmlreportpath)
	execjmxouthtml = f"cmd.exe /c {JMETER_Home} -n -t {tmpjmxfile} -l {csvfilename} -e -o {htmlreportpath}"
	execcmd(execjmxouthtml)


jobs = [dict(Num_Threads=x * 10, Loops=1000) for x in range(2, 21)]
[execjmxs(x["Num_Threads"], x["Loops"]) for x in jobs]
