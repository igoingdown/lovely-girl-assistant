import os
import subprocess

def foo():
	subprocess.call("/home/yizhi/sites/blogApp/demo/bin/demo $(cat /home/yizhi/sites/blogApp/demo/bin/source.txt)", shell=True)
	#subprocess.call("ls -l", shell=True)	
	pass


if __name__ == '__main__':
	foo()

