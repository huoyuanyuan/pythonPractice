import subprocess
p = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
out,err = p.communicate()
for line in out.splitlines():
	print(line.decode("gbk"))