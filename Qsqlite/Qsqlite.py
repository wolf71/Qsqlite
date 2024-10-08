'''
  Qsqlite Quick sqlite Tools
           (c) 2020 - 2022
           By: Charles Lai
'''

__version__ = 0.974
__author__ = 'Charles Lai'

help_str = '''
====== Qsqlite (Quick Sqlite Tools) Help (V0.974) ======
# command
 @ q - quit
 @ ?/h - help    or  ? querystr    etc: ? draw;    cls / clear - clear screen. (windows-cls, mac/linux-clear)
 @ #/-  comment;  three ' for block comment;    { } for multi-lines block code.  ( { and } on new line )
 @ l - List last 12 cmd History; la - List all History; l0 - run last cmd; l8 - run #8 cmd; l> file / l< file (save/load cmd History to/from file )
 @ exec script - Execute a Qsqlite Script, etc: exec qInit.txt
 @ ls - List current dir files; ls *.csv or ls city
 @ echo - Display information
 @ open dbname - open database(if db not exist, auto create it) / open :memory: 
 @ open #dbname# (open a mysql db)
 @ mysql - setup a mysql db, mysql dbname server user password ; and then using open #dbname# open it.(server support port,etc: server:3308)
 @ db - Show open database name  / @ dinfo on/off - debug info on/off or using dinfo show status
 @ info 0/1/2/3 - show database info; 0-table / 1-index (for MySQL 2-tables; 3-table struct)
 @ >[ _@1_, _@2_, ...] select result reformat. (_@0_ for order id)
 @ copy dbname table_insert sqlcmd (insert select data to table_insert)
 - etc: copy new.db tb01 select * from tb00 where age < 100 limit 10
 - !same db,can using: insert into tb01 select a,b,c from tb00 where a<10
 @ dump #mysqldb# sqlitedb (Dump mysql database to sqlite with data.)
 @ loadcsv - load csv file and copy to new table (and support .tsv file, bioinformatics .maf/.vcf/.sam/.gtf/.gff/.gpd/.gct file; support .gz or .zip file)
 - etc: loadcsv file.csv table1	 or loadcsv file.csv table1 1 (csv line 1 as title)
 - etc: loadcsv file.tsv.gz table1 or loadcsv file.gtf.zip
 @ loadgb - load bioinformatics genbank file features info to table. (etc: loadgb file tb01)
 @ >csv file.csv 1/0  export select result to csv/tsv file (0/1 - with/without rowinfo; file.tsv export tsv format; file.csv.gz export csv file and gzip.)
 @ loadjson - load json file and copy to new table
 - etc: loadjson file.json table1 item (when item set, it's will select data on json item.)
 @ loop/lend function . Etc: select i1,i2 from tab / select * from tab where a = _^1_ and b = '_^2_' /lend
 - or : loop [(1,2,...),(1,2,...)...] / echo _^0_ _^1_ / lend
 @ loop loadweb function. Etc: loop loadweb url=https://xxx.xxx/xxx re=href="/searc/(.+?)" ext=_^1_
 @ loop [ i for i in loadweb('url=https://xxx.xxx/xxx re=href="/searc/(.+?)" ext=_^1_')[:1] ] , using in [ ]
 @ loop [i for i in getTableCols('c')[4:]]  using getTableCols function transform table cols to rows
 @ download function. Etc: download https://xxx.xxx/xxx test.csv   will download file from web.
 @ draw type sqlcmd (Draw data using matplotlib. type: l-line h-hist v-violin s-scatter)
 - draw l select x_lable,col1,col2 from tab1 (*first col using for matplot x-laxble) / draw ls (subplot mode)
 - draw lx select x,y from tab ( log(x) or log(y) using draw ly ) / draw ll select x,y from tab  (For log(x)/log(y))
 - draw l2 select x,y from tab / l2x, l2y, l2l, l2s
 - draw b for bar darw, all arg like draw l; etc draw bs / draw b2 / draw b2x ...
 - draw h select col1 from tab1 / hx: x-log hist / hy: y-log hist  /  hl : x-y log hist
 - draw v select col1 from tab1  draw the violin box distribution
 - draw s select y from table / draw s select x,y from table / draw s select x,y,size from table / draw s select x,y,size,color from table
 - Mulit-Draw: draw v select col1 from tab1; draw l select a,b,c from tab2; ...
 @ html filename / chtml  (save output to a html file / close html file)
 @ webserver ip:port / @page url / webinput url name(5) age(3) _type(321) ~Search / _#n_ 
 @ jobserver / @job / @mail For Job server support;
 @ server running on background: Qsqlite scrp.txt >>out.log &  or  nohup Qsqlite scrp.txt &
 @ select command format
 - select * from table1 limit 1000,10 (start,cnt) 
 - select x,y,z from tab where a='123' >[index:_@0_  X=_@1_, Y=_@2_, Z=_@3_]
 - select * from tab >csv filename.csv 0/1 (export csv file with/without rowinfo)

# Ext function for SQLite:
 @@ regexp('^[1]([3-9])[0-9]{9}$',mobil)
 @@ regfind('1(.*?)2','1hello2 1good2',1) -> hello
 @@ regfn(',','1,2,3,4,5,6') -> 5 (5 match re)
 @@ regsub('([\d]{3})','#\\1#','Test000-372')  -> Test#000#-#372#
 @@ destr('123,456,34,456,1',',') -> '123,456,34,1'
 @@ select mID,csum(mName),count(*) from T group by mID
 @@ csum function; select mID,csum(userID),csum(mName) from t group by mID   or select csum('apple',1,2,3,4,5)
 @@ std function; select std(mM) from T    or   select std(1,2,3,4,5)
 @@ median function; select median(mM) from t   or   select median(1,3,2,5,4)
 @@ summary function; select type,summary(m) from t group by type   or   select summary(3,-2,9,4,6,3) will return combined descriptive statistics string. etc: cnt=6; max=9.0; min=-2.0; avg=3.8; med=3.5; std=3.35; his=[1,0,0,0,0,0,0,2,1,0,0,1,0,0,0,1]
 @@ idcheck(id,f=0/1/2) 0-15/18;1-18;2-15 / idchecksum / idconv  (check CHINA IDCard 15/18; gen checksum; conv 15->18)
 @@ power(2,2) -> 2^2 / power(2,1.0/2) -> sqrt(2)
 @@ slist('1,2,3,4,5',2) -> 3 / slist('1,2,3,4,5',7) -> 5 (if n>len,then return last item)
 @@ ctop('1 2 3 4 5',' ',3) -> 1 2 3  (ctop(x,y,z) split string x using y,and return top z item)
 @@ cindex(col) select uid, cindex(pid) as cnt, a from T group by uid where cnt<3*2
 @@ navg(row,n)  N row moving average calculation
 @@ rdelta(column name)  inter-row difference calculation
 
# Sqlite Tips:
 - select distinct * from Table order by random() limit 2 offset 1000 (or limit s,n ==> limit n offset s)
 - select date,code1,code2 from T1 left outer join (select date as d1 from T1 where xxx) on date=d1 left outer join (select d3,code2 from T2 where xxx) on date=d3
 - select id,name,addr from T1 union select id,uname,'---' from T2  (union or union all)
 - create table if not exists Roominfo2 (mID text PRIMARY KEY,mName real,mOrg int,PRIMARY KEY(ID ASC)) * can add without rowid 
 - SQlite data type: text, integer, real, blob
 - delete from table where a > 123 / drop table tb001
 - create [unique] index inx1 on table1 (ctime,[name...])  / drop index inx1
 - update A set last = (select t from B where A.time = B.time) where A.code > 30
 - create index u_name on tab1 (col1,...) / drop index u_name
 - strftime("%s",mETime) Convert string to seconds / strftime('%Y-%m-%d %H:%M:%S','now','localtime') / 'start of month' /'-7 days', 'weekday 5'  %W - week of year(1-54) %w-week(0-6) %j-(1-365)
 - Sqlite String add using : 'a' || 'b' ; select 'a' || x'0d' || x'0a' || 'apple'
 - cast(x as int) or cast(7/2.0 as int) or x+0 or x+0.0 / substr(str,begin,len)
 - select rowid, * from c (select system rowid); select last_insert_rowid()
 - with recursive xx(x) as (select 1 union select x+1 from xx where x<(select max(regfn(',',fn)) from tb1)) select id,regfind('(.+?)(?:,|$)',fn,x) as s from tb1, xx where s != '')  --> let a fn col like 'fun1,fun2,fun3,fun4' to row: fun1 / fun2 / fun3 / fun4 4 rows. (col to rows)
 - SQlite system function: count, max, min, avg, sum, substr, random, abs, upper, lower, length, trim, ltrim, rtrim, replace('apple','app','*'), typeof, hex, like('%12%',name) or like('23_33',tel) or like('100\%F%', name, '\'), iif(c,x,y), coalesce(t1,t2,t3...), hex(randomblob(16)), printf('%08d is %.2fs on %-10s %,d', 34123, 3123.334, 'apple',12345) ... 
 - Convert 1/22/20 date string to Sqlite format 2020-01-22 using: date(printf('20%d-%02d-%02d', regfind('(\d+?)(?:/|$)',d,3), regfind('(\d+?)(?:/|$)',d,1), regfind('(\d+?)(?:/|$)',d,2)))
 - Explain to see the SQLite execution policy: explain select ID from Room where m > 15
 - loadcsv xxx.gtf gene , And then: select regfind('gene_id "(.+?)";',attributes,1) as id, regfind('gene_name "(.+?)";',attributes,1) as gene, regfind('gene_type "(.+?)";',attributes,1) as type from gene
 - select data to new table: create table newtb as select name, count(*) as cnt from s group by name
 - VACUUM : optimize the database file (small size) / pragma table_info(tb1)  will list all tb1 cols info.
'''

import os, sys, math, re, time, base64, csv, gzip, zipfile
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote
from io import BytesIO, StringIO, TextIOWrapper

# for Linux/MacOS input() can get history by arrow key
try:
  import readline
except:
  pass

#
# 全局变量初始化
#
db, his_cmd, exec_flag = '', [], []
# 调试/时间信息输出标志、循环LOOP标志、循环命令缓存、MySQL服务器参数字典、数据库连接字典
dinfo_flag, loop_flag, loop_cnt, sql_block, loop_cmd, mysql_srv, srv_conn  = 0, 0, 0, '', [], {}, {}
# Sqlite 扩展函数用到的全局变量
sqlext_v, sqlext_s, navg_sum, navg_n, rdelta_tmp = 0, '', [], 0, None
# html 输出文件句柄, 是否有<ul>标志
f_html, ul, ul1 = None, 0, 0
# Web服务器执行命令缓存
wcmd = {}

#
# Sqlite 扩展函数全局变量复位函数
#
def Sqlite_ext_reset():
  global sqlext_v, sqlext_s, navg_sum, navg_n, rdelta_tmp
  # 这些全局变量在每次函数执行后，需要进行复位
  sqlext_v, sqlext_s, navg_sum, navg_n, rdelta_tmp = 0, '', [], 0, None

#
# Web 服务器
#
class Websrv(BaseHTTPRequestHandler):
  # 处理 http 请求
  def do_GET(self):
    # 为 Web 服务器建立 内存IO 输出缓冲
    global f_html
    f_html = StringIO()
    # web 路径、参数解析
    qPath = urlparse(self.path)
    fPath, query = qPath.path[1:], unquote(qPath.query)
    # 对于根目录，则用 / 表示
    if not fPath: fPath = '/'
    # 输出调试信息
    if dinfo_flag: print('>>> ',fPath, '?= ',query)
    # 根据 URL 匹配相对应的服务
    if wcmd and fPath in wcmd.keys():
      tmp = query.split(' ')
      # 对可能是 Form 传入的参数进行识别，如果能分割，且上面 split 没有切割，则用这个替代
      tmp2 = re.findall('\d=([^&]*)',query)
      if tmp2 and len(tmp) == 1: tmp = tmp2
      # 循环执行该页面对应的指令集
      for c in wcmd[fPath]:
        # 进行替换操作，用参数替换对应的 _#x_
        for j, d in enumerate(tmp):
          # 对于 _#x_ 替换为对应结果
          c = c.replace('_#'+str(j+1)+'_',str(d))
        #
        # 处理特殊的 Web input 指令 ( webinput url 姓名(10)(默认内容) 电话(15)(默认内容) >提交 )
        #
        url = re.findall('webinput (.+?) (.*)(\~|\^)(.+?)($| )', c)
        # 首先获取 URL, 如果存在则继续处理 后续输入框
        if url:
          ibox = re.findall('(.+?)\((.*?)\)\((.*?)\)', url[0][1])
          html_i, html_br, html_c = '', '', 0
          # submit 按钮前面的 > 表示横向排列， ^ 表示竖向排列，需要换行
          if url[0][2] == '^': html_br = '<br>'
          for i in ibox:
            html_c += 1
            # 如果输入的第一个字符是 _，表示这是一个隐藏信息，后面跟的是具体内容
            if i[0].strip()[:1] == '_':
              html_i += '<input type="hidden" name="%d" value="%s">'%(html_c, i[2])
            else:
              # 构造 html input 内容 （如果没有设置宽度，则设置默认10）
              html_i += '%s : <input type="text" name="%d" size=%s value="%s">%s'%(i[0], html_c, (int(i[1]) if i[1].isdigit() else 10), i[2], html_br)
          # 结果输出
          html_f = '<form action="%s">%s<input type ="submit" value="%s"></form>'%(url[0][0], html_i, url[0][3])
          # 如果 webinput 属于 select 输出子句描述，则特殊处理
          if re.findall('select .+? (webinput .+ [\~\^].+?)[ \]]', c):
            # 替换后执行
            proc_cmd(re.sub('webinput .+ [\~\^].+?[ \]]', html_f, c))
          else:
            # 如果 webinput 是单独一句，则直接输出
            oprint(html_f)
        else:
          # 执行指令
          proc_cmd(c)
      # 完成指令集合后，输出给浏览器
      self.webout(f_html)
    # 如果不存在 / 根目录的配置，则输出默认 功能 url 列表
    elif fPath == '/':
      oprint('# 可以使用以下 url 访问')
      for i in wcmd.keys():
        oprint('- /' + i + '?arg1&arg2...<br>')
      self.webout(f_html)
    else:
      self.send_error(404,'URL Error!')

  # 将内容输出给浏览器
  def webout(self, f_html):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('<head><meta charset="utf-8"></head><body style="">'.encode())
    f_html.seek(0)
    self.wfile.write(f_html.read().encode())
    self.wfile.write('</body>'.encode())

  # 禁止调试信息输出
  def log_message(self, format, *args):
    return

#
# 发送邮件函数
#  发件人地址、发件人密码、smtp服务器地址、端口号、收件人地址列表、邮件标题、邮件内容
#  发送成功返回 1
#
def SendMail(from_addr,password,msrv,to_addr,msgtitle,msgcontent):
  from email import encoders
  from email.header import Header
  from email.mime.text import MIMEText
  from email.utils import parseaddr,formataddr
  import smtplib, ssl
    
  # 解析 邮件服务器 地址:端口
  smtp_server, port = msrv.split(':')
  try:
    # 构建 邮件内容
    msg = MIMEText(msgcontent, 'html','utf-8')
    msg['From'] = from_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = Header(msgtitle,'utf-8').encode()
    #发送邮件
    server = smtplib.SMTP(smtp_server,port)		# SMTP协议默认端口是25
    context1 = ssl.create_default_context()		# 创建一个用于加密信道使用的 上下文 对象
    if server.starttls(context = context1)[0] == 220:		#判断返回码，如果是220表示成功连接
      server.login(from_addr,password)		#登陆SMTP服务器
      # 发送邮件（可发多人 to_addr 为 list，邮件正文是str, as_string()把MIMEText对象变成str)
      server.sendmail(from_addr, to_addr, msg.as_string())
      server.quit()
      return 1	# 发送成功返回
  except:
    pass
  # 发送失败，返回结果
  return 0

#
# Get table cols info, using for loop
#
def getTableCols( tbname ):
  res = []
  if db and tbname:
    # Connect SQLite
    cx,cxt = dbconn(db)
    cu = cx.cursor()
    Sqlite_ext_reset()
    # Get table cols info
    cu.execute('pragma table_info(%s)'%tbname)
    res = cu.fetchall()
  # return
  return res

#
# loadweb: load url from web, and get re item.
#
def loadweb( cmdstr ):
  res = []
  # 解析参数
  arg = re.findall('url=(.+?) re=(.+?)(?:$| ext=(.+?)$)', cmdstr, re.IGNORECASE)
  if arg:
    url, rearg, extv = arg[0]
    # 将 附加参数 分割 , 转成 tuple 类型(便于后续叠加)
    extv = tuple( extv.split(',') )
    try:
      import requests
    except ModuleNotFoundError:
      print('# Please using pip3 install requests module.')
      return res
    # 通过 request 获取 web 内容
    try:
      r = requests.get(url, timeout = 60)
      if r.status_code == 200:
        info = r.text
      else:
        info = ''
    except:
      info = ''
    # 解析内容
    ret = re.findall(rearg, info)
    # 获取结果
    for i in ret:
      # 将参数 和 扩展参数叠加
      res.append(i + extv)
  else:
    print('loadweb arg error, please using loadweb url=https://xxx.xxx re=href="(.+)"> ext=_^1_, fun')
    return res 
  # 返回结果
  return res

#
# Download file from web
#
def downloadfile(url, filename):
  # 判断文件是否已经存在
  if os.path.isfile(filename):
    print('# File [%s] already exists.'%filename)
    return 0
  else:
    try:
      import requests
    except ModuleNotFoundError:
      print('# Please using pip3 install requests module.')
      return -1
    # 下载文件 (批量写入文件)
    try:
      r = requests.get(url, stream=True)
      with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8096):
          if chunk:
            f.write(chunk)
    except:
      print('# Download file error. please check network, url or filename!')
      return -2
    # 下载完成返回
    print('# Download file [%s] completed.'%filename)
    return 0

#
# Job Server
#
def JobServer(jcmd):
  # 导入文件操作的库 和 全局变量
  import shutil
  global f_html
  # 构建初始 执行标志 (每一个任务 执行的周n ，初始化为-1)
  r_flag = [-1 for i in range(len(jcmd))]

  # 启动循环
  while 1:
    # 获取当前时间，当前周数（周n, 周日为 0 )
    ct = time.strftime('%H:%M', time.localtime())
    cw = int( time.strftime('%w', time.localtime()) )
    cd = time.strftime('%Y-%m-%d' , time.localtime())

    for cnt, i in enumerate(jcmd):
      w, t = i[0]['weeks'], i[0]['time']
      # 确认 当前日期没有执行过 & 时间到了
      # 这样复杂的逻辑，主要是用于解决一些操作可能时间很长，导致 用时间相等 判断错过
      # 这里用 r_flag 列表作为执行标志，执行过后，则+1，这样就只有明天才会触发，因此可以用 ct >= t 来做时间判断
      # 否则 ct >= t 会导致重复执行；如果用 ct = t，则可能因为上一个指令执行超时，导致错过执行
      if (cw == r_flag[cnt] or r_flag[cnt] == -1) and ct >= t:
        # 当前 日期 需要执行
        if str(cw) in w:
          # 设定执行标志为下一天 (如果是6，累加1后，变为0，因为星期天为0)
          r_flag[cnt] = (0 if cw == 6 else cw + 1)
          # 开始执行序列
          # 为 Job 服务器建立 内存IO 输出缓冲
          f_html = StringIO()
          for c in i[1]:
            # 执行指令
            proc_cmd(c)
          # 执行指令后，根据类型输出文件或邮件
          if i[0]['type'] == 0:
            if dinfo_flag: print('Out File:',i[0]['file'].replace('_@Date_',cd).replace('_@Time_',ct) )
            # 输出到文件
            with open(i[0]['file'].replace('_@Date_',cd).replace('_@Time_',ct), 'w') as fd:
              f_html.seek(0)
              shutil.copyfileobj(f_html, fd)
          else:
            # 输出到邮件
            f_html.seek(0)
            r = SendMail( i[0]['user'], i[0]['pwd'], i[0]['msrv'], i[0]['addr'], i[0]['mtitle'].replace('_@Date_',cd).replace('_@Time_',ct), f_html.getvalue() )
            if r:
              if dinfo_flag: print('Email Sent')
            else:
              if dinfo_flag: print('Email Send Error!')
        else:
          # 就算当日不需要执行，也需要每天设定执行标志为下一天 (如果是6，累加1后，变为0，因为星期天为0)
          r_flag[cnt] = (0 if cw == 6 else cw + 1)
    # 延时
    time.sleep(10)

#
# 解析 Web page (在发现 webserver 关键字，并且解析出后面的 ip，端口号后)
#
def parsingWeb(cmd):
  # 找寻
  cmds = cmd.splitlines()  # split \n\r not only split('\n')
  cblock = False			# 采用 ''' 块注释标记
  wFlag = False				# 解析 web 标志
  pFlag = ''					# 解析 @page 后的路径 
  ocmd = {}						# 用于存放每一个 不同@page 的指令集 
  wip, wport = '', 8000		# 默认的 IP，端口
  try:
    for i in cmds:
      i = i.strip()
      if i:
        # 如果出现块注释，则取反注释标记(配对出现)
        if i[:3] == "'''":
          cblock = not cblock
          continue
        # 如果不属于块注释范围，则解释命令；否则跳过
        if not cblock:
          if i[0] != '#' and i[0] !='-':
            # 如果属于 webserver 功能，则开始解析 @page 内容
            # @page homepage 3  (表示如果 web 地址为 homepage?1234&apple&good)
            if wFlag:
              if i[:6] == '@page ':
                pFlag = i[6:].split(' ')[0]
                ocmd[pFlag] = []
              # 如果已经发现 @page，则将所有 后续指令 记录到对应字典的数组内
              elif pFlag:
                ocmd[pFlag].append(i)
              else:
                # 对于在 @webserver	后，第一个 @page 前的指令，进行执行，作为初始化操作
                proc_cmd(i)
            elif i[:10] == '@webserver':
              # 获取后续的 参数 ip:port
              t = i[10:].split(':')
              if len(t)==2 and t[1].isdigit():
                wip, wport = t[0].strip(), int(t[1])
              # 设置 解析标志
              wFlag = True
  except:
    pass
  # 返回 web 页面/指令集 字典
  return wip, wport, ocmd

#
# 解析 Job Server page (在发现 jobserver 关键字，并且解析出文件后面的具体任务序列)
#
def parsingJob(cmd):
  # 找寻
  cmds = cmd.splitlines()  # split \n\r not only split('\n')
  cblock = False			# 采用 ''' 块注释标记
  jFlag = False				# 解析 jobserver 标志
  pFlag = ''					# 解析 @page 后的路径 
  # 用于存放每一个 @job 或 @mail 的指令集 
  # [{'type':类型(0-job,1-mail),'weeks':'1234567','time':'03:30','msrv':'mail.office360.com:469','user':'abc@outlook.com','pwd':'123456','mtitle':'邮件的标题 _@Data_','addr':'m1@email.com m2@email.com'},[指令序列], [...] }]
  ocmd = []					
  try:
    for i in cmds:
      i = i.strip()
      if i:
        # 如果出现块注释，则取反注释标记(配对出现)
        if i[:3] == "'''":
          cblock = not cblock
          continue
        # 如果不属于块注释范围，则解释命令；否则跳过
        if not cblock:
          if i[0] != '#' and i[0] !='-':
            # 如属于 jobserver 功能，则开始解析 @job 或 @mail 内容
            if jFlag:
              if i[:5] == '@job ':
                # 用正则提取 @job 后面的参数 [周] [时间] [输出文件名] 
                arg = re.findall('\[(\d+?)\] \[(\d+:\d+)\] \[(.+?)\]', i[5:])
                if arg:
                  ocmd.append( [{'type':0,'weeks':arg[0][0],'time':arg[0][1],'file':arg[0][2]}, [] ] )
                  pFlag = True
                else:
                  pFlag = False 
              elif i[:6] == '@mail ':
                # 用正则提取 @mail 后面的参数 [周] [时间] [邮件服务器信息] [标题] [收件人] 
                arg = re.findall('\[(\d+?)\] \[(\d+:\d+)\] \[(.+?:\d+)\] \[(.+?)\] \[(.+?)\] \[(.+?)\] \[(.+?)\]',i[6:])
                if arg:
                  ocmd.append( [{'type':1,'weeks':arg[0][0],'time':arg[0][1],'msrv':arg[0][2],'user':arg[0][3],'pwd':arg[0][4],'mtitle':arg[0][5],'addr':arg[0][6].split(' ')}, [] ] )
                  pFlag = True
                else:
                  pFlag = False 
              # 如果已经发现 @page，则将所有 后续指令 记录到对应字典的数组内
              elif pFlag:
                # 往最后一个记录的命令序列插入指令
                ocmd[-1][1].append(i)
              else:
                # 如果在 @jobserver后面， @job 或 @mail 前面出现指令，则执行，作为初始化指令
                proc_cmd(i)
            elif i[:10] == '@jobserver':
              # 设置 解析标志, 并且初始化 命令序列 存储
              jFlag = True
  except:
    pass
  # 返回 web 页面/指令集 字典
  return ocmd

#
# 将字符串内的\n和空格去掉，合并成一行（用于处理SQLite的创建字串)
#
def format_t1(cmd):
  return''.join([i.strip() for i in cmd.split('\n')])

#
# 为SQLite提供正则支持函数
# 通过 cx.create_function('regexp', 2, regexp) 来添加
# 使用：select * from tab1 where regexp('^[1]([3-9])[0-9]{9}$',mobile) = true
#
def regexp(pattern, input):
  return bool(re.match(pattern, input))

#
# 正则替换函数 
#  参数：正则、替换串、输入串
#
def regsub(pattern, r, input):
  return re.sub(pattern, r, input)

