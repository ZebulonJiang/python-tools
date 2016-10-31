#coding=utf-8

import os
import sys
import ctypes
from sub_func import *

def rtl_parser() :

	##	-------------------------------------------------------------------------------------
	##	���Կ���
	##	-------------------------------------------------------------------------------------
	debug = 0;
#	debug = 1;
#	print("debug is ",debug);

	##	===============================================================================================
	##	ref ***source file operation***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	�жϴ�������ĸ���
	##	-------------------------------------------------------------------------------------
	if(len(sys.argv)==1):	print("please input filepath & word");
	if(len(sys.argv)==2):	print("please input word");

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
#	if(debug==1):	print("all line num is ",line_num);

	##	===============================================================================================
	##	ref ***read source file,search keyword***
	##	===============================================================================================
	##	-------------------------------------------------------------------------------------
	##	��ñ�ѡ�������
	##	-------------------------------------------------------------------------------------
	word_sel 		= sys.argv[2];
	line_content	= 0;
	all_list		= [];
	declare_list	= [];
	driver_list		= [];
	reference_list	= [];
	index_value		= 0;

	##	-------------------------------------------------------------------------------------
	##	��ͷ��ʼ������������ص����� ȫ����������
	##	-------------------------------------------------------------------------------------
	for i in range(0,line_num):
		line_content	= file_content[i];
		##	-------------------------------------------------------------------------------------
		##	ȥ��ע�� �س� �ַ������ߵĿո� tabת��Ϊ�ո�
		##	-------------------------------------------------------------------------------------
		try:
		    index_value = line_content.index("\n")
		except ValueError:
		    index_value = -1
		if(index_value!=-1): line_content	= line_content[0:index_value];

		try:
		    index_value = line_content.index("//")
		except ValueError:
		    index_value = -1
		if(index_value!=-1): line_content	= line_content[0:index_value];

		line_content	= line_content.replace("\t"," ");
		line_content	= line_content.strip();
		##	-------------------------------------------------------------------------------------
		##	����У����ȷŵ� reference_list����
		##	-------------------------------------------------------------------------------------
#		if(line_content.find(word_sel)>=0):
		if(find_word(line_content,word_sel)):
			all_list.append([line_content,i+1]);
#			print("line_content is",line_content);
#			print("i is",i);

	##	-------------------------------------------------------------------------------------
	##
	##	-------------------------------------------------------------------------------------
	for i in range(0,len(all_list)):
		line_content	= all_list[i][0];
		##	-------------------------------------------------------------------------------------
		##	�Ѹ�ֵ����֮ǰ�����ݽ�ȡ����
		##	-------------------------------------------------------------------------------------
		try:
		    index_value = line_content.index("=")
		except ValueError:
		    index_value = -1
		if(index_value!=-1): line_content	= line_content[0:index_value];

#		##	-------------------------------------------------------------------------------------
#		##	�����ģ��ӳ�䣬����Ҫ�������е����ݽ�ȡ����
#		##	-------------------------------------------------------------------------------------
#		try:
#		    index_value = line_content.index(".")
#		except ValueError:
#		    index_value = -1
#		if(index_value!=-1):
#			try:
#			    index_value = line_content.index("(")
#			except ValueError:
#			    index_value = -1
#			if(index_value!=-1):	line_content	= line_content[index_value+1:len(line_content)];
		##	-------------------------------------------------------------------------------------
		##	��� = ǰ������ѡ�ʣ���ô˵���������������߸�ֵ
		##	-------------------------------------------------------------------------------------
##		if(line_content.find(word_sel)>=0):
		if(find_word(line_content,word_sel)):
			##	-------------------------------------------------------------------------------------
			##	�ж��ǲ��Ǹ�ֵ���
			##	-------------------------------------------------------------------------------------
			if(line_content.split(' ')[0]=="assign"):
				driver_list.append(all_list[i]);
			elif(line_content.split(' ')[0][0:len(word_sel)]==word_sel):
				driver_list.append(all_list[i]);

			else:

				##	-------------------------------------------------------------------------------------
				##	��[]֮ǰ�����ݽ�ȡ����
				##	-------------------------------------------------------------------------------------
				try:
				    index_value = line_content.index("[")
				except ValueError:
				    index_value = -1
				if(index_value!=-1): line_content	= line_content[0:index_value];

				##	-------------------------------------------------------------------------------------
				##	�ж��ǲ����������
				##	-------------------------------------------------------------------------------------
				if(line_content.split(' ')[0]=="parameter"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="localparam"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="function"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="task"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="input"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="output"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="inout"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="wire"):
					declare_list.append(all_list[i]);
				elif(line_content.split(' ')[0]=="reg"):
					declare_list.append(all_list[i]);
				else:
					reference_list.append(all_list[i]);
		else:
			reference_list.append(all_list[i]);
	##	-------------------------------------------------------------------------------------
	##	���
	##	-------------------------------------------------------------------------------------
	##	-------------------------------------------------------------------------------------
	##	ͷ
	##	-------------------------------------------------------------------------------------
	print("https://github.com/fifoteam/python-tools/tree/master/rtl_parser v1.2 2016.10.31");
	print("src file is : ",src_path);
	print("selected word is \""+word_sel+"\"");
	print("find num :",len(all_list));
	##	-------------------------------------------------------------------------------------
	##	���ò���
	##	-------------------------------------------------------------------------------------
	print("***declaration***");
	for i in range(0,len(declare_list)):
		print(""+src_path+"("+str(declare_list[i][1])+"):"+declare_list[i][0]+"");

	##	-------------------------------------------------------------------------------------
	##	��������
	##	-------------------------------------------------------------------------------------
	print("***driver***");
	for i in range(0,len(driver_list)):
		print(""+src_path+"("+str(driver_list[i][1])+"):"+driver_list[i][0]+"");

	##	-------------------------------------------------------------------------------------
	##	���ò���
	##	-------------------------------------------------------------------------------------
	print("***reference***");
	for i in range(0,len(reference_list)):
		print(""+src_path+"("+str(reference_list[i][1])+"):"+reference_list[i][0]+"");

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

rtl_parser()


