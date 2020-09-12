#Python3脚本，不适用于Python2
#!/usr/bin/envpython
#coding=utf-8
from bottle import route,run,template,request,static_file
import os
import time
 
# 此处需改为你的目录地址
img_path='/home/unixq/testHttpServer/img'	#定义上传文件的保存路径
 
# 此处可扩充为完整HTML
uploadPage='''
	<form action="upload" method="POST" enctype="multipart/form-data">
		<input type="file" name="data" />
    	<input type="submit" value="上传" />
	</form>
'''
 
@route('/upload')
def upload():
	return uploadPage
 
@route('/upload',method='POST')
def do_upload():
	uploadfile=request.files.get('data')		#获取上传的文件
	uploadfile.save(img_path,overwrite=True) 	#overwrite参数是指覆盖同名文件
	os.system('python3 imgProcess.py')			# 执行服务器本地Python脚本
	time.sleep(3)								# 等待3秒，待本地脚本执行完毕
	return u"转换成功，请点击<a href='/download/output.jpg'>下载文件</a>"
 
@route('/download/<filename:path>')
def download(filename):
	return static_file(filename,root=img_path,download=filename)
 
 
run(host='0.0.0.0',port=8899,debug=True)