#
# 返回正则表达式匹配的结果(默认是第一个匹配项，可以在最后一个参数n指定)
# 使用：select regfind('1(.*?)2','1hello2 1good2',1)    n=0 返回所有 hello good  n=1，返回hello，n=2返回good
#
def regfind(pattern, input, n):
  r = re.findall(pattern, input)
  if n>0 and len(r) >= n:
    ret = r[n-1]
    # 如果内部包含多个结果集，这需要进行处理
    if type(ret) == tuple:
      return ' '.join(ret)
    else:
      return ret
  elif n == 0:
    # 如果内部包含多个结果集，这进行处理，例如：[(1,2,3),(3,5,7)]
    if len(r)>0 and type(r[0]) == tuple:
      ret = []
      for i in r:
        ret.append(' '.join(i))
      return ' '.join(ret)
    else:
      return ' '.join(r)
  else:
    return ''

#
# 通过指定序号，索引列表内容
#   参数：以逗号分割的列表内容字符串；索引id
#     例如: slist('0,1,2,3,4,5',3) -> 3；如果 id>列表长度，则返回列表最末尾元素
#
def slist(liststr,n):
  s = liststr.split(',')
  sl, n = len(s), int(n)
  if n < 0:
    return s[n] if n >= -1 * sl else s[0]
  else:
    return s[n] if n < sl else s[-1]
#
# 字符串分割、去重功能 ： 将送进来的字符串分割，而后去重，最后再拼接回去, 最后一个参数是 分割符
# 使用 select destr('123456 345 789 345',' ') 返回： 123456 345 789
#
def destr(input,sstr):
  # 分割字符串，并且过滤掉没有意义的空字符；同时对两端的空格也过滤掉
  l = [i.strip() for i in filter(None,input.split(sstr))]
  # 利用转换为set集合去重，而后用 sorted 按照原来序列重排
  return sstr.join(sorted(set(l),key=l.index)).strip()

#
# 为一个字段提供行自增计数器，即当该行的值和上一行没有变化，每次调用返回值+1，直到值变化，则从1再开始计算
#
def cindex(input):
  global sqlext_v, sqlext_s
  s = str(input)
  # 如果 值发生变化, 则清零; 否则递增计数器
  if sqlext_s != s:
    sqlext_v, sqlext_s = 1, s
  else:
    sqlext_v += 1
  return sqlext_v

#
# 计算两行之间的差值 (Row n+1 - Row n)
#
def rdelta(input):
  global rdelta_tmp
  # 如果有预存值，则计算差值返回; 否则返回 None
  if rdelta_tmp:
    retval = input - rdelta_tmp
  else:
    retval = None
  # 将当前值保存到临时变量
  rdelta_tmp = input
  # 返回结果
  return retval

#
# 移动平均值计算函数 (输入数据序列-数字类型, n-表示累计多少行后开始计算平均值,例如7天均值)
#
def navg(input, n):
  global navg_sum, navg_n
  # 累加值 和 统计次数
  navg_sum.append(input)
  # 判断是否符合计算要求, 如果符合要求，计算均值，重设两个累加变量; 否则返回空值(因为还无法计算)
  if navg_n == n-1:
    retval = sum(navg_sum) / n
    # 将最前面一个值弹出
    navg_sum.pop(0)
  else:
    navg_n += 1
    retval = None
  # 返回结果
  return retval

#
# 身份证校验函数 （输入身份证前17位,返回最后一位)；
#
def IDChecksum(idinfo):
  # 通过正则表达式来对输入数据进行判断，确保全部为数字 & 长度位17
  if re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d$',idinfo):
    # 根据规则，定义转换变量
    cCardCV=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    cCardXV='10X98765432'
    iTotal = 0;		# 存储累加和
    iCount = 0;     # 存储执行指针
    # 按照规则，对不同位数的值乘以系数，而后累加
    for i in idinfo:
      iTotal += int(i)*cCardCV[iCount]
      iCount +=1
    # 按照规则，除以11，取余后查表得到校验值
    return cCardXV[iTotal%11]
  else:
    return ''

#
# 判断身份证是否有效函数
# 参数 f=0 新旧身份证都算 f=1 只有新身份证有效 f=2 只有旧身份证有效
#
def IDCheck(idinfo,f):
  # 新身份证 或 新旧都算
  if f <= 1 and len(idinfo) == 18:
    if re.match('^[1-6]\d{5}(18|19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',idinfo):
      return idinfo[-1:].upper() == IDChecksum(idinfo[:-1])
    else:
      return False
  elif f != 1:	#如果并非只检测新身份证，则检测旧身份证
    return bool(re.match('^[1-6]\d{7}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}$',idinfo))
  else:
    return False

#
# 对旧身份证信息进行自动转换 (如果无法转换，则返回原值)
#
def IDConv(idinfo):
  if re.match('[1-6]\d{7}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}$',idinfo):
    n = idinfo[:6] + '19' + idinfo[6:]
    return n + IDChecksum(n)
  else:
    return idinfo

#
# 为SQLite提供新的排序方法
# 如果第一个的顺序低于第二个，则返回-1，如果顺序相等，则返回0; 如果第一个的顺序高于第二个，则返回1
# 通过 cx.create_collation("reverse", collate_reverse) 来添加
# 使用： select x from test order by x collate reverse
#
# def collate_reverse(string1, string2):
# 	return -cmp(string1, string2)

# 添加新的数据类型转换、映射
# sqlite3.register_adapter(stext, adapt_stext)
# sqlite3.register_converter('text', convert_stext)


#
# 为SQlite 提供扩展统计函数 (类似count/sum/max/min/avg)
#	通过：cx.create_aggregate("csum", 1, StrSum) 来添加
# 使用： select csum(total) from tb1
#
# csum: 字符串累加功能
class StrSum:
  def __init__(self):
    self.count = []

    # 每一行数据会调用这里
  def step(self, *value):
    self.count.append(' '.join([str(i) for i in value]))

    # 最后返回结果 
  def finalize(self):
    return ' '.join(self.count)

# std: 标准差计算函数
class Cstd:
  def __init__(self):
    self.count = []

    # 每一行数据会调用这里
  def step(self, *value):
    for i in value:
      try:
        self.count.append(float(i))
      except:
        pass

    # 最后返回结果
  def finalize(self):
    # 计算均值
    m = sum(self.count)/len(self.count)
    # 计算方差
    z = [(m-i)**2 for i in self.count]
    # 汇总方差，而后开平方得到标准差
    return ( sum(z)/len(z) ) ** 0.5

# median: 中位数计算函数
class median:
  def __init__(self):
    self.count = []

  # 每一行数据会调用这里(数据进行转换)
  def step(self, *value):
    for i in value:
      try:
        self.count.append(float(i))
      except:
        pass

    # 最后返回结果
  def finalize(self):
    # 根据数据数量获取中间位置(p1,p2)
    s = len(self.count)
    if s > 0:
      # 如果是偶数, 则获取中间两个的值, 而后计算平均值, 例如 [2,3,4,5] 应该计算 (3+4)/2
      if s % 2 == 0:
        p1 = s/2 - 1
        p2 = p1 + 2
      # 如果是奇数, 获取中间值, 例如 [2,3,4] -> 3
      else:
        p1 = (s-1) / 2
        p2 = p1 + 1
      # 对数据进行排序, 而后获取
      self.count.sort()
      v = self.count[int(p1) : int(p2)]
      # 计算中位数 (对于偶数个数需要计算两个数的均值)
      return sum(v) / len(v)
    else:
      return None

# summary: 返回一个综合的 统计描述 摘要字符串, 包含系列统计信息
# count; max; min; avg; median; [直方图]
class summary:
  def __init__(self):
    self.count = []

  # 每一行数据会调用这里(数据进行转换)
  def step(self, *value):
    for i in value:
      try:
        self.count.append(float(i))
      except:
        pass

    # 最后返回结果
  def finalize(self):
    # 设置直方图数量
    hn = 16
    # 根据数据数量获取中间位置(p1,p2)
    s = len(self.count)
    if s > 0:
      # 如果是偶数, 则获取中间两个的值, 而后计算平均值, 例如 [2,3,4,5] 应该计算 (3+4)/2
      if s % 2 == 0:
        p1 = s/2 - 1
        p2 = p1 + 2
      # 如果是奇数, 获取中间值, 例如 [2,3,4] -> 3
      else:
        p1 = (s-1) / 2
        p2 = p1 + 1
      # 对数据进行排序, 而后获取
      self.count.sort()
      v = self.count[int(p1) : int(p2)]
      # 计算中位数 (对于偶数个数需要计算两个数的均值)
      med = sum(v) / len(v)
      # 计算 max, min
      max, min = self.count[-1], self.count[0]
      # 计算均值
      avg = sum(self.count) / s
      # 计算方差
      z = [(avg-i)**2 for i in self.count]
      # 汇总方差，而后开平方得到 标准方差 (这里计算的是总体标准差)
      # 如果要计算样本标准差: std = ( sum(z)/(s-1 if s > 1 else s) ) ** 0.5
      std = ( sum(z)/ s ) ** 0.5
      # 计算 直方图 (把数据根据 最大-最小 值均分为 hn 段, 而后看看大致落在哪段的数量)
      d = (max - min) / (hn - 1)
      o = [0 for i in range(hn)]
      # 避免 d=0 引发错误
      if d > 0:
        for i in self.count:
          o[ round( (i - min) / d ) ] += 1
      else:
        o[0] = s
      his = ','.join([str(i) for i in o])
      # 返回结果集
      return 'cnt=%d; max=%s; min=%s; avg=%s; med=%s; std=%s; his=[%s]'%(s, max, min, round(avg,3), round(med,3), round(std,3), his)
    else:
      return ''


#
# 根据f_html文件句柄，确定文件输出/屏幕输出 (对于输出到文件，提供简单Markdown转换html功能)
#
def oprint(*arg):
  global f_html, ul, ul1
  if f_html:
    # 因为集合无法修改，因此转成列表,并且字符串化，且将空格替换&nbsp; (但是避免转换<html标记>...<html>之间内容)
    #arg = [str(i) if re.match('<.+>.+<.+>',str(i)) else str(i).replace(' ','&nbsp;') for i in arg]
    arg = [str(i) for i in arg]
    # 反序匹配（从######开始）, 对 Markdown # 转换为 <h1></h1>; ## -> <h2></h2> ...
    for i in range(6,0,-1):
      cs = '#' * i
      if arg[0][:i] == cs:			# [:i] 就算 arg[0]为空，也能返回空值，不会出错
        arg[0] = '<h%d>'%(i) + arg[0].replace(cs,'')
        arg += ['</h%d>'%(i)]
        # 如果是第二级标题，则加上下划线
        if i==2: arg += ['<hr>']
        break
    # 匹配 -/* 开头内容 为<li> </li>
    if arg[0][:1] == '-' or arg[0][:1] == '*':		# [:1] 就算 arg[0]为空，也能返回空值，不会出错，因此不用arg[0][0]
      if not ul:
        f_html.write('<ul>\n')
        ul = 1
      if ul1:		# 如果存在下一级，则需要关闭
        f_html.write('</ul>\n')
        ul1 = 0
      arg[0] = '<li>' + ('<b>*</b>' if arg[0][0] == '*' else '') + arg[0][1:]
      arg[-1] += '</li>\n'
    # 匹配 空格-/空格* 下一级列表处理(必须要有上一级ul才处理)
    elif arg[0][0:2] == ' -' or arg[0][0:2] == ' *':
      if ul:
        if not ul1:
          f_html.write('<ul type="square">\n')
          ul1 = 1
        arg[0] = '<li>' + ('<b>*</b>' if arg[0][0:2] == ' *' else '') + arg[0][2:]
        arg[-1] += '</li>\n'
    else:
      if ul:
        ul = 0
        arg[0] = '</ul>\n' + arg[0]
      if ul1:
        ul1 = 0
        arg[0] = '</ul>\n' + arg[0]
    # 匹配 **info** 黑体标记
    arg[0] = re.sub('\*\*(.+?)\*\*','<b>\g<1></b>',arg[0])
    # 判断最后是否 html 标记，如果不是，则添加 <br> 换行
    if not re.match('.*<.*>$',arg[-1]): arg = arg + ['<br>']
    # 输出到文件
    f_html.write(''.join(arg))
  else:
    print(*arg)

#
#	根据f_html文件句柄，确定保存图片/屏幕输出
#		matplotlib: plt.xlim/ylim(0,2) 用于指定x,y坐标轴取值范围
#
def oplt_show(plt,fig):
  global f_html
  if f_html:
    # 构建内存文件句柄，而后保存图形文件到内存，用base64编码，而后内嵌到html页面
    buff = BytesIO()
    # top=0.99 指上面图形可以去到99%；bottom 0.1表示留下10%空间显示标签；left也是显示标签；right可以用尽
    # 如果标签位置不够，可以适当调整 left,bottom
    plt.subplots_adjust(left=0.1, right=0.99, top=0.95, bottom=0.1)
    plt.tight_layout()		# 自动优化布局，使得标注不会超出范围
    plt.savefig(buff)		
    f_html.write('<img src="data:image/png;base64,%s" /><br>' % (base64.b64encode(buff.getvalue()).decode()) )
  else:
    plt.subplots_adjust(left=0.1, right=0.99, top=0.95, bottom=0.1)
    plt.tight_layout()		# 自动优化布局，使得标注不会超出范围
    plt.show()
  # 释放资源
  plt.close(fig)

# 将 sqlite 返回结果转换为和 MySQL 一样的 字典类型 
def dict_factory(cursor, row):
  return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))


# 检查数据库是否 MySQL
def check_mysql(dbname):
  return re.findall('#(.+?)#',dbname)

