#coding=utf-8

import os
import sys
import ctypes
##import sub_func
#from sub_func import *

def select_line() :

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
	##	ref ***Դ�ļ�����***
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
	##	ref ***�ҵ�pattern***
	##	===============================================================================================
	pattern1 = sys.argv[2];
	pattern2 = sys.argv[3];

	##	===============================================================================================
	##	ref ***���ļ� �ҹؼ���***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��� pattern1�ҵ��ˣ���ô���� pattern2 ������ҵ���˵��û������
	##	-------------------------------------------------------------------------------------
	list_parser = [];
	for i in range(0,line_num):
		line_content	= file_content[i];
		##	-------------------------------------------------------------------------------------
		##	��ÿһ������ pattern1
		##	-------------------------------------------------------------------------------------
		if(line_content.find(pattern1)>=0):
			if(debug==1):	print("******find pattern1 line num is ",i);
			##	-------------------------------------------------------------------------------------
			##	��ÿһ������ pattern2�����������pattern2����ô�Ϳ�������
			##	-------------------------------------------------------------------------------------
			if (line_content.find(pattern2)<0):
				list_parser.append(line_content);

	##	===============================================================================================
	##	ref ***����ļ�***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��Դ�ļ���·���õ�Ŀ���ļ�·��
	##	--��������ļ�������"select_line.txt"
	##	-------------------------------------------------------------------------------------
	temp = os.path.split(src_path);
	only_path = temp[0];
	path = only_path+'\\'+"select_line.txt";


	##	-------------------------------------------------------------------------------------
	##	�����µ��ļ�
	##	-------------------------------------------------------------------------------------
	outfile_summary = open(path,"w+");

	##	-------------------------------------------------------------------------------------
	##	�����µ��ļ�
	##	-------------------------------------------------------------------------------------
	for eachline in list_parser:
		outfile_summary.write(str(eachline));

	##	===============================================================================================
	##	ref ***����***
	##	===============================================================================================
	outfile_summary.close()
	infile.close()

select_line()

