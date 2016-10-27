#coding=utf-8

import os
import sys
import ctypes
#import sub_func
from sub_func import *

def bushound_parser() :

	##	-------------------------------------------------------------------------------------
	##	���Կ���
	##	-------------------------------------------------------------------------------------
	debug = 0;

	for i in range(0,len(sys.argv)):
		if(sys.argv[i]=="-d"):
			debug = 1;
			break;
#	debug = 1;
	print("debug is ",debug);

	##	===============================================================================================
	##	ref ***source file operation***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��ȡ�����ļ�
	##	-------------------------------------------------------------------------------------
	src_path = sys.argv[1];
	if(debug==1):	print("src_path is",src_path);

	##	-------------------------------------------------------------------------------------
	##	�ж�������Ƿ���һ���ļ�
	##	--��������ļ�����ӡ�����˳�
	##	--�����һ���ļ������ļ�
	##	-------------------------------------------------------------------------------------
	if(os.path.isfile(src_path)==False):	return -1
	if(debug==1):	print("src_path is really exist");
	infile	= open(src_path,"r")

	##	-------------------------------------------------------------------------------------
	##	��¼�ļ�������
	##	-------------------------------------------------------------------------------------
	file_content = infile.readlines();
	line_num = len(file_content);
	if(debug==1):	print("all line num is ",line_num);

	##	===============================================================================================
	##	ref ***read source file,search keyword***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��ͷ��ʼ�� �� "55 33 56 " ��Ϊһ���ļ���ʼ��
	##	-------------------------------------------------------------------------------------
	for i in range(0,line_num):
		line_content	= file_content[i];
		##	-------------------------------------------------------------------------------------
		##	���һ�еĿ�ͷ�� "------"����ô����Ϊ����������ݿ�ʼ
		##	-------------------------------------------------------------------------------------
		if(line_content.find("55 33 56 ")>=0):
			if(debug==1):	print("******find pattern line num is ",i);
			line_start=i;
			break
		##	-------------------------------------------------------------------------------------
		##	������һ�ж�û���ҵ�����ô����û��pattern���ͻ��˳�
		##	-------------------------------------------------------------------------------------
		if(i==line_num-1):
			if(debug==1):	print("******not found pattern");
			return -1

	##	-------------------------------------------------------------------------------------
	##	��һ���ж�λ"55 33 56 "���ֵ�λ��
	##	-------------------------------------------------------------------------------------
	first_byte_pos = file_content[line_start].find('55 33 56 ');
	if(debug==1):	print("first byte position is ",first_byte_pos);

	##	===============================================================================================
	##	ref ***parse file by keyword***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��line start��ʼ���� U3VC U3VL U3VT �Ĺؼ���
	##	-------------------------------------------------------------------------------------
	list_parser = [];
	for i in range(line_start,line_num):
		line_content	= file_content[i];
		if(line_content[first_byte_pos:first_byte_pos+11]=="55 33 56 43"):
			if(debug==1):	print("find U3VC");
			list_parser.append(u3vc_proc(debug,first_byte_pos,i,file_content));
		elif(line_content[first_byte_pos:first_byte_pos+11]=="55 33 56 4c"):
			if(debug==1):	print("find U3VL");
			list_parser.append(u3vl_proc(debug,first_byte_pos,i,file_content));
		elif(line_content[first_byte_pos:first_byte_pos+11]=="55 33 56 54"):
			if(debug==1):	print("find U3VT");
			list_parser.append(u3vt_proc(debug,first_byte_pos,i,file_content));

	##	===============================================================================================
	##	ref ***output result***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��Դ�ļ���·���õ�Ŀ���ļ�·��
	##	--��������ļ�������Դ�ļ�����+"_parser.txt"
	##	-------------------------------------------------------------------------------------
	temp = os.path.split(src_path);
	only_path = temp[0];
	temp = os.path.basename(src_path);
	temp = temp.split('.');
	only_name = temp[0];
	parser_name = only_name + "_parser.txt";
	summary_name = only_name + "_summary.txt";
	parser_path = only_path+'\\'+parser_name;
	summary_path = only_path+'\\'+summary_name;

	##	-------------------------------------------------------------------------------------
	##	���±༭file_content ��Ҫд����������ӵ�����
	##	--list_parser��һ����ά�б���ÿһ��Ԫ�ض���һ���б�������0�����кţ�1������������
	##	--Ҫ��list_parser�б��е��������ӵ���Ӧ���У�file_content�����һ���ַ��ǻس���Ҫȥ��
	##	-------------------------------------------------------------------------------------
	for i in range(0,len(list_parser)):
		file_content[list_parser[i][0]]	= file_content[list_parser[i][0]].rstrip("\n")+"\t#"+list_parser[i][1]+"\n";

	file_content_summay = list_parser;
	for i in range(0,len(list_parser)):
		file_content_summay[i]	= "line num is "+str(list_parser[i][0]+1)+"\t"+list_parser[i][1]+"\n";

	##	-------------------------------------------------------------------------------------
	##	�����µ��ļ�
	##	-------------------------------------------------------------------------------------
	outfile_parser = open(parser_path,"w+");
	outfile_summary = open(summary_path,"w+");

	##	-------------------------------------------------------------------------------------
	##	�����µ��ļ�
	##	-------------------------------------------------------------------------------------
	outfile_parser.writelines(file_content);
	outfile_summary.writelines(file_content_summay);

	##	===============================================================================================
	##	ref ***end***
	##	===============================================================================================
	outfile_parser.close()
	outfile_summary.close()
	infile.close()



#	path = "f:/test/UE_TMP.v"
#	infile = open(path,"r")
#	outfile = open("f:/test/UE_TMP1.v","w")
#	outfile.write("hello")
#
#
#	temp = os.path.split(src_path);
#	print('temp[1] is :',temp[1]);
#	print(os.path.basename(src_path));
#	u = os.path.basename(src_path);
#	v = u.split('.');
#	#	print(u.split(.));
#	print(v[0]);
#	#	print(os.path.split(path));
#
#	outfile.close()
#	infile.close()
##
###!/usr/bin/python
### -*- coding: UTF-8 -*-
##
##for letter in 'Python':     # ��һ��ʵ��
##   print '��ǰ��ĸ :', letter
##
##fruits = ['banana', 'apple',  'mango']
##for fruit in fruits:        # �ڶ���ʵ��
##   print '��ǰ��ĸ :', fruit
##
##print "Good bye!"

bushound_parser()