#
# 数据库连接建立 (如果是内存数据库，则共用，并且不关闭 connect)
# 	! 非内存数据库每次用完关闭，是希望不锁定文件，避免影响其它程序（例如写入同一数据库）
#		参数： 数据库名；返回：数据库连接是否需要关闭 (0-不需要，1-需要)
#
def dbconn(dbname):
  global srv_conn, mysql_srv		# memory_cx
  SQLite_opt = 0		# SQLite扩展执行标志
  # 如果连接已经创建，则直接使用
  cx = srv_conn.get(dbname)
  if cx:
    cxt = 0		# 设置不需要关闭连接标志
  else:
    cxt = 1		# 默认设置需要关闭连接标志
    my = check_mysql(dbname)
    # 创建一个内存数据库连接，作为临时数据库用途
    if dbname == ':memory:':
      cx, cxt = sqlite3.connect(':memory:'), 0
      srv_conn[dbname] = cx		# 对于不需要关闭连接的，将连接缓存到全局变量
      SQLite_opt = 1					# 设置扩展执行标志
    # 如果是 MySQL 数据库
    elif my:
      try:
        import pymysql
      except ModuleNotFoundError:
        print('# Please install pymysql, using: pip3 install pymysql')
      mysql = mysql_srv.get(my[0])
      if mysql:
        # 根据 MySQL 服务器参数，获取正确的端口号
        t_Mysrv = mysql[0].split(':')
        if len(t_Mysrv) == 2 and t_Mysrv[1].isdigit():
          myPort = int(t_Mysrv[1])
        else:
          myPort = 3306 	# 默认MySQL端口号
        # 如果需要返回结果集为字典类型，包含字段名，添加：cursorclass=pymysql.cursors.DictCursor
        cx, cxt = pymysql.connect(host=t_Mysrv[0],user=mysql[1],passwd=mysql[2],db=my[0],charset='utf8mb4',port=myPort), 0
        srv_conn[dbname] = cx		# 对于不需要关闭连接的，将连接缓存到全局变量
      else:
        print('!!! MySQL database not found, Please using mysql db srv user pwd setup')
    else:
      cx, cxt = sqlite3.connect(dbname), 1
      SQLite_opt = 1
    # 如果需要设置扩展(SQLite文件连接，第一次memory连接），则执行
    if SQLite_opt:
      # 设置自定义的row预处理，将 row 转换为字典类型，和 MySQL 一样
      # cx.row_factory = dict_factory
      # 设置连接参数
      cx.row_factory = sqlite3.Row
      # 为SQLite 添加扩展函数 
      # create_function参数：用户定义函数名, 函数接受的参数的个数, 对应的 Python 函数
      # create_function 可以创建同一个名字，但是参数个数不同的函数，例如： ('regabc',1,reg1)  ('regabc',2,reg2)
      # 参数个数-1表示接受任意参数： create_function('concat', -1, lambda x, y, sep=',' : "%s%s%s" % (x, sep, y))
      # 对于-1，可以这样接收参数：create_function('csv', -1, lambda *args : ','.join(map(repr, args)) )
      cx.create_function('regexp', 2, regexp)
      cx.create_function('regsub', 3, regsub)
      cx.create_function('regfind', 3, regfind)
      # 返回找到正则的数量，例如 regfn(',','1,2,3,4,5,6') 返回5，表示找到5个逗号
      cx.create_function('regfn', 2, lambda x,y : len(re.findall(x,y)))
      cx.create_function('destr', 2, destr)
      cx.create_function('idchecksum', 1, IDChecksum)
      cx.create_function('idcheck', 2, IDCheck)
      cx.create_function('idconv', 1, IDConv)
      cx.create_function('slist', 2, slist)
      cx.create_function('power', 2, lambda x,y : x ** y)
      # 对字符串截取 N 项 将字符串split，而后取最前面的 z 项返回
      cx.create_function('ctop', 3, lambda x,y,z : y.join([i for i in x.split(y)[:z]]) )
      # 对字符串进行累加操作，例如 sumc('1,2,3,4,5',',') -> 15.0
      # sum([float(i) if re.match('^[-+]?[0-9]*\.?[0-9]+$',i) else 0.0  for i in x.split(y)])) 速度慢4倍 放弃容错
      cx.create_function('sumc', 2, lambda x,y : sum([float(i) for i in x.split(y)]) )
      cx.create_function('cindex', 1, cindex )
      cx.create_function('navg', 2, navg )
      cx.create_function('rdelta', 1, rdelta )
      cx.create_aggregate('csum', -1, StrSum)
      cx.create_aggregate('std', -1, Cstd)
      cx.create_aggregate('median', -1, median)
      cx.create_aggregate('summary', -1, summary)
  # 返回连接串、连接类型
  return cx, cxt

#
# load csv file to new table
#		参数：数据库, csv文件名, 表名, ftype是否第一行过滤掉(1表示过滤掉), 是否 tsv 格式(\t分割的csv)
#
def loadCSV(dbname, fname, tname, ftype, tsv=0):
  # 默认用 utf-8 打开文件，如果出错，则改用默认方式
  wt = ['GBM','utf-8-sig']				# 默认尝试2次，一次用UTF-8解码，一次GBK; wt.pop(), 顺序反写
  bt = time.time()
  fname = fname.strip()
  # 根据文件名判断压缩文件类别 (z_type: 0-非压缩, 1-gzip, 2-zip)
  if fname[-3:].upper() == '.GZ':
    z_type = 1
    l_ext = fname[-7:-3].upper()
  elif fname[-4:].upper() == '.ZIP':
    z_type = 2
    l_ext = fname[-8:-4].upper()
  else:
    z_type = 0
    l_ext = fname[-4:].upper()
  # 根据文件名判断不同类别文件, 设定对应解析参数
  #    ftype: 是否需要过滤掉第一行;         tsv: 是否\t分割; 
  #    p_ext: 注释字符(etc: #/##/@ 等);   skip_n: 跳过前面 n 行; 
  if l_ext == '.TSV':
    tsv = 1
    p_ext, skip_n = '', 0
  elif l_ext == '.MAF':
    ftype, tsv = 1, 1
    p_ext, skip_n = '#', 0
  elif l_ext == '.VCF':
    ftype, tsv = 1, 1
    p_ext, skip_n = '##', 0
  elif l_ext == '.SAM':
    ftype, tsv = 0, 1
    p_ext, skip_n = '@', 0
  elif l_ext == '.GTF' or l_ext == '.GFF' or l_ext == '.GPD':
    ftype, tsv = 0, 1
    p_ext, skip_n = '#', 0
  elif l_ext == '.GCT':
    ftype, tsv = 1, 1
    p_ext, skip_n = '', 2    # .GCT 文件 第一行是版本号, 第二行是样本数量描述, 需要跳过
  else:
    p_ext, skip_n = '', 0
  # 计算 p_n (注释字符 p_ext 长度)
  p_n = len(p_ext)
  # 读取文件, 检查是否符合要求
  while wt:
    en_code = wt.pop()
    try:
      # 根据文件压缩类型, 使用不同的文件打开方式 (1-gzip, 2-zip, 0-normal)
      # utf-8-sig也能解析utf-8内容
      if z_type == 1:
        f = gzip.open(fname, 'rt', encoding = en_code)
      elif z_type == 2:
        gz_f = zipfile.ZipFile(fname, 'r')
        # 获取 ZIP 文件中的第一个文件, 并且通过 io.TextIOWrapper 方式来解码
        f = TextIOWrapper(gz_f.open(gz_f.namelist()[0], 'r'), encoding = en_code)
      else:
        f = open(fname, 'r', encoding = en_code, newline = '')	
      # 读取文件 (cnt - 列数, rsize - 行数, skip_r - 跳过前面 行数, i_note: maf/vcf 文件注释 )
      cnt, rsize, skip_r, i_note = 0, 0, skip_n, []
      # 用于跳过前面 n 行 的计数器
      skip_cnt = skip_n
      # 如果是 TSV 格式, 按照 \t 分割
      if tsv:
        r = csv.reader(f, delimiter='\t')
      else:
        r = csv.reader(f) #, delimiter=' ', quotechar='|')
      for t in r:
        # 如果需要跳过 n 行, 则跳过
        if skip_cnt > 0:
          skip_cnt -= 1
          continue
        # 如果有注释符, 则判断,跳过
        if p_n:
          # 如果是注释行
          if t[0][:p_n] == p_ext:
            # 如果是头部的注释行(因为有一些文件, 例如gff/gtf 会在中间使用注释行)
            if rsize == 0:
              i_note.append(t[0])
              skip_r += 1
            continue
        # 累加有效行计数器
        rsize += 1
        # check csv row cnt
        if cnt > 0:
          if cnt != len(t):
            print( '# CSV Problem (split item not %d): %s'%(cnt, t) )
            err = 1
            break
        else:
          cnt = len(t)
          # 如果第一行为表头, 则在这里进行获取
          if ftype == 1:
            info = t
            # 对于 vcf 文件, 需要过滤掉表头前的 # 符号 (#name	code)
            if l_ext == '.VCF': info[0] = info[0][1:]
      # 读取完成，表示不需要再尝试，直接退出
      err = 0
      break
    except UnicodeDecodeError:
      print('@ UTF-8 Encoding Error, Try Using GBK.')
      err = 1
      continue
    except:
      err = 2
      break 
  # 将 csv 数据插入
  if err == 0 and rsize > 0:
    # 如果第一行是表头, 则 记录数-1 
    if ftype == 1: rsize -= 1
    # 对于 maf/vcf 类型文件, 显示注释信息
    if i_note: print('\n' + '\n'.join(i_note) + '\n')
    # 显示检查结果
    print('@ %s check ok, total %d records, write to [ %s ]...'%(fname, rsize, tname))
    # Connect SQLite
    cx, cxt = dbconn(dbname)
    cu = cx.cursor()
    # 如果 CSV 第一行 为标题，则使用其作为 表字段, 否则使用 r1/r2... 顺序名
    if ftype == 1:
      row  = ','.join(['"'+info[i]+'" text' for i in range(cnt)])
    else:
      if l_ext == '.GTF' or l_ext == '.GFF':
        row = 'seqid text, source text, type text, start text, end text, score text, strand text, phase text, attributes text'
      elif l_ext == '.SAM':
        row = 'QNAME text, FLAG text, RNAME text, POS text, MAQ text, CIGAR text, MRNM text, MPOS text, ISIZE integer, SEQ text, QUAL text'
      elif l_ext == '.GPD':
        row = 'name text, chrom text, strand text, txStart text, txEnd text, cdsStart text, cdsEnd text, exonCount text, exonStarts text, exonEnds text'
      else:
        row  = ','.join(['r'+str(i+1)+' text' for i in range(cnt)])
    # 针对 SQLite/MySQL 不同构建插入语句
    if check_mysql(dbname):
      rcnt = ','.join(['%s' for i in range(cnt)])
    else:
      rcnt = ','.join(['?' for i in range(cnt)])
    # create new table
    cu.execute('create table if not exists %s (%s);'%(tname,row))
    # 文件指针回到开头位置(因为 zipfile 不支持 seek 功能, 因此需要重新打开)
    if z_type == 2:
      # 先关闭之前打开的文件，而后再打开
      f.close()
      gz_f.close()
      # 重新打开文件
      gz_f = zipfile.ZipFile(fname, 'r')
      # 获取 ZIP 文件中的第一个文件, 并且通过 io.TextIOWrapper 方式来解码
      f = TextIOWrapper(gz_f.open(gz_f.namelist()[0], 'r'), encoding = en_code)
      if tsv:
        r = csv.reader(f, delimiter='\t')
      else:
        r = csv.reader(f) #, delimiter=' ', quotechar='|')
    else:
      f.seek(0, 0)
    # 如果第一行是表头, 则递增 跳过计数器
    if ftype == 1: skip_r += 1
    # 跳过 头部 注释记录
    while skip_r:
      next(r)
      skip_r -= 1
    # 批量写入数据 (对于 非 csv/tsv 的生物信息学文件, 可能中间包含注释, 因此需要用逐行解析方式)
    if p_n == 0: # l_ext in ('.CSV', '.TSV')
      cu.executemany('insert into %s values (%s)'%(tname, rcnt), r)
    else:
      for t in r:
        if t[0][:p_n] == p_ext:
          continue
        else:
          cu.execute('insert into %s values (%s)'%(tname, rcnt), t)
    # 最后完成 commit, 关闭文件
    cx.commit()
    f.close()
    print('Load %d Records to table %s, spent time: %.2f s'%(rsize, tname, time.time() - bt))
    if cxt: cx.close()		# 如非内存连接，则关闭
  else:
    if err == 1:
      print('!!! Read File %s Error. items size problem (maybe last line problem).'%(fname))
    else:
      print('!!! Read File %s Error. file not found or encoding problem.'%(fname))

