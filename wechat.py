# -*- coding: utf-8 -*-
#!/Users/tesths/.pyenv/shims/python

import sys
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

infile = sys.argv[1]
f = open(infile,'r')
body = f.read()
f.close()

# p
body = re.sub(r'<p[^>]*?>([\s\S]+?)</p>','''<p style="margin: 1.5em 15px !important;color: #898989;">\g<1></p>''',body)

# h1

if re.search(r'<h1[^>]*?>\s*(\d+?)\s*</h1>',body)!=None:
	num = int(re.search(r'<h1[^>]*?>\s*(\d+?)\s*</h1>',body).group(1))/600
	body = re.sub(r'<h1[^>]*?>\s*(\d+?)\s*</h1>','<section data-role="outer" style="font-size:16px;"><section style="height: 40px;z-index:0;margin: 10px 10px 30px 10px; color: rgb(102, 102, 102); text-align: center; font-size: 16px; border-style: solid; -webkit-border-image: url(http://mmbiz.qpic.cn/mmbiz_png/fgnkxfGnnkS3q7kcqWSIgKyScCBibjiasG37kbbicr3XQdqQjKoOJH1MVZDPaSQIQaGjEWSXwQTia7TqkszDg3ItRw/0?wx_fmt=png) 130 fill; border-width: 20px; box-sizing: border-box;"><p data-brushtype="text" style="white-space: normal;margin-top: -13px;">读完本文大约需要<strong> '+str(num)+' </strong>分钟<span style=""></span></p></section></section></section></section>',body)

body = re.sub(r'<h1[^>]*?>([^<]+?)</h1>','<section data-role="outer" style="font-size:16px;"><section style="height: 40px;z-index:0;margin: 10px 10px 30px 10px; color: rgb(102, 102, 102); text-align: center; font-size: 16px; border-style: solid; -webkit-border-image: url(http://mmbiz.qpic.cn/mmbiz_png/fgnkxfGnnkS3q7kcqWSIgKyScCBibjiasG37kbbicr3XQdqQjKoOJH1MVZDPaSQIQaGjEWSXwQTia7TqkszDg3ItRw/0?wx_fmt=png) 130 fill; border-width: 20px; box-sizing: border-box;"><p data-brushtype="text" style="white-space: normal;margin-top: -13px;">读完本文大约需要<strong>\g<1></strong>分钟<span style=""></span></p></section></section></section></section>',body)

# h2
body = re.sub(r'<h2[^>]*?>([^<]+?)</h2>','''<h2 style="font-size: 20px;margin: 5px 0px;padding-bottom: 0px;position: relative;">\g<1></h2><h2 style="font-size: 10px; margin-top: 0px; margin-bottom: 10px;white-space: normal; max-width: 100%; color: white; border-left-width: 35px; border-left-style: solid; border-left-color: #2196F3; background: #64B5F6;padding: 4;font-weight: bold;font-style: bold !important;color: #3E3E3E !important;text-align: left !important;padding: 0.5em 0;color: #424242;"></h2>''',body)

# h3
body = re.sub(r'<h3[^>]*?>([^<]+?)</h3>','''<h3 style="font-size: 18px;margin: 5px 5px;padding-bottom: 0px;position: relative;">\g<1></h3><h3 style="font-size: 8px; margin-top: 0px; margin-bottom: 10px;margin-left: 5px;white-space: normal; max-width: 100%; color: white; border-left-width: 35px; border-left-style: solid; border-left-color: #42A5F5; background: #90CAF9;padding: 4;font-weight: bold;font-style: bold !important;color: #3E3E3E !important;text-align: left !important;padding: 0.5em 0;color: #424242;"></h3>''',body)

# h4
body = re.sub(r'<h4[^>]*?>([^<]+?)</h4>','''<h4 style="font-size: 16px;margin: 5px 10px;padding-bottom: 0px;position: relative;">\g<1></h4><h4 style="font-size: 6px; margin-top: 0px; margin-bottom: 10px;margin-left: 10px;white-space: normal; max-width: 100%; color: white; border-left-width: 35px; border-left-style: solid; border-left-color: #42A5F5; background: #90CAF9;padding: 4;font-weight: bold;font-style: bold !important;color: #3E3E3E !important;text-align: left !important;padding: 0.5em 0;color: #424242;"></h4>''',body)

# h5
body = re.sub(r'<h5[^>]*?>([^<]+?)</h5>','''<h5 style="margin: 20px 0 10px;padding: 4;font-weight: bold;font-style: bold !important;color: #3E3E3E !important;text-align: left !important;margin:1em auto;padding: 0.5em 0;color: #424242;">\g<1></h5>''',body)

