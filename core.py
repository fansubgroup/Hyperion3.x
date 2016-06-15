#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import re
import urllib
import http.client
from hashlib import md5
import random
import json
import shutil


def split_txt(file_for_split):
    
    # Usage: split the src file into cells
    
    #print '<Start split>'
    if not os.path.isdir('temp'):
        os.mkdir('temp')
    if not os.path.isdir('translate-result'):
        os.mkdir('translate-result')
    filename = file_for_split
    first_line = 1
    fp = open(filename, 'r')
    null_line_count = 1
    time_list = []
    english_list = []
    num_list = []
    null_list = []
    for f_miss in fp.readlines():
        f = f_miss.strip('\r\n')
        
        find_1x = re.findall(r"\-", f)
        find_2x = re.findall(r"\>", f)
        
        if len(find_1x):
            if len(find_2x):
                time_list.append(f)
                    
        find_english = re.findall("[A-Za-z]", f)
        f_mid = re.sub("\D", "", f)
        find_number = re.findall("[0-9]+", f_mid)
        if len(find_english):
            english_list.append(f)
        if len(find_1x) == 0:
            if len(find_english) == 0:
                if first_line:
                    if len(find_number) != 0:
                        num_list.append(f_mid)
                        first_line = 0
                else:
                    time_list.append(f)
                
        if len(find_1x) == 0:
            if len(find_2x) == 0:
                if len(find_english) == 0:
                    if len(find_number) == 0:
                        save_name = "%d_temp.txt" % null_line_count
                        save_fp = open('temp/%s' % save_name, 'a')
                        num_save = num_list[0]
                        save_fp.writelines(num_save)
                        save_fp.writelines('\n')
                        
                        time_line = time_list[0]
                        save_fp.writelines(time_line)
                        save_fp.writelines('\n')
                        
                        for e in english_list:
                            save_fp.writelines(e)
                            save_fp.writelines('\n')
                            
                        save_fp.writelines("\n")
                        save_fp.close()
                        null_line_count += 1
                        first_line = 1
                        
                        null_list.append(f)
                        for t in range(0, len(time_list)):
                            time_list.pop()
                        for e in range(0, len(english_list)):
                            english_list.pop()
                        for num in range(0, len(num_list)):
                            num_list.pop()
                        for nu in range(0, len(null_list)):
                            null_list.pop()
    #print '<End split>'


def get_trans_txt(input_file):
    
    #Usage: Return the translation lines
    
    english_pool = []
    find_english = re.compile("[A-Za-z]+")
    fp = open(input_file, 'r')
    for j in fp.readlines():
        is_word = find_english.findall(j)
        if len(is_word) == 0:
            continue
        elif len(is_word) != 0:
            english_pool.append(j)
    if fp:
        fp.close()
        return english_pool



def translation_txt(src, dst):
    
    #Usage: Translation the target file
    
    #print '<Start translation>'
    
    get_app = open('app.conf', 'r')
    appid = str(get_app.readline().strip('\n'))
    secretKey = str(get_app.readline().strip('\n'))
    get_app.close()
    loop = True
    count_num = 1
    english = []
    httpClient = None
    myurl = '/api/trans/vip/translate'
    while loop:
        txt_name = '%d_temp.txt' % count_num
        txt_name_after = 'temp/%s' % txt_name
        if os.path.exists(txt_name_after):
            if get_trans_txt(txt_name_after):
                english = get_trans_txt(txt_name_after)
                for q in english:
                    fromLang = src
                    toLang = dst
                    salt = random.randint(32768, 65536)
                    sign = appid+q+str(salt)+secretKey
                    sign = sign.encode('utf-8')
                    m1 = md5()
                    m1.update(sign)
                    sign = m1.hexdigest()
                    #sign = sign.decode('utf-8')
                    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
                    try:
                        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
                        httpClient.request('GET', myurl)
                        response = httpClient.getresponse()
                        u = response.read()
                        json_mid = json.loads(u.decode('utf-8'))
                        dict_trans = json_mid.get('trans_result')
                        dict_trans_mid = dict_trans[0]
                        result_mid = dict_trans_mid.get('dst')
                        result = result_mid
                        op = open(txt_name_after, 'a')
                        op.writelines(result)
                        op.write('\n')
                    finally:
                        if httpClient:
                            httpClient.close()
                count_num += 1
            else:
                continue
        else:
            loop = False
    #print '<End translation>'


def join_txt():
    
    #Usage: Merge the final result
    
    #print '<Start join>'
    join_judge = True
    nb = 1
    result_name = 'translate-result/result.docx'
    wp = open(result_name, 'a')
    while join_judge:
        file_path = '%d_temp.txt' % nb
        file_path_2 = 'temp/%s' % file_path
        if os.path.exists(file_path_2):
            dp = open(file_path_2, 'r')
            for k in dp.readlines():
                wp.writelines(k)
            wp.write('\n')
            nb += 1
            dp.close()
        else:
            join_judge = False
    wp.close()
    #print '<End join>'


def move_result(path):
    
    #Usage: Move the result to where user want to save 
    
    #print '<Start move>'
    if os.path.exists('translate-result/result.docx'):
        if os.path.isdir(path):
            pp = path + '/result.docx'
            shutil.copyfile('translate-result/result.docx', pp)


def delete_txt():
    
    #Usage: Delete the temp file
    
    #print('<Start delete>')
    remove_name = 'temp/%d_temp.txt'
    count = 1
    some_true = True
    while some_true:
        file_name = remove_name % count
        if os.path.exists(file_name):
            os.remove(file_name)
            count += 1
        else:
            some_true = False
    os.rmdir('temp')
    #print '<End delete>'

def main(file_for_translate):
    
    get_lang = open('hyperion.conf', 'r')
    src = str(get_lang.readline().strip('\n'))
    dst = str(get_lang.readline().strip('\n'))
    file_to_open = str(get_lang.readline().strip('\n'))
    file_to_save = str(get_lang.readline().strip('\n'))
    get_lang.close()
    
    split_txt(file_for_translate)
    translation_txt(src, dst)
    join_txt()
    if file_to_save:
        move_result(file_to_save)
    delete_txt()