#
# load json file to new table
#		参数：数据库、json文件名、表名、JSON取值区域
#
def loadJSON(dbname, fname, t_name, vitem):
  import json

  # 加载 JSON 内容
  with open(fname, 'r',  encoding='utf-8') as f:
    d = json.load(f)

  # 如果有设置 JSON 取值区域，且在JSON中正确存在，则获取该区域的值
  if vitem:
    if vitem in d:
      d = d[vitem]
    else:
      print("*Err: JSON file can't found [%s] item."%vitem)
      return

  # 判断 JSON 取值是否有效 (列表类型), 如果无效则退出
  if not d or type(d) != type([]):
    print('*Err: JSON file Invalid value !')
    return

  # 定义JSON类型 -> 表类型转换表
  # i: 整数, r:实数, t:字符, td:字符(字典), tl:字符(列表), tn:字符(None), ib:整数(逻辑)
  db_tr = ( ('i', type(1)), ('r', type(1.1)), ('t', type('abc')), ('td', type({})), ('tl', type([])), ('tn', type(None)), ('ib', type(True)) )
  # sqlite 表类型转换
  tab_i = { 'i':'integer', 'ib':'integer', 'r':'real', 't':'text', 'td':'text', 'tl':'text', 'tn':'text' }

  # 初始化 子表结构 字典
  s_t = {}

  #
  # 扫描所有JSONs数据，从而构建 表字段 信息(只递归第一层的 [{},{}...] 结构, 因此 默认 loop=0)
  #
  def getItem(d, t={}, loop=0):
    for i in d:
      for j in i:
        # 获取对应 JSON 项的数据类型
        o_t = type(i[j])
        # 如果 loop 递归标志设置，则解析遇到的 [{},{}] 内容 (判断 i[j] 是避免 i[j] = [] 的情况导致错误)
        if loop and o_t == type([]) and i[j] and type(i[j][0]) == type({}):
          # 若 该子项 第一次出现，则初始化字典 (第一个字段是t_ID,用于和主表关联)
          if j not in s_t: s_t[j] = {'t_ID':'t'}
          # 递归 解析该子项下面的字典内容 (当前只解析第一层, loop=0)
          s_t[j] = getItem(i[j], t=s_t[j], loop=0)
        dtype = ''
        for dt in db_tr:
          if o_t == dt[1]:
            dtype = dt[0]
            break
        # 循环完成后，看是否有无法匹配的情况
        if dtype:
          o_t = dtype
        else:
          print('*Err: Can found.', o_t)
        # 判断该字段是否重复，如果重复，则类型是否匹配
        if j in t:
          if t[j][:1] != o_t[:1]:
            # 如果新的字段是 r 实数，原来为 i 整数，则应该设定字段为实数，(r 可以表达 i 的所有数据)
            if t[j] == 'i' and o_t == 'r': t[j] = 'r'
            # 如果非 r / i 的问题，则显示提示信息
            if t[j] not in ['i','r']:
              print('*Note: [%s] data type is [%s], but include [%s], Value:'%(j, t[j], o_t), i[j])
        else:
          t[j] = o_t
    # return result
    return t

  #
  # 解析 JSON 数据项，构造插入语句，将数据插入 (只递归第一层的 [{},{}...] 结构, 因此 默认 loop=0)
  # 参数: t_name-表名, i-JSON字段数据集, rsize-子表索引序号, t-JSON字段类型, loop-是否递归(默认0不敌贵)
  def insertItem(t_name, i, rsize, t, loop=0):
    odata = []
    # create insert statement (insert into t_name value (?,?,...))
    usql = 'insert into %s values (%s)'%(t_name, ','.join(['?' for i in range(len(t))]))

    # 构建插入数据
    for j in t:
      # 确保该字段在json数据中，如果不在，则用 None 替代(对应 sqlite 的 null)
      if j in i:
        # 如果 JSON 数据市 列表类型 []，则判断是否需要构建 子表
        if t[j]=='tl':
          # 字段为 None 则直接返回 None
          if i[j]:
            # 判断是否存在子表
            if loop and j in s_t:
              # 将当前 ID 顺序号作为值保存
              odata.append(str(rsize))
              # 插入 子表 数据
              for st in i[j]:
                # 添加 索引ID 字段
                st['t_ID'] = rsize
                insertItem(t_name+'_'+j, st, rsize, s_t[j])
            else:
              odata.append( ', '.join([str(z) for z in i[j]] ) )
          else:
            odata.append(None)
        # JSON 字典类型 {"xx":"abc","xxx":bbb,...} 转为字符串: 'xx:abc,xxx:bbb'
        elif t[j] == 'td':
          if i[j]:
            odata.append( ', '.join(['%s:%s'%(z, str(i[j][z])) for z in i[j] ] ) )
          else:
            odata.append(None)
        # True/False -> 1/0
        elif t[j] == 'ib':
          if i[j] == True:
            odata.append(1)
          else:
            odata.append(0)
        else:
          odata.append(i[j])
      else:
        odata.append(None)	# 如果希望子表序号返回为0，可以: odata.append( 0 if t[j] == 'tl' else None )
    # 插入数据库
    cu.execute(usql, odata)

  # 解析 JSON 结构，用于构建 表结构(t) 和 子表结构(s_t)
  t = getItem(d, t={}, loop=1)
  
  # 确认 JSON 加载正确且有数据
  if t:
    # Connect SQLite
    cx, cxt = dbconn(dbname)
    cu = cx.cursor()

    # create new table
    csql = 'create table if not exists %s ( %s )' % (t_name, ', '.join( [ '"%s" %s'%(i,tab_i[t[i]]) for i in t]))
    cu.execute(csql)
    # create sub-table
    for s in s_t:
      csql = 'create table if not exists %s ( %s )' % ('%s_%s'%(t_name,s), ', '.join( [ '"%s" %s'%(i,tab_i[s_t[s][i]]) for i in s_t[s] ]))
      cu.execute(csql)

    # insert data
    rsize = 0 
    for i in d:
      rsize += 1
      insertItem(t_name, i, rsize, t, loop=1)

    # commit db
    cx.commit()
    print('Load JSON %d Records to table %s'%(rsize, t_name))
    if s_t:
      print('- And create & insert sub tables: ',','.join([i for i in s_t]))
    if cxt: cx.close()		# 如非内存连接，则关闭


#
# 读取 GenBank 格式文件 Features 数据, 写入数据库表
#	 Features Ref: https://www.insdc.org/files/feature_table.html
#
def loadGenBank(dbname, f_name, t_name):
  '''
    读取 GenBank 格式文件，将 Features 的注释信息内容写入数据库表
    f_name: genbank 格式数据文件;  t_name: 数据库表名
  '''
  f_flag, locus, last_rec, n_first = 0, '', '', ''
  gbinfo, definfo, refinfo, gbitem, defitem, refitem = [], [], [], {}, {}, {}

  bt = time.time()
  # 数据库表 固定字段 (除此之外, 所有其它内容合并写入 note 字段)
  ditem = ['locus', 'type', 'gene', 'start', 'end', 'location', 'product', 'protein_id']

  # 对每个字段进行处理, 生成一行记录 (使用 strip 去除前后的 " )
  def r_gene(r):
    if r:
      # 将其它字段合并放到 note 项
      t_note = []
      for i in r:
        if i not in ditem:
          t_note.append( '%s=%s'%(i, r[i]) )
      # 将内容添加到列表(中间用 \t 分割)
      gbinfo.append([ r['locus'], r['type'], r['gene'].strip('"'), r['start'], r['end'], r['location'], r['product'].strip('"'), r['protein_id'].strip('"'), '\t'.join(t_note)])

  # !!! Python 的字符串操作 很多时候 比 正则快, 因此避免不必要的正则 (特别是在执行次数较多的地方)
  # 搜寻 /Qualifiers 内容, 格式: 21个空格 + /xxx=xxx , 例如: /gene="ORF1ab"
  re_fval = re.compile('^ {21}/(.+)=(.+)$')
  # 确认 Location 是否有效 (2 / 2..30 / 2.30 / <2..30 / <2..>30 / 2^3 )
  re_location = re.compile('^(?:\<*|.+?\:)\d+(?:$|(?:\.{1,2}\>?|\^)\d+$)$')
  # 简单的 Location 提取 (33..456 / 33.456) -> start,end
  re_slocation = re.compile('^(\d+)(?:\.{1,2})(\d+)$')

  # 读取文件(如果后缀.gz, 则以 gzip 方式打开)
  if f_name[-3:].upper() == '.GZ':
    f = gzip.open(f_name, 'rt', encoding='utf-8')
  else:
    f = open(f_name, 'rt', encoding='utf-8')
  for i in f:
    # 初始化已解析标志
    r_ok = 0
    # 如果已找到 Feature 部分, 则进行解析
    if f_flag:
      # 1. 搜寻 item 内容  (例如: /gene="ORF1ab" )
      if r_ok == 0:
        n = re_fval.findall(i)
        # 如果找到 item 的内容
        if n:
          r_ok = 1
          # 过滤掉 translation 内容, (这里包含的是蛋白质编码信息, 不建议保存在数据库)
          if n[0][0] == 'translation':
            n_first = ''
          else:
            n_first = n[0][0].strip()
            # 因为 /db_xref=xxx 这类信息会有多个, 因此需要判断后累加 (但需排除 gene/product/protein_id)
            if n_first not in ['gene', 'product', 'protein_id'] and n_first in gbitem:
              gbitem[n_first] += '; ' + n[0][1].strip()
            else:
              gbitem[n_first] = n[0][1].strip()
      # 2. 搜寻 features 例如: (gene 216..21496) or (CDS join(216..13409,13409..21496), location可能多行!
      # 1-5 blank  6-20 feature key   21 blank   22-80 location
      if r_ok == 0 and i[0:5] == '     ' and i[20:21] == ' ' and i[5:6] != ' ' and i[21:22] != ' ':
        f_t, f_l = i[5:20].strip(), i[21:].strip()
        if f_t and f_l:
          loc, n_first = '', ''
          if f_l[:5] == 'join(' or f_l[:11] == 'complement(' or f_l[:6] == 'order(':
            loc = f_l
            n_first = 'location'
          else:
            # 检测是否符合 location 规范
            fe = re_location.findall(f_l)
            if fe:
              loc = fe[0]
          # 如果找寻到 location 信息
          if loc:
            r_ok = 1
            # 解析开头/结尾地址, 对于 join 不解析 (原来采用复杂模式 (?:^|join\()(\d+)(?:.|..).*?(\d+)(?:$|\)$)
            s_loc = re_slocation.findall(loc)
            if s_loc:
              l_s, l_e = s_loc[0]
            else:
              l_s, l_e = 0, 0
            # 如果还有上一次未保存记录, 则保存
            if gbitem: r_gene(gbitem)
            # 初始化一个新记录 
            gbitem = {'locus':locus, 'type':f_t, 'gene':'', 'start':l_s, 'end':l_e, 'location':loc, 'product':'', 'protein_id':''}
      # 3. 如果出现 ORIGIN / LOCUS 表示 Feature 结束
      if r_ok == 0:
        if i[:6] == 'ORIGIN' or i[:5] == 'LOCUS':
          r_ok = 1
          f_flag = 0
          # 将未保存记录保存
          if gbitem: r_gene(gbitem)
          # 重设对应变量
          locus, gbitem = '', {}
      # 4. 如以上都不符合, 则判断为上一行信息的 折行 信息, 添加到上一行记录后 (location 不用补空格)
      if r_ok == 0 and n_first and i[:21].strip() == '':
        if n_first == 'location':
          gbitem[n_first] += i.strip()
        else:
          gbitem[n_first] += ' ' + i.strip()
    # 头部信息搜索 (LOCUS 开头给出序列信息; 而后 FEATURES)
    if f_flag == 0:
      # 如果存在序列名称, 寻找 序列 Features 块, 找到后设置标志 f_flag
      if locus :
        # 搜索 定义信息
        t = i[:10]
        # 1 处理 Defin 后面的附加信息 (在 Locus 部分已经创建, 这里主要处理后续部分)
        if defitem and t in ['DEFINITION','ACCESSION ', 'VERSION   ', 'DBLINK    ', 'KEYWORDS  ', 'SOURCE    ', '  ORGANISM', 'COMMENT   ']:
          last_rec = '@' + t.strip()
          defitem[t.strip()] = i[10:].strip()
        # 2.1 处理 Reference 信息
        elif t == 'REFERENCE ':
          # 如果有未写入信息, 则写入
          if refitem: refinfo.append([locus, refitem['REFERENCE'], refitem['TITLE'], refitem['AUTHORS'], refitem['JOURNAL'], refitem['PUBMED'], refitem['REMARK']])
          # 创建新的 REF 记录
          refitem = {'REFERENCE':i[10:].strip(), 'TITLE':'', 'AUTHORS':'', 'JOURNAL':'', 'PUBMED':'','REMARK':''}
          last_rec = 'REFERENCE'
        # 2.2 处理 Reference 后附加信息
        elif refitem and t in ['  AUTHORS ', '  TITLE   ', '  JOURNAL ', '   PUBMED ', '  REMARK  ']:
          last_rec = t.strip()
          refitem[last_rec] = i[10:].strip()
        # 3. 如果找到 FEATURES, 则设置标志, 开始进入 Features 搜寻
        elif i[:40] == 'FEATURES             Location/Qualifiers':
          f_flag = 1
          # 3.1 将未写入 Def 信息写入, 并清除缓存
          if defitem: 
            definfo.append([locus, defitem['LocusInfo'], defitem['DEFINITION'], defitem['ACCESSION'], defitem['VERSION'], defitem['DBLINK'], defitem['KEYWORDS'], defitem['SOURCE'], defitem['ORGANISM'], defitem['COMMENT']])
            defitem = {}
          # 3.2 将未写入 Ref 信息写入, 并清除缓存
          if refitem:
            refinfo.append([locus, refitem['REFERENCE'], refitem['TITLE'], refitem['AUTHORS'], refitem['JOURNAL'], refitem['PUBMED'], refitem['REMARK']])
            refitem = {}
        # 这里的内容应该属于 折行 内容, 添加到最后一个单元(last_rec记录的)
        elif last_rec and len(i) > 12 and i[:12].strip() == '':
          if last_rec[0] == '@':
            if defitem: defitem[last_rec[1:]] += ' ' + i.strip()
          else:
            if refitem: refitem[last_rec] += ' ' + i.strip()
      # 如果没有 Locus, 则搜索
      elif i[:6] == 'LOCUS ':
        last_rec = ''
        # 名称, 长度, 类型, 数据分类, 最后修订时间
        t = i[6:].split()
        if t:
          locus = t[0]
          # 初始化 Locus 保存字典
          defitem = {'LocusInfo':'%s'%t[1:], 'DEFINITION':'', 'ACCESSION':'', 'VERSION':'', 'DBLINK':'', 'KEYWORDS':'', 'SOURCE':'', 'ORGANISM':'', 'COMMENT':''}
          # 清空 ref 字典
          refitem = {}
  # 全部读取完成, 关闭文件, 数据库写入
  f.close()
  if gbinfo:
    # Connect SQLite
    cx, cxt = dbconn(dbname)
    cu = cx.cursor()
    # create new table
    cu.execute('create table if not exists %s (locus text, type text, gene text, start integer, end integer,location text, product text, protein_id text, note text)'%(t_name))
    # insert data
    cu.executemany('insert into %s values (?,?,?,?,?,?,?,?,?)'%(t_name), gbinfo)
    # commit and close file
    cx.commit()
    # 如果存在 def 信息, 则写入
    if definfo:
      # 创建 序列信息定义表
      cu.execute('create table if not exists %s (locus text, locusinfo text, reference text, accession text, version text, dblink text, keywords text, source text, organism text, comment text)'%(t_name+'_def'))
      # insert data
      cu.executemany('insert into %s values (?,?,?,?,?,?,?,?,?,?)'%(t_name+'_def'), definfo)
      cx.commit()
      print('- note: %s table auto create for file defind information. %s Records.'%(t_name+'_def', len(definfo)))
    # 如果存在 ref 信息, 则写入
    if refinfo:
      # 创建 序列信息定义表
      cu.execute('create table if not exists %s (locus text, reference text, title text, authors text, journal text, pubmed text, remark text)'%(t_name+'_ref'))
      # insert data
      cu.executemany('insert into %s values (?,?,?,?,?,?,?)'%(t_name+'_ref'), refinfo)
      cx.commit()
      print('- note: %s table auto create for file reference information. %s Records.'%(t_name+'_ref', len(refinfo)))
    # 输出信息
    print('# Load %d Records to table %s, spent time: %.2f s'%(len(gbinfo), t_name, time.time() - bt))