# h6
body = re.sub(r'<h6[^>]*?>([^<]+?)</h6>','''<h6 style="margin: 20px 0 10px;padding: 4;font-weight: bold;font-style: bold !important;color: #3E3E3E !important;text-align: left !important;margin:1em auto;padding: 0.5em 0;color: #424242;">\g<1></h6>''',body)

# strong
body = re.sub(r'<strong[^>]*?>([^<]+?)</strong>','''<strong style="color: #4D4D4B;font-weight: bold;font-style: bold !important;">\g<1></strong>''',body)

# b
body = re.sub(r'<b[^>]*?>([^<]+?)</b>','''<b style="color: #898989;font-weight: bold;font-style: bold !important;">\g<1></b>''',body)

# em
body = re.sub(r'<em[^>]*?>([^<]+?)</em>','''<em style="color: #424242;">\g<1></em>''',body)

# i
body = re.sub(r'<i[^>]*?>([^<]+?)</i>','''<i style="color: #424242;">\g<1></i>''',body)

# hr
body = re.sub(r'<hr[^>]*?>([^<]+?)</hr>','''<hr style="border: 1px solid #C5E1A5;margin: 1.5em auto;">\g<1></hr>''',body)

# ol
body = re.sub(r'<ol[^>]*?>([\s\S]+?)</ol>','''<ol style="color:#2196F3;margin:0px 0px 20px 10px;">\g<1></ol>''',body)

# li
body = re.sub(r'<li[^>]*?>([\s\S]+?)</li>','''<li style="margin: 10px;"><p style="color:#898989;margin:0px 0px 0 5px;">\g<1></p></li>''',body)

# ul
body = re.sub(r'<ul[^>]*?>([^<]+?)</ul>','''<ul style="list-style-type: circle;margin: 10px 5px;">\g<1></ul>''',body)

# dl
body = re.sub(r'<dl[^>]*?>([^<]+?)</dl>','''<dl style="padding: 0;margin: 10px 5px;font-size: 1em;font-weight: bold;font-style: italic;margin: 0 0 10px;padding: 0 10px;">\g<1></dl>''',body)

# dt
body = re.sub(r'<dt[^>]*?>([^<]+?)</dt>','''<dt style="font-size: 1em;font-weight: bold;font-style: italic;margin: 0 0 10px;padding: 0 10px;">\g<1></dt>''',body)

# dd
body = re.sub(r'<dd[^>]*?>([^<]+?)</dd>','''<dd style="font-size: 1em;font-weight: bold;font-style: italic;margin: 0 0 10px;padding: 0 10px;">\g<1></dd>''',body)

# q
body = re.sub(r'<q[^>]*?>([^<]+?)</q>','''<q style="margin: 10px 5px;border-left: 8px solid #64B5F6;padding-top: 1px;padding-bottom: 1px;color: #777777;quotes: none;margin-left: 15px;background-color: #E3F2FD;">\g<1></q>''',body)

# blockquote
body = re.sub(r'<blockquote[^>]*?>([\s\S]+?)</blockquote>','''<blockquote style="margin: 20px 15px 20px 15px;border-left: 8px solid #64B5F6;padding-top: 1px;padding-bottom: 1px;color: #777777;quotes: none;background-color: #E3F2FD;">\g<1></blockquote>''',body)

# blockquote p

allblockquote = re.findall(r'(<blockquote[^>]*>[\s\S]+?</blockquote>)',body)

subnum = len(allblockquote)
waitfilled = re.sub(r'<blockquote[^>]*>[\s\S]+?</blockquote>','%s',body)

if len(re.findall('%',waitfilled))!=subnum:
    waitfilled=re.sub(u'%(?!s)','∉'.decode("utf-8"),waitfilled) 

allfilled = []

for item in allblockquote:
    deal_item = re.sub(r'<p[^>]*>([\s\S]*?)</p>','<p style="margin: 10px 10px 10px 10px;">\g<1></p>',item)
    allfilled.append(deal_item)
    
body = waitfilled%tuple(allfilled)

body=re.sub("∉".decode("utf-8"),'%',body)

# 默认 body

html = '''<html>
<head>
  <meta charset="utf-8">


	
</head>
<body style="font-family: sans-serif;font-size: 15px;line-height: 28px;letter-spacing: 1px;word-wrap: break-word !important;">
    %s
</body>


</html>'''%body

# 打开文件修改

f = open(infile,'w')
f.write(html)
f.close()