#
#	构建 MySQL 数据库表结构 
#  参数：数据库cursor对象,数据库名
#  返回：表结构[{'name':'table1','sqlite_str':'...','sqlite_ins':'...','mysql_str':'...','mysql_ins':'...'}]
#
def getMySQLinfo(cu,dbname):
  tables = []
  cu.execute('show tables;')
  table_info = cu.fetchall()
  # 列出所有表的结构
  for row in table_info:
    tb_name = row[0]
    cu.execute('SHOW FULL COLUMNS FROM ' + dbname + '.' + tb_name + ';')
    info = cu.fetchall()
    SQLite_v = []
    pk = []
    # 将 MySQL 对应的 数据类型 转换为 SQLite 
    for t_item in info:
      if t_item[4] == 'PRI': pk.append(t_item[0])
      # 构造SQLite字段
      if t_item[1].find('char') > -1 or t_item[1].find('datetime') > -1 or t_item[1].find('text') > -1:
        SQLite_v.append(t_item[0] + ' text')
      else:
        SQLite_v.append(t_item[0] + ' integer')
    # 构建PK定义内容
    if pk:
      pkstr = ', primary key(%s)'%(','.join(pk))
    else:
      pkstr = ''
    # 构建对应表结构定义
    table = {}
    table['name'] = tb_name
    table['sqlite_str'] = 'create table %s (%s%s)'%(tb_name, ', '.join(SQLite_v),pkstr)
    table['sqlite_ins'] = 'insert into %s values(%s)'%(tb_name,','.join('?'*len(info)))
    table['mysql_str'] = 'CREATE TABLE %s (%s%s)'%(tb_name, ', '.join([k[0] + ' ' + k[1] for k in info]),pkstr)
    table['mysql_ins'] = 'insert into %s values(%s)'%(tb_name,','.join('%s'*len(info)))
    tables.append(table)
  # 返回结果集
  return tables

#
# Query SQLite Database Info
# type: 0-Table  1-Index  2- MySQL表  3 - MySQL 表结构
def getSQLiteInfo(sqlite_db,type=0):
  # Connect Database
  cx, cxt = dbconn(sqlite_db)
  cu = cx.cursor()
  my = check_mysql(sqlite_db)
  cnt = 1
  # 如果是 MySQL
  if my:
    if type == 1:
      # 列出MySQL数据库的索引
      Qexec("SELECT a.TABLE_NAME,a.index_name,GROUP_CONCAT(column_name ORDER BY seq_in_index) AS `Columns` FROM information_schema.statistics a where a.TABLE_SCHEMA = '" + my[0] + "' GROUP BY a.TABLE_SCHEMA,a.TABLE_NAME,a.index_name")
    elif type == 2:
      # 列出所有 MySQL 表，（包括表的备注信息)
      Qexec("select table_name, table_comment, table_rows, round(data_length/1024/1024,2) from information_schema.TABLES where table_schema = '" + my[0] + "' ORDER BY table_name >[- _@0_ - _@1_ (_@3_ rows, _@4_ Mbytes)  _@2_  ]")
    elif type == 3:
      # 列出所有 MySQL 表结构 信息
      qCmd = "loop select table_name,table_comment,table_rows from information_schema.TABLES where table_schema = '" + my[0] + "' \n"
      qCmd += "echo ### _^0_ - _^1_ (_^3_ rows; _^2_) \n"
      qCmd += "select COLUMN_NAME 字段名, column_comment 字段说明, column_type 字段类型, column_key 约束 from information_schema. COLUMNS b where b.TABLE_NAME = '_^1_' >[- _@1_ _@3_ _@4_ _@2_] \n lend"
      Qexec(qCmd)
    else:
      tables = getMySQLinfo(cu,my[0])
      # 按照 SQLite/MySQL 模式输出表结构
      for i,j in enumerate(tables):
        oprint('# %d [%s] \n- SQLite: %s\n- MySQL: %s'%(i+1,j['name'],j['sqlite_str'],j['mysql_str']))
  # 如果是 SQLite
  else:
    if type == 0:
      stype = 'table'
    else:
      stype = 'index'
    cu.execute('select * from sqlite_master where type = "' + stype + '";')
    for row in cu.fetchall():
      if type == 0:
        oprint('# %d [%s] \n %s'%(cnt,row[1],format_t1(row[4])))
      else:
        oprint('# %d Table: %s index name: %s'%(cnt,row[2],row[1]))
      cnt +=1
  # 关闭连接
  cu.close()
  if cxt: cx.close()		# 如非内存连接，则关闭

#
# SQLite Query
#		跟在Select后面的输出类型： >[_@0_ _@1_] 输出格式化信息； >csv 文件名 输出csv 文件； ??>{name}输出到变量??
#		o_disp 参数默认为1, 输出信息; 只有在被作为 import 调用时, 才设置为0, 屏蔽所有输出信息
def SQLiteQuery(sqlite_db, sql, o_disp=1):
  # 通过正则判断 select 语句后面带有 >[ xxx ]内容，如果是，则表示输出内容需要拼接
  c = re.findall('(.*)\>\[(.*)\]',sql)
  o, csv_flag = '', 0
  if c:
    sql = c[0][0]
    o = c[0][1]
  else:
    # 判断是否输出 csv >CSV filename 0/1
    csv_p = re.findall('(.+?)>csv (.+?)(?:$| +(0|1)| .+)',sql,flags=re.IGNORECASE)
    # 如果是 csv 输出，则通过正则获取SQL指令、文件名，是否输出列名标记
    if csv_p:
      sql = csv_p[0][0].strip()
      csv_file = csv_p[0][1].strip()
      csv_flag = 1 + int(csv_p[0][2]) if csv_p[0][2] else 2
      # 判断文件名有效性
      if len(csv_file) < 3 or len(sql) < 10:
        print('!!!CSV File name error. or SQL Command Error')
        return -1
      # 输出到csv文件
      else:
        # 判断是否需要使用 gzip 压缩输出文件
        if csv_file[-3:].upper() == '.GZ':
          f = gzip.open(csv_file, 'wt', encoding='utf_8_sig', newline='')
          ext_flag = csv_file[-7:-3]
        else:
          f = open(csv_file, 'wt', encoding='utf_8_sig', newline='')		#excel 用utf-8 有问题
          ext_flag = csv_file[-4:]
        # 根据文件后缀判断(.csv or .tsv)来设置参数
        if ext_flag.upper() == '.TSV':
          csv_f = csv.writer(f, delimiter='\t')
        else:
          csv_f = csv.writer(f)
  # Connect SQLite
  bt = time.time()
  cx, cxt = dbconn(sqlite_db)
  cu = cx.cursor()
  Sqlite_ext_reset()
  cu.execute(sql)
  # 统计查询耗时
  if dinfo_flag and o_disp: print('* Query spent time: %.2f s *'%(time.time() - bt))
  cnt = 1
  # 返回结果列表(rcol:列名, retv:结果集)
  rcol, retv = [], []
  for row in cu:
    # 如果第一行，则打印/输出 表结构信息 (可以用 row['name']来访问，替代row[2])
    if cnt == 1:
      # 构建查询结果列名信息（SQLite/MySQL不同）
      if check_mysql(sqlite_db):
        rcol = [i[0] for i in cu.description]
      else:
        rcol = row.keys()
      if dinfo_flag and o_disp: print('--',' '.join(rcol),'--')
      # 输出/写入csv文件
      if csv_flag > 1: csv_f.writerow(rcol)
    if o:
      tmp = o
      # 替换所有内容
      for j, d in enumerate(row):
        tmp = tmp.replace('_@'+str(j+1)+'_',str(d))
      # 输出前，将_@0_替换为顺序号
      if o_disp: oprint(tmp.replace('_@0_',str(cnt)))
    else:
      if csv_flag:
        csv_f.writerow( row )
      else:
        if o_disp: oprint( '-%d %s'%(cnt,' '.join([str(j) for j in row])) )
    cnt += 1
    # 只在 o_disp == 0 的时候保存数据
    if o_disp == 0: retv.append( [j for j in row] )
  # 表示 结果集 为空, 可能是update/del等语句，从 cu.rowcount 获取影响行数
  if cnt == 1:
    cnt = cu.rowcount
  else:
    cnt -= 1
  if csv_flag:
    f.close()
    if o_disp: print('-- Total Write %d lines to %s .'%(cnt, csv_file))
  elif not o:
    if o_disp: print('------ Total: %d ------ '%(cnt))
  cx.commit()
  cu.close()
  if cxt: cx.close()		# 如非内存连接，则关闭
  # 返回执行的结果 (列信息, 数据集)
  return rcol, retv

#
# insert select data to table_insert
#
def SQliteCopy(sqlite_db,ndb,table_insert,sql):
  # Connect SQLite
  cx,cxt = dbconn(sqlite_db)
  cu = cx.cursor()
  cx2,cxt2 = dbconn(ndb)
  cu2 = cx2.cursor()
  Sqlite_ext_reset()
  cu.execute(sql)
  cnt, rcnt = 0, ''
  dbtype = check_mysql(ndb)
  while 1:
    i = cu.fetchone()	# 不用fetchall() 是因为避免大数据量（例如1千万条记录）导致对内存需求过大
    if not i: break		#如果没有记录，则退出循环
    # 如果还未构建插入格式串，则构建（只构建一次）
    if rcnt == '' :
      # 针对 SQLite/MySQL 不同构建插入语句
      if dbtype:
        rcnt = ','.join(['%s' for k in range(len(i))])
      else:
        rcnt = ','.join(['?' for k in range(len(i))])
    # MySQL/Sqlite不同方式处理
    if dbtype: 
      cu2.execute('insert into %s values (%s)'%(table_insert,rcnt),[x for x in i])
    else:
      cu2.execute('insert into %s values (%s)'%(table_insert,rcnt),i)
    cnt += 1
  print('%d Records copy to %s - %s table.'%(cnt,ndb,table_insert))
  cx2.commit()
  if cxt2: cx2.close()		# 如非内存连接，则关闭
  if cxt: cx.close()		# 如非内存连接，则关闭

#
# MySQL dump to SQLite (dump mysql sqlite)
#
def dumpMySQL(mysql_db,sqlite_db):
  my = check_mysql(mysql_db)
  if not my:
    print('!!! MySQL Database %s not found.'%(mysql_db))
    return -1
  # 构建连接
  cx, cxt = dbconn(mysql_db)
  if cx:
    cu = cx.cursor()
    # 获取数据库结构
    tables = getMySQLinfo(cu,my[0])
    cx2, cxt2 = dbconn(sqlite_db)
    cu2 = cx2.cursor()
    # 数据复制
    for table in tables:
      # 创建表
      if table['sqlite_str']:
        cu2.execute(table['sqlite_str'])
        cx.commit()
        print('# Table %s Created. Dump Data ...'%(table['name']),end='')
      # 复制数据 (每30000个记录一个段落进行)
      sPoint,sStep = 0, 50000
      while 1:
        cu.execute('select * from ' + table['name'] + ' limit ' + str(sPoint) + ',' + str(sStep) + ';')
        cnt = 0
        info = cu.fetchall()
        cu2.executemany(table['sqlite_ins'],info)
        cx2.commit()
        if len(info) < sStep:
          print(' [ %d Records copy]'%(sPoint + len(info)))
          break
        else:
          sPoint += sStep
          print(sPoint,end=' ',flush=True)


#
# Draw data using matplotlib
# type: L-line LX-Log line X LY-Log line Y LL-Log line X and Y; LS - Subplot Line;  L2 / L2X L2Y L2L
#       B-Bar  BX/BY/BL log   BS- subplot  B2
# 			H-hist HL-hist log, HLL-hist double log;
#       V-violin;
#       S-scatter
# 支持 draw l select * from a; draw h select * from b  (将多个绘制在子图内)
# 
def SQliteDraw(sqlite_db, cmd):
  # 解析命令串(多个 draw 放在一起，用于将图绘制在子图里)
  r = re.findall('(draw ([lsbhv].*?) (select .+?)(?:$|;))',cmd,flags=re.IGNORECASE)
  n_sub = len(r)	# 多少个 draw 指令
  # 如果无法找到正确参数，则退出
  if not n_sub:
    print('!!! Draw parameter error.')
    return -1
  # 参数检测
  for i in r:
    # 检查正则解析出来的内容是否正确 i[0]-完整语句  i[1]-参数 i[2]-select语句
    if len(i) != 3:
      print('!!! Multi-Draw cmd error,Please Check.')
      return 1
    # 如果子图模式中，存在 ls/bs 这种也包括子图的，报错并退出
    elif n_sub > 1 and i[1].upper().find('S') > 0:
      print('Multi-Draw include draw ls/bs, Please remove it.')
      return 1
  # 获取数据、绘制图形
  try:
    import matplotlib.pyplot as plt
    import locale
    # 只有中文环境才进行 PIL 字体设置
    if locale.getdefaultlocale()[0] == 'zh_CN': 
      # Matplotlib 中文字体 设置
      if sys.platform == 'darwin':
        # Mac 系统配置
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        # 确保负号正常显示
        plt.rcParams['axes.unicode_minus']=False
      elif sys.platform == 'win32':
        plt.rcParams['font.sans-serif']=['SimHei']
        # 确保负号正常显示
        plt.rcParams['axes.unicode_minus']=False
  except ModuleNotFoundError:
    print('# Please install matplotlib, using: pip3 install matplotlib')
    return -1
  except Exception:
    pass
  # 设置 Plot 绘制多条线的颜色顺序 for name, hex in matplotlib.colors.cnames.items():
  # plt_color = ('#1f77b4','blue','green','red','cyan','magenta','yellow','coral')
  plt_color = ('#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22')
  # 通过子图数量，构建子图参数；每行3个子图，因此只需要计算列
  # matplotlib 默认 fig_size(6.4,4.8) 4:3结构
  if n_sub > 1 or r[0][1].upper().find('S') > 0:
    sub_x, sub_y = 3 if n_sub>3 else n_sub, n_sub//3 + (1 if n_sub % 3 > 0 else 0)
    fig_size_x, fig_size_y = 9, 3.6 * sub_y		# 多子图尺寸
  else:
    fig_size_x, fig_size_y = 8.4, 4.2			# 无子图尺寸
  # 设置画布尺寸
  plt.close('all')	# 创建前，先关闭所有画布，避免因为之前意外错误未绘制的空画布
  fig = plt.figure(figsize=(fig_size_x, fig_size_y))
  # 利用 for 循环 绘制图形（可能是多个）
  sub_cnt = 0
  for i in r:
    sub_cnt += 1				# 当前子图序号
    type, sql = i[1].upper(), i[2]
    # 设置子图 (有子图,并且不存在 LS/BS 这类设置)
    if n_sub > 1 and type.find('S',1) == -1:
      plt.subplot(sub_y,sub_x,sub_cnt)
    # Connect SQLite
    cx,cxt = dbconn(sqlite_db)
    cu = cx.cursor()
    Sqlite_ext_reset()
    cu.execute(sql)
    data = {}
    row_name = []
    rcnt = 0		# 累计列数
    cnt = 0			# 累计行数
    # 查询数据库，构建结果集 {0:[col1...],1:[col2...]...}
    for i in cu.fetchall():
      cnt += 1
      # 获取结果列数量, 列名
      if rcnt == 0:
        rcnt = len(i)
        row_name = i.keys()
      for j in range(rcnt):
        if data.get(j): 
          data[j].append(i[j])
        else:
          data[j] = [i[j]]
    # 分布图/直方图 (HX:x轴对数分布，HY:Y轴对数，HL:双对数分布)
    if type[0:1] == 'H':
      # 为避免一些字符类型的数字，因此进行 float() 转换
      odata = [ float(i) for i in data[0] ]
      if type == 'HX' or type == 'HL':
        if min(data[0]) <= 0:
          print('!!!Data include < 0 item, Log Error.')
        else:
          odata = [math.log10(i) for i in odata]
      # 绘制图形,显示标注
      plt.hist(odata, 32, label=row_name[0])
      plt.legend(prop={'size': 7})
      if type == 'HL' or type == 'HY': plt.yscale('log')
    # 小提琴分布图
    elif type == 'V':
      plt.violinplot([ float(i) for i in data[0] ],showmeans=True,showmedians=False,showextrema=True)
    # 散点图 
    elif type == 'S':
      # 只提供一个参数，则自动构建 X 
      if rcnt == 1:
        x = [i for i in range(cnt)]
        plt.scatter(x, [ float(i) for i in data[0] ])
      # 只提供两个参数 (x,y)
      elif rcnt == 2:
        plt.scatter([ float(i) for i in data[0] ], [ float(i) for i in data[1] ])
      # 三个参数 (x,y,size)
      elif rcnt == 3:
        plt.scatter([ float(i) for i in data[0] ], [ float(i) for i in data[1] ], s=[ float(i) for i in data[2] ])
      # 四个参数 (x,y,size,color)
      elif rcnt == 4:
        plt.scatter([ float(i) for i in data[0] ], [ float(i) for i in data[1] ], s=[ float(i) for i in data[2] ], c=data[3])
      else:
        print('#参数不足以绘制散点图，最少需要两个参数,例如: draw s select x,y from table')
    # 柱状图(B) / 折线图(L)
    elif type[0:1] == 'B' or type[0:1] == 'L':
      # 数据集数量>1 并且设置 2 参数(将第一个数据集作为X轴)
      if rcnt > 1 and type.find('2') > 0:
        x = [float(i) for i in data[0]]
      else:
        x = [float(i) for i in range(cnt)]
      # 除第一个数据集外，其它都作为 Y 数据集绘制 (如果只有一个数据集,则作为 Y 绘制)
      for i in range(1 if rcnt>1 else 0, rcnt):
        # 如果 BS 则表示单独绘制, 因此创建子图; 否则叠加绘制(叠加绘制需要处理坐标偏移)
        if rcnt > 1 and type.find('S') > 0:
          plt.subplot(1, rcnt-1, i)
          s_step = 0
          pwidth = 0.8
        else:
          # 如果 rcnt>1, 叠加绘制计算 bar 宽度:  0.8/(rcnt-1)
          s_step = 0.8 if rcnt==1 else 0.8 / (rcnt-1)
          pwidth = s_step
        if type[0:1] == 'B':
          # 计算 X 轴位置的时候，根据需要进行 -/+ 偏移, 以便并排显示
          plt.bar( [dx + s_step*(i-rcnt/2) for dx in x], [ float(dy) for dy in data[i] ], width = pwidth, color=plt_color[i%10], label=row_name[i] )
        else:
          plt.plot( [dx for dx in x], [ float(dy) for dy in data[i] ], color=plt_color[i%10],label=row_name[i] )
        # 绘制标注
        plt.legend(prop={'size': 7})
        # 对数处理 (因为 L可能与第一个 L混淆，因此 find() 需要从1开始, 排除掉0位的L干扰)
        if type.find('L', 1) > 0 or type.find('X') > 0: plt.xscale('log')
        if type.find('L', 1) > 0 or type.find('Y') > 0: plt.yscale('log')
        # 如果属于需要处理标签的 (没有 b2 , 并且没有对 X 轴进行 log处理)
        if rcnt > 1 and type.find('2') < 0 and type.find('L', 1) < 0 and type.find('X') < 0:
          # 计算 x 轴标签数量 (默认32个, 如果多子图或bs参数, 则相应缩减)
          xlen = len(x)
          if n_sub > 1:
            ss = 16 if n_sub == 2 else 12			# 多子图模式, 横向最多3个
          # 如果是 BS 子图绘制, 则按子图个数等比缩减
          elif s_step == 0:
            ss = ss = int(32.0/(rcnt-1))
          else:
            ss = 32
          x1 = [k for k in range(0, xlen, 1 if xlen < ss else int(xlen/ss))]
          x2 = [data[0][k] for k in range(0, xlen, 1 if xlen < ss else int(xlen/ss))]
          plt.tick_params(labelsize=7)
          plt.xticks(x1, x2, rotation=90)
    # 如需关闭数据库连接，则关闭
    if cxt: cx.close()
  # 输出图片
  oplt_show(plt,fig)

#
#		命令解析
#
def proc_cmd(cmd0):
  global db, his_cmd, exec_flag, loop_flag, sql_block, loop_cnt, loop_cmd, f_html, dinfo_flag, mysql_srv
  try:
    # 判断是否 SQL 代码块 ( { code block } ), 若是则进行行累加
    if sql_block:
      # SQL 代码块结束
      if cmd0 == '}':
        cmd0 = sql_block.strip()
        sql_block = ''
      else:
        sql_block += ' ' + cmd0
        return
    # 非 SQL 代码块正常逻辑
    cmd = cmd0.upper()
    # loop_flag 标志一个 loop 已开始, loop_cnt 记录 loop 嵌套层数
    # 处在 Loop 标记块中, 记录命令到列表 loop_cmd; 如是最外层 lend (loop_cnt==1 and cmd[:4] == 'LEND'), 则交由后续 lend 模块负责执行
    if loop_flag and (cmd[:4] != 'LEND' or loop_cnt > 1):
      # 对于内部嵌套的 loop/lend 进行处理 (遇到 loop 嵌套层数+1, lend 层数-1)
      if cmd[:4] == 'LOOP':
        loop_cnt += 1
      if cmd[:4] == 'LEND':
        loop_cnt -= 1
      # 将 loop / lend 循环体内的指令保存起来
      loop_cmd[-1].append(cmd0)
    # SQL 代码块判断, 如果是则设置为' ' (非空)
    elif cmd == '{':
      sql_block = ' '
    # 清屏
    elif cmd == 'CLS' or cmd =='CLEAR':
      os.system(cmd0)
    # 解析具体指令, ?/h
    elif re.findall('^(?:H|\?)($| .+)',cmd):
      help_q = cmd0[1:].strip()
      # 如果 后面有关键字，则进行过滤
      if help_q:
        for i in help_str.split('\n'):
          if help_q.lower() in i.lower():
            print(i)
      else:
        print(help_str)
    elif cmd[:4] == 'OPEN':
      db = cmd0[5:]
      my = re.findall('#(.+?)#',db)
      # Check Files
      if db == ':memory:':
        print('Using Share Memory Database.')
      elif my:
        if not mysql_srv.get(my[0]):
          db = ''
          print('!!! Please using: [ mysql dbname serverip user password ] setup MySQL Server.')
        else:
          print('Using MySQL Server Database.')
      elif not os.path.exists(db):
        print('@ %s Not Found, Create it.'%(db))
    elif cmd[:5] == 'MYSQL':
      s = re.findall('(.+?) (.+?) (.+?) (.+$)',cmd0[6:])
      if s:
        mysql_srv[s[0][0]] = [s[0][1],s[0][2],s[0][3]]
      else:
        # 显示 当前存储的 mysql 列表
        if mysql_srv:
          for t_mysql in mysql_srv:
            print(f'- MySQL Server: [{t_mysql}], {mysql_srv[t_mysql]}')
        else:
          print('!!! Please using: mysql dbname serverip user password')
    elif cmd[:2] == 'DB':
      print('- SQLite Version: %s'%(sqlite3.sqlite_version))
      if db:
        print('Database: %s '%(db))
      else:
        print('!!! Not Open Database, Using open dbname to open.')
    elif cmd[:4] == 'ECHO':
        oprint(cmd0[5:])
    elif cmd[:5] == 'DINFO':
        if cmd[6:8] == 'ON':
          dinfo_flag = 1
        elif cmd[6:9] == 'OFF':
          dinfo_flag = 0
        elif len(cmd) > 5:
          print('Using dinfo on/off switch on/off debug message.')
        # 显示状态
        print('- Debug info : %s'%(('Off','On')[dinfo_flag]))
    elif cmd[:4] == 'INFO':
      if db:
        t_type = cmd[5:6]
        if t_type.isdigit():
          getSQLiteInfo(db,int(t_type))
        else:
          getSQLiteInfo(db,0)
      else:
        print('!!! Not Open Database.')
    elif cmd[:4] == 'COPY':
      if db:
        cmd0_s = cmd0.split(' ')
        ndb, ntb = cmd0_s[1], cmd0_s[2]
        sql = ' '.join(cmd0_s[3:])
        if sql[:7].upper() == 'SELECT ':
          SQliteCopy(db,ndb,ntb,sql)
        else:
          print('!!! Using dbname table select ...')
      else:
        print('!!! Not Open Database.')
    elif cmd[:4] == 'DUMP':
      v = re.findall('^(#.+#?) (.+)',cmd0[5:])
      if v:
        if len(v[0]) == 2:
          dumpMySQL(v[0][0],v[0][1])
          return 0
      print('!!! Using dump #mysqldb# sqlitedb to dump MySQL db to SQLite.')
    elif cmd[:7] == 'LOADCSV':
      if db:
        v = re.findall('loadcsv (.+?) (.+?)($| \d)', cmd0, flags=re.IGNORECASE)
        if v:
          csv = v[0][0]
          tbl = v[0][1].strip()
          f = 1 if v[0][2].strip() == '1' else 0
          loadCSV(db,csv,tbl,f)
        else:
          print('!!! Using loadcsv csvfile table 0/1')
      else:
        print('!!! Not Open Database.')
    elif cmd[:6] == 'LOADGB':
      if db:
        v = re.findall('loadgb (.+?) (.+?)$', cmd0, flags=re.IGNORECASE)
        if v:
          gbfile = v[0][0].strip()
          tbl = v[0][1].strip()
          loadGenBank( db, gbfile, tbl )
        else:
          print('!!! Using loadgb genbank table')
      else:
        print('!!! Not Open Database.')
    elif cmd[:8] == 'LOADJSON':
      if db:
        v = re.findall('loadjson (.+?) (.+?)($| .+?$)', cmd0, flags=re.IGNORECASE)
        if v:
          json = v[0][0]
          tbl = v[0][1].strip()
          loadJSON( db, json, tbl, v[0][2].strip() )
        else:
          print('!!! Using loadjson jsonfile table item')
      else:
        print('!!! Not Open Database.')
    elif cmd[:4] == 'DRAW':
        SQliteDraw(db,cmd0)
    elif cmd[:5] == 'CHTML':
        if f_html:
          f_html.write('</body>')
          f_html.close()
          f_html = None
    elif cmd[:4] == 'HTML' and not f_html:
        html_name = cmd0.split(' ')
        if len(html_name) == 2:
          f_html = open(html_name[1], 'w', encoding='utf_8')
          f_html.write('<head><meta charset="utf-8"></head><body style="">') #br{font-size:0}">')
        else:
          print('!!! Not filename, Using html out.html ')
    elif cmd[:4] == 'LOOP':
        # loop_flag 标志一个 loop 开始, loop_cnt 记录 loop 嵌套层数
        loop_flag = 1
        loop_cnt += 1
        loop_cmd.append([cmd0[5:] ])
    # loop / lend 匹配完成, 执行 内部脚本
    elif cmd[:4] == 'LEND':
        loop_flag = 0
        loop_cnt = 0
        if db and loop_cmd[-1]:
          # 如果是查询语句，则执行
          if loop_cmd[-1][0].upper().strip()[:7] == 'SELECT ':
            # Connect SQLite
            cx,cxt = dbconn(db)
            cu = cx.cursor()
            Sqlite_ext_reset()
            cu.execute(loop_cmd[-1][0])
            res = cu.fetchall()
          # loadweb 则获取网页, 正则提取内容
          elif loop_cmd[-1][0].upper().strip()[:8] == 'LOADWEB ':
            # 执行 loadweb 返回解析结果
            res = loadweb( loop_cmd[-1][0] )
          else:
            # 非select/loadweb语句, 作为列表处理
            try:
              res = eval(loop_cmd[-1][0])
              # 用这个进行测试，看看数据是否二维 [(1,2),(1,2)]
              tmp = res[0][0]
            except:
              print('loop error, please using [(1,2,...),(1,2,...)...]')
              res = []
          # 用结果集替换所有 loop 结构体内的特定内容 _@n_
          cnt = 0
          sub_loop = 0		# 是否遇到嵌套 loop
          for row in res:
            cnt += 1		# 执行次数计数器
            # 用具体结果，替换对应参数
            tmp = [i for i in loop_cmd[-1][1:]]
            for j in range(len(tmp)):
              if tmp[j][:4].upper() == 'LOOP':
                sub_loop += 1
              if tmp[j][:4].upper() == 'LEND':
                sub_loop -= 1
              # 对 非嵌套，或第一层嵌套的 LOOP ，使用替换；否则不进行替换
              if sub_loop == 0 or (sub_loop == 1 and tmp[j][:4].upper() == 'LOOP'):
                # 对于 _^0_ 替换为顺序号
                tmp[j] = tmp[j].replace('_^0_',str(cnt))
                for i, d in enumerate(row):
                  # 对于 _^x_ 替换为对应结果
                  tmp[j] = tmp[j].replace('_^'+str(i+1)+'_',str(d))
              # 执行结构体内指令
              proc_cmd(tmp[j])
          # 完成循环后，弹出
          loop_cmd.pop()
        else:
          print('!!! Not Open Database or loop is none.')
    # 列出当前目录文件 (ls or ls *.csv)
    elif cmd[:2] == 'LS':
      ext_str = cmd0[3:].strip().replace('*','.*')
      d_cnt = 0
      for f in os.listdir('.'):
        # 如果后面有 参数，则根据参数过滤
        if ext_str == '' or re.search(ext_str, f, re.IGNORECASE):
          d_cnt += 1
          print('- %d %s (%sK)'%(d_cnt, f, format(round(os.path.getsize(f)/1024), ',d' )) )
    # 下载文件
    elif cmd[:9] == 'DOWNLOAD ':
      dfarg = re.findall('(http[s]{0,1}:\/\/.+?) (.+?)$', cmd0[9:])
      if dfarg:
        url, fname = dfarg[0][0].strip(), dfarg[0][1].strip()
        if url and fname:
          downloadfile(url, fname)
        else:
          print('# Please check filename.')
      else:
        print('# Using download https://xxx.xxx/ddd myfile.csv')
    # 执行脚本命令
    elif cmd[:5] == 'EXEC ':
      e_file = cmd0[5:].strip()
      if e_file:
        # 为避免递归, 检查当前执行过程名称是否一样
        if e_file.upper() not in exec_flag:
          # 将当前执行脚本名加入执行堆栈
          exec_flag.append(e_file.upper())
          try:
            with open(e_file, 'r',  encoding='utf-8') as f:
              Qexec(f.read())
          except FileNotFoundError:
            print('# Script file [%s] not found !'%e_file)
          # 执行完成, 弹出堆栈
          if exec_flag: exec_flag.pop()
        else:
          print('# Exec not support recursive !')
          exec_flag = []
    # la / l3 / l> file / l< file 历史命令
    elif re.findall('^L(?:(A$|$)|(\d+)$|(>|<) (.+)$)', cmd0, re.IGNORECASE):
      # 从历史记录删除这个记录
      if his_cmd: del his_cmd[-1]
      his_len = len(his_cmd)
      # 解析参数 0-A; 1-n; 2- >or<; 3- file
      ext_cmd = re.findall('^L(?:(A$|$)|(\d+)$|(>|<) (.+)$)', cmd0, re.IGNORECASE)[0]
      # 1. 判断是否有参数 l00 , 执行对应命令
      if ext_cmd[1]:
        inx_cmd = int(ext_cmd[1])
        if inx_cmd < his_len:
            proc_cmd(his_cmd[his_len - 1 - inx_cmd])
        else:
          if his_len > 0: print('!!! History Number out of (0-%d).'%(his_len-1))
      # 2. 判断是否 导出 历史
      elif ext_cmd[2] == '>':
        if his_cmd:
          try:
            with open(ext_cmd[3], 'a',  encoding='utf-8') as f:
              f.write('#\n# %s History \n#\n'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
              for i in his_cmd:
                f.write(i+'\n')
          except:
            print('# Export history to [%s] error !'%ext_cmd[3])
        else:
          print('# No history to write.')
      # 3. 判断是否 导入 历史
      elif ext_cmd[2] == '<':
        try:
          with open(ext_cmd[3], 'r',  encoding='utf-8') as f:
            for i in f.read().splitlines():
              i = i.strip()
              if i and i[:1] != '#':
                his_cmd.append(i)
        except:
          print('# Load history from [%s] error !'%ext_cmd[3])
      # 4. 列出历史命令
      else:
        # 如果有 A, 则列出所有, 否则列出最近 12 条 (到排序)
        cnt_cmd = his_len if ext_cmd[0].upper() == 'A' else 12
        c = cnt_cmd if cnt_cmd < his_len else his_len
        for i in his_cmd[-cnt_cmd: ]:
          c -= 1
          print('#%d %s'%(c,i))
    elif len(cmd) < 6:
      if his_cmd: del his_cmd[-1]
      print('!!! SQL Command Error.')
    else:
      SQLiteQuery(db,cmd0)
  except sqlite3.OperationalError as err:
    print('!!! SQL Command Error: %s'%(err))
  except sqlite3.Warning as err:
    print('!!! SQL Command Warning: %s'%(err))
  except Exception as err:
    print('!!! Error: %s'%(err))

#
# Qsqlite 脚本文件执行函数
#
def Qexec(cmd):
  '''
  Execute Qsqlite Script
    cmd: Qsqlite script 
  '''
  cmds = cmd.splitlines()  # split \n\r not only split('\n')
  cblock = False			# 采用 ''' 块注释标记
  try:
    for i in cmds:
      i = i.strip()
      if i:
        # 如果出现块注释，则取反注释标记(配对出现)
        if i[:3] == "'''":
          cblock = not cblock
          continue
        # 如果不属于块注释范围，则解释命令；否则跳过
        if not cblock:
          if i[0] != '#' and i[0] !='-':
            proc_cmd(i)
  except KeyboardInterrupt:
    print('!!! Ctrl+c Break.')

#
# Qselect 执行查询语句, 返回行信息, 结果集
#
def Qselect(dbconn, cmd):
  '''
  Execute SQL command and return result.
    dbconn: database connect, etc :memory: , my.db #mysql#
    cmd: sql, etc: select * from abc limit 20
  Return:
    row_info: a list for row info, etc: ['date','name','age']
    result:   result list, etc: [ ['2022-03-28','apple',12], ['2022-02-28','google',3] ]
  '''
  return SQLiteQuery(dbconn, cmd, 0)

#
# Main
#
def main():
  global his_cmd, wcmd
  # 如果命令行有参数，则作为脚本文件名处理
  if len(sys.argv) > 1:
    cmd_file = sys.argv[1]
    try:
      # 读取脚本文件内容，而后调用脚本解析函数
      f = open(cmd_file, 'r', encoding='utf-8')
      cmd = f.read()
      f.close()
      #
      # 1. 解析是否存在 webserver 命令，如果存在，则启动 web 服务
      #
      wip, wport, wcmd = parsingWeb(cmd)
      if wcmd:
        # 启动 Web 服务器 
        print('Starting Webserver @ %s:%d...'%(wip,wport))
        httpd = HTTPServer((wip,wport), Websrv)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            # 直接清空指令，退出
          print(' WebServer Stop...')
        finally:
          httpd.server_close()
      #
      # 2. 解析是否存在 jobserver 命令，如果存在，则启动 job 服务
      #
      else:
        wcmd = parsingJob(cmd)
        if wcmd:
          # 启动 Job Server 服务器
          print('JobServer Started.')
          try:
            JobServer(wcmd)
          except KeyboardInterrupt:
            print(' JobServer Stop...')
        #
        # 3. 解析普通脚本文件，并执行
        #
        else:
          Qexec(cmd)
    # 错误处理
    except FileNotFoundError:
      print('!!! Script File not found.')
  # 交互命令行操作
  else:
    print('> Quick SQLite Cmd/Script Tools V%s (?/h - Help, q - Quit)'%__version__)
    while True:
      try:
        cmd0 = input('> ').strip()
        if cmd0 == 'Q' or cmd0 == 'q':
          break
        elif cmd0 == '' or cmd0[:1]== '#':
          continue
        else:
          his_cmd.append(cmd0)
          proc_cmd(cmd0)
      except KeyboardInterrupt:
        print('!!! Ctrl+c Break.')
        # !!! 如不加延迟，会导致获得两次ctrl+c, 触发During handling of the above exception, another exception occurred
        time.sleep(0.1)

if __name__ == "__main__":
  main()
