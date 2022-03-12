# Quick SQLite Cmd/Script Tools

## Qsqlite 介绍
- 一个**命令行工具**，可通过交互方式来操作 sqlite 或 mysql 数据库, 快速实现数据处理、分析、统计、图形展示工作;
  - 常规 sqlite 操作（类似于 sqlite 提供的命令行工具); 可以方便的使用 sql 语句进行操作.
	- 支持 sqlite 及 sqlite 内存数据库(:memory:)、支持mysql数据库、将整个mysql数据库复制到sqlite、sqlite 不同数据库间表的复制操作.
	- 加载 csv 或 json 数据，或将 select 结果输出到 csv 文件.
	- 用 select 语句获取的数据绘制图形，例如：散点图、折线图、直方图(分布)、小提琴图(基于数据分布).
	- 提供系列扩展的 sqlite 函数，支持 正则操作、基于文本的sum操作、中国身份证识别等扩展功能.
- 一个**脚本解释器**，可以通过编写脚本文件，批量、自动化执行系列操作，实现数据处理、分析、报表输出工作;
	- 提供基于 sql 语句的脚本功能，让你能将批量操作自动完成，并且将结果输出到一个 html 文件.
	- 支持扩展的 loop/lend 带嵌套支持的循环语句, 便于实现一些 sql 语句无法处理的操作需求.
	- 支持对 select 结果进行格式化输出的语法，便于生成格式化的报表.
	- 输出的 html 文件中，图形将以内嵌的形式保存，使得只需要发送单一 html 文件就能完整展示所有图表内容.
- 一个**Web服务器** 和 **Job服务器**，可基于数据库提供 web 或 定时任务 处理后台服务;
	- Web 服务器可通过脚本定义来实现数据查询，数据插入操作，便于将数据统计、分析结果以 浏览器 方式实现交互.
	- Job 服务器可通过脚本定义来实现定时的数据清理、数据汇总、分析、报表生成，并且以本地文件输出，或发送邮件方式分享结果.
- 一个**Python库**, 通过 from Qsqlite import Qexec 导入, 在 python 或 ipynb jupyter/ipython notebook 中使用 Qexec(cmds) 调用, cmds 可以是一个带换行符的字符串，包括系列的命令 或 一个指令.
- **总结**: 借助 sqlite 强大的 sql 语法功能 和 高性能的表现，Qsqlite希望能让你**高效**的发挥 sqlite 和 sql语法 的能力，快速实现数据的整理、分析、统计、展示工作；并在需要时可通过导出/导入 csv 文件和 Excel 进行协同工作，实现更高效率。

## 快速使用
1. 将 Qsqlite.py 复制到本地, 而后在 命令行/终端 下运行 python Qsqlite.py (请确认使用 python3 环境运行)
2. 现在你可以输入 sql 指令或输入 ? 来获取帮助信息，或者尝试将下面指令复制进去运行测试一下
```sql
	# 打开一个内存数据库
	open :memory:
	# 创建 demo 表
	create table demo(ID text, Name text, Age integer)
	# 利用 loop/lend 循环插入数据
	loop [ [i, i**2] for i in range(1,100) ]
	insert into demo values ('_^1_', 'User_^1_', _^2_)
	lend
	# 输出数据
	info
	select count(*) from demo 
	select * from demo limit 10 >[- ID: _@1_, Name: _@2_, Age: _@3_]
	# 绘制图形
	draw l select age from demo; draw ll select id,age from demo
```
3. 可尝试运行 demo 目录下的 演示脚本 文件, 使用 python3 Qsqlite.py 脚本文件名 来运行
	- qloop.txt   loop/lend功能演示
	- qdraw.txt   html输出及绘图功能演示 （需使用 demo 目录下两个 csv 文件)
	- qweb.txt    Web服务器功能演示
	- qjob.txt    Job任务服务器功能演示

## Qsqlite 功能
### 1. 基础数据库操作功能
- 1.1 打开 SQLite 数据库
  - **open dbname**  打开一个 sqllite 数据库文件
  - **open :memory:** 打开 sqlite 内存数据库文件; 可利用内存数据库进行临时数据处理、中转
	- **db** 显示当前打开的数据库名
  - 如提供的文件名不存在，则会创建一个新的数据库文件
- 1.2 MySQL 数据库支持
	1. 用 **mysql dbname server user password** 创建一个MySQL数据库连接
    - 例如: mysql test 127.0.0.1 root pwd  (如需设置 MySQL 端口号，可用: mysql test 127.0.0.1:3308 root pwd)
    - 可用 mysql 指令设置多个 MySQL 的数据库，而后用 open 来切换;
	2. 用 **open #dbname#** 来打开/切换 MySQL 数据库;
  3. 一些 MySQL 命令
    - show databases     列出数据库服务器上的所有数据库
		- show tables        列出当前数据库的所有表
		- show keys from tb  列出某个表所包含的索引
- 1.3 常用状态指令
  - **info** 显示当前打开数据库的 表 信息
    - **info 1** 显示当前打开数据库的 索引 信息
    - **info 2** 显示当前连接的 MySQL 表（包括表的记录数、所占空间大小）
    - **info 3** 显示当前连接的 MySQL 带注释信息的 表结构
  - **dinfo on/off** 开启/关闭 数据库查询调试信息显示
  - **ls** 列出当前目录下的文件信息，支持 ls *.db 通配符，便于过滤文件
  - **l** 列出最近使用的 12 条操作指令
    - **la** 列出所有使用过的操作指令
    - **l0** 执行最后一个操作指令, 也可以用对应序号来执行以前的操作指令, 例如: l3, l22
- 1.4 数据库复制操作
  - **copy db tableDest select * from tabSource**
    - 用于在多个数据库之间进行 表数据复制, 例如将当前数据库中的 tabSource表的内容，复制到 db 数据库的 tableDest 表中去；
    - 例子: 将数据库 A.db 中的 tableA 表内容，复制到一个新的数据库 B.db 的 NewA 表中去
      1. open A.db
      2. 用 info 列出 数据库表结构，将 tableA 表结构创建语句复制下来
      3. open B.db 打开 B 数据库, 利用刚才复制的创建语句，在 B 数据库创建 NewA 表
      4. open A.db 回到 数据库 A
      5. 使用 copy B NewA select * from tableA 命令将 A 数据库的 tableA 表内容，复制到 B 数据库 NewA 表 (因为使用 select 语句，因此可以用 where 条件或其它方式灵活进行数据过滤,组织,处理)
      6. 可以通过使用 open :memory: 内存数据库来进行数据中转,处理; 也可以使用 MySQL 数据库进行操作
  - **dump #mysqldb# sqlitedb**
    - 将 mysqldb 数据库的所有表复制到一个 sqlite 数据库中; 该指令会自动扫描 mysql 数据库表结构，而后在对应的 sqlite 中创建对应的表，并且完成数据的复制.
    - 可以用 dump #mysqldb# :memory: 将数据复制到 内存 sqlite 数据库
- 1.5 查询语句输出格式化操作
  - **>[ ]**
    - 默认 select 查询结果会自动列出, 不需特殊处理, 除非你希望格式化输出, 则可以在语句后用 >[] 来调整
    - 例如 select * from table >[- ID: _@1_, Name: _@2_(_@3_), Age: _@4_]
    - 在这里 _@1_ 表示 select 语句 返回的第一列, _@2_ 表示第二列，依次类推; 如希望显示顺序号(从1开始，自动递增), 可用 _@0_ 表示, 例如: select * from table limit 10 >[ _@0_ ID: _@1_, Name: _@2_]

### 2. 加载或导出 csv 和 加载 JSON 功能
- 2.1 加载 csv , 使用: **loadcsv file.csv tab01**
	- 加载 file.csv 文件, 自动根据 csv 文件栏目创建 tab01 表，而后将 csv 文件内容插入到表中.
		- tab01 ( "r1" text, "r2" text, "r3" text )
	- 如果 csv 文件包含表头信 (一般在文件第一行)，则可设置参数(最后加上参数 1 )，以便正确识别.
		- 使用: **loadcsv filecsv tab01 1**
		- 将会自动根据csv表头信息来构建 数据库表 的信息，而后插入数据，例如:
			- tab01 ( "ID" text, "Name" text, "Tele" text )
- 2.2 导出 csv
  - 使用 **>csv csv文件名 0/1** (后面的参数0/1 表示是否导出表头信息. 0-不导出, 1-导出)
  - 例如: select * from table1 where n=300 >csv user1.csv 1 , 通过 select 将 某个表的内容导出到 user1.csv 文件，并且导出表头信息(导出的csv文件第一行是数据库表头信息)
  - 例如: select ID, name, sum(val) as val from tab1 group by ID limit 100 >csv test1.csv 
- 2.3 简单 JSON 数据加载, 例如: JSON 文件 t1.json 内容如下:
```json
[{"Corp": "Apple", "ID": 123}, {"Corp": "Microsoft", "ID": 456}, {"Corp": "IBM", "ID": 789}]
```
	- 使用: **loadjson t1.json corp**
		- 将读取 t1.json 文件, 根据JSON内容，创建 corp 表
			- corp ( "Corp" text, "ID" integer )
		- 而后读取 JSON 文件内容，插入 corp 表

- 2.4 复杂 JSON 数据, 例如: JSON 文件 t2.json 内容如下:
```json
{"Result":0, "Return":[{"Corp": "Apple", "ID": 123, "Product":[{"ID":1,"Name":"iPhone"}, {"ID":2,"Name":"iPad"}, {"ID":3,"Name":"Mac"}], "Profit":[{"Type":"Profit1","P":3456789}]}, {"Corp": "Microsoft", "ID": 456, "Product":[{"ID":11,"Name":"Windows"}, {"ID":12,"Name":"Office"}]}, {"Corp": "IBM", "ID": 789, "Product":[{"ID":21, "Name":"MainFrame"}], "Profit":[{"Type":"Profit1","P":1234567}, {"Type":"Profit2","P":336699}] }], "Ref":1234567}	
```
- 希望写入数据库的内容, 存放在 JSON 的 "Return" 栏目, 因此需要通过参数设置告诉 Qsqlite
- 使用: **loadjson t2.json ncorp Return**
  - 读取 t2.json 文件, 获取 "Return" 栏目的数据, 创建 ncorp, ncorp_Product, ncorp_Profit 3个表.
    - ncorp ( "Corp" text, "ID" integer, "Product" text, "Profit" text )
    - ncorp_Product ( "t_ID" text, "ID" integer, "Name" text )
    - ncorp_Profit ( "t_ID" text, "Type" text, "P" integer )
    - 为什么是 3 个表? 因为 Qsqlite 发现 JSON 数据里面包含了 子列表 (Product 和 Profit), 所以自动创建两个对应子表，并且通过 在 ncorp 自动增加 Product, Profit 字段关联 2 个子表.
  - 注意: 当前只支持第一层级的 子表 创建，不会递归到下面层级

### 3. 绘制图表功能 (折线图、分布图、箱型图、散点图)
- 3.1 **draw s** 绘制散点图
  - 一个数据集，作为 Y 坐标，自动生成 0-N 的X坐标:  draw s select y from table
  - 两个数据集，则作为 X,Y 坐标:  draw s select x, y from table 
  - 三个数据集，前两个为 X,Y 坐标, 后一个为 点大小 参数: draw s select x, y, size from table 
  - 四个数据集, 前两个为 X,Y 坐标, 后两个为 点大小, 点颜色参数: draw s select x, y, size, color from table
- 3.2 **draw l** 绘制折线图, 可绘制一组或多组数据，如果只有一组数据（select a from tb1），系统会自动根据结果集数量，产生对应的X轴数据(0..N); 如果是多个数据，则第一行数据作为 X 轴标记显示（一般是日期/时间），其它作为 Y 轴 (select x_lable,col1,col2 from tab1);
  - **draw l2** 表示 X 轴的数据不是系统产生的 0-N 的等比例数据, 而是用 select 结果第一项；例如：draw l2 select height, weight, m from tb1
  - **draw ll** 表示对 Y 轴进行对数处理;  **draw ll2** 表示进行 X-Y 轴进行双对数处理;
  - **draw ls** 将多个数据列，绘制在不同的 **子图** 上，并列排放;
- 3.3 **draw h** 绘制分布图(直方图), 只取结果集的第一列; 
  - **draw hx** 表示对 分布图的 X 轴进行对数处理; 
  - **draw hy** 表示对 分布图的 Y 轴进行对数处理;
  - **draw hl** 表示对 X-Y 轴双对数处理;
- 3.4 **draw v** 表示绘制小提琴箱型分布图，只取结果集第一列;
- 3.5 **多图绘制**功能, 将不同的类型图，通过子图模式，绘制在一个输出图片里, 子图之间用 ; 分割。 例如下面例子将绘制4个子图
  - draw l select a,b,c from t1; draw hl select a from t2; draw ll select a,b from t3; draw v select a from t4
- 3.6 Draw 功能演示脚本，可参考 Demo 目录下的 qdraw.txt 脚本文件. 用 python3 Qsqlite.py qdraw.txt 运行, 而后会生成一个 city_map.html 文件. (注意: 该演示脚本会用到 demo 目录下的 cn_city_l3_xy.csv, cn_city_l2_xyp.csv 两个文件，请确保这两个文件存在)

### 4. SQLite 扩展函数
1. 行字符串累加: **csum(列名)**，就像SQLite的默认sum()函数，sum()累加每列的值，返回总数；而csum()将每列作为字符串拼接起来;
	- select csum('apple','ibm','oracle') 将返回 'apple ibm oracle'
  - select mID,csum(nName),count(*) from T group by mID 或者 select csum(nName||'-'||nOrg) ...
2. 正则判断功能：**regexp(正则表达式,列/字串)**  用于判断某个列的内容是否符合正则表达式；返回结果是 布尔类型（True/False)
	- select * from tab1 where regexp('^[1]([3-9])[0-9]{9}$',mobile) = false
3. 正则提取功能: **regfind(正则表达式,列/字串,n)** 用于利用正则从列/字串提取内容, n=1 表示获取第1个结果, 2表示获取第2个, n = 0 表示获取所有结果，结果之间用空格分割; 
	- select regfind('1(.*?)2','1hello2 1good2',1)    n=1返回hello, n=2返回good,  n=0返回 hello good
4. 正则替换功能: **regsub(正则表达式,替换串,列/字串)**  利用正则匹配，替换字符串
	- regsub('([\d]{3})','#\1#','Test000-372')  -> Test#000#-#372# 
5. 字符串单元去重: **destr(列/字串,分隔符)** 用于将分隔符连接的字串，分割后，去重元素，而后再组合回去；
	- select destr('123456 345 789 345',' ') 返回： 123456 345 789
6. 中国身份证有效性检测: **idcheck(列/字串,f)** 如果身份证有效返回true; (f=0 15/18位都算，f=1只算18位，f=2只算15位)
7. 身份证校验位生成: **idchecksum(列/字串)** 根据17位，生成最后一位校验位
8. 旧身份证转换为新的: **idconv(列/字串)** 将旧的15为身份证，自动转换为18为的（包括校验位计算）
9. 幂运算操作: **power(2,3)** 表示计算2^3; 
  - power(2,0.5) 计算2的平方根; power(2,1.0/3) 计算2的立方根,注意用1.0，而非1
10. 标准差计算: **std(2,3,4,5)** 用在数据库统计中，例如 select std(mM) from T1 ；计算一组数据的 标准差;
11. 列表索引选择: **slist('1,2,3,4,5',2)** 返回3，即将字符串用 , 分割, 而后选择第2个元素（0开头）
  - 如索引超过, 则返回最后一个元素; 可以用负值, 例如: slist('1,2,3,4,5',-2) 返回 4; 同样，超过范围，返回最前一个值；也可以 slist('apple,ibm',1)
12. 返回拼接字符串首 N 项: **ctop('string', 'split char', n)** 
	- ctop('1 2 3 4 5', ' ', 2) 将返回 '1 2';  ctop('1,2,3,4,5', ',', 3) 将返回 '1,2,3'
  - 当用 csum 将结果集聚合成一个字符串，若希望获取TopN项, 则可用这个功能，例如: ctop(csum(name||count(*)),' ',10), 这样就可实现对每个group by 数据, 只选取前面10个
13. 返回找到正则的数量: **regfn(',','1,2,3,4,5,6')** 返回5，表示找到5个逗号
14. 针对同一个传入变量，提供自增计数器，即当输入参数没有变化，每次调用返回值+1，直到输入参数变化，则从1再开始计算; 可用 select **cindex('@@_0_@@')** 来强制重置计数器；这个功能对于 group by 后选取分组 top N 项 很有价值；例如：
  - (!!! 注意：因为 cindex(N) as II ，而后用 where II< 判断，实际上是执行了两次，导致 cindex 执行了多次
	- select N,C,Dist,cindex(N) as II from (select N,max(C) as C, ID, count(*) as C1 from (select N, C, substr(USER_ID,1,4) as ID from USERBASE as T,(select substr(USER_NAME,1,1) as N, count(*) as C from USERBASE group by substr(USER_NAME,1,1) having C > 50) as T1 where length(USER_ID)=18 and substr(T.USER_NAME,1,1) = T1.N) group by N,ID order by C desc, C1 desc) as T , IDTYPE as I where T.ID = I.ID and II<21

### 5. 脚本支持
- 5.1 脚本概述
  - 脚本功能让你可以将系列命令放到一个 脚本文件 , 在需要的时候进行批量执行;
  - 使用 **python3 Qsqlite 脚本文件名** 来执行脚本文件;
  - 脚本文件中, 如果需要 注释 内容，可用类似 python 格式的 注释 方法
    - 用 # 进行注释
    - 用 ''' 注释内容 ''' 进行多行注释
- 5.2 结果输出到 html 功能
  - **html html文件名** 开启将输出内容输出到 html 文件, **chtml** 关闭 html 输出. (这样可在一个脚本中，一部分屏幕显示，另一部分输出到 html 文件，当遇到chtml的时候，会将文件关闭, 后面内容输出到屏幕)
  - 例子:
  ```sql
		# 打开数据库
		open test.db
		# 开启 html 文件输出功能
		html test.html
		echo ## 测试报表
		select * from demo where name like '%apple%' >[- ID:_@1_, Name:_@2_]
		echo ## 图标测试
		draw l select date, scorp from report 
		# 关闭 html 文件
		chtnl
		# 这部分内容将输出到屏幕
		select * from test
  ```
  - 可将某部分输出到一个文件(html file1 ... chtml), 另一部分输出到其它文件(html file2 ... chtml);
  - 输出到 html 文件功能，对于所有的图形操作 (draw) 的图片，会采用内嵌方式嵌入到 html 文件，因此只需要将 html 单一文件拷贝就可以自动包含图片;
- 5.3 **echo**信息输出
  - echo 会将后面的所有内容输出到 终端 或 html 文本中
  - 充分利用 echo 功能可美化 html 格式, 例如: 
    - 一个 echo 会直接输出一个空行
    - echo 后面可以跟一些 html 语句, 例如
  	- 也可以在 html 之后，用 echo 来输出样式，改变显示模式
		```html
			html test.html
			echo <style type="text/css">ul {list-style: square;} </style>
			echo # 测试报告
			echo ## 性能报告
			echo * 这是加黑的内容
			echo - 列表项目 001
			echo  - 列表子项目 001.001
			echo <h1>大标题</h1>
			echo <br>
			echo <a href="/list?test">Get List</a>
			chtml
		```
- 5.4 **loop/lend** 循环功能
  - loop / lend 循环功能可解决很多结果利用一个SQL语句无法实现的问题, 结合内存数据库中转, 可以实现更强大功能;
	- loop 指令后面可以是一个查询语句，或者是一个类似 Python 一样的列表（模拟SQL查询语句返回结果集）
	  - loop select mID, name from tab1 where mTime > 10 (这个查询语句会返回两个结果集 _^1_ -> mID, _^2_ -> name)
	  - loop [ (123,'name1',1.2), (345,'name2',2.3) ] (这个方式可以让我们手动定义循环结果，例如 _^1_ -> 123, _^2_ -> name1, _^3 -> 1.2)
	  - loop [ (i+1, i+2) for i in range(12) ]	可以利用这样的方式来构建循环（Python语法，因为通过eval解析）
	  - loop 中，其实还有一个隐含的参数 _^0_，这是结果集的行号，例如 select 返回的第一行是 1，第二行是2，或者[()]列表返回第一个是1，而后是2；
	- loop / lend 指令之间夹着的指令将会根据 loop 后面的 select 或 列表元素 的结果集多少, 执行多次;
	- 例子: 利用直接定义结果列表，每行只有一个结果，总共两行；用echo来显示内容 （技巧: _^_的替换可以在 >[] 里面用）
  ``` sql
		loop [ (333,), (666,) ]
		echo # _^0_  --  _^1_
		select * from tab1 where name like '%测试_^1_%' and id = _^0_ >[ 查询 %测试_^1_% 的结果：_@1_, _@2_ ]
		lend
  ```
  - loop / lend 支持嵌套功能，可以使用嵌套实现复杂功能，例如：
  ``` sql
		# loop 功能需要确保有数据库开启
		open :memory:
		# 第一层循环
		loop [ (i+1, ) for i in range(9) ]
			echo ==== _^1_ ====
			# 第二层循环
			loop [ (_^1_, i+1, _^1_*(i+1), ) for i in range(9)]
				echo _^1_ * _^2_ = _^3_
			lend
		lend
  ```
	- loop / lend 配合上 :memory: 内存数据库，能够解决很多复杂的查询需求. 例子: 按照日期统计两个参数，而后合并到一起显示；（结合 group by / max 来进行纵向合并）
  ```sql
		open :memory:
		create table T (gtime text , c integer, n integer)
		open db1
		loop select substr(mBTime,1,10) from tab1 where mTime > 10 group by substr(mBTime,1,10)
		copy :memory: T select '_^1_',count(*),0 from tab3 where xxx group by xxx
		copy :memory: T select '_^1_',0,count(*) from tab6 where xxx group by xxx
		open :memory:
		select gtime,max(c),max(n) from T group by gtime >[_@1_ 参数1: _@2_, 参数2:_@3_]
  ```

### 6. WebServer 支持 （单线程)
- 6.1 设置 Web 服务器
	- 在脚本文件中使用 **@webserver ip:port** 来启动 web 服务器; 脚本中带有 @webserver 则被判断为 Web 脚本, 程序会保持运行, 直到用户用 ctrl + c 退出, 或者终止进程
	- WebServer 只支持单线程, 只是为了更便利的用 Web 访问数据，而非为性能考虑
	- 在 开启服务器后，使用 open 语句打开数据库，以便后续页面可以访问数据库
- 6.2 添加 Web 页面 
	- 用 **@page url** 添加一个 页面/功能 描述, 在该语句下面则是标准的数据库操作脚本; 使用多个 @page 来配置多个页面功能
	- 浏览器 url 后面跟随的参数，在脚本里面被解析为 _#1_ _#2_ ... 模式. 例如 /user?apple&ipad&iphone, 则: _#1_ 为apple, _#2_ 为ipad, _#3_ 为iphone, 中间用 & 连接; 如果没有对应变量，则会使用 _#2_ 或 _#3_ 等替代.
	```sql
		# 开启 web 服务器, 访问地址: http://127.0.0.1:8080
		@webserver 127.0.0.1:8080	
		# 打开数据库文件
		open my.db

		# 定义页面 /user 的内容
		@page user
		echo ## 查询用户结果
		select * from user where name like '%_#1_%'
		draw l select date,record from urec where name like '%_#1_%'
		
		# 定义页面 /time 内容
		@page time
		echo <b> Time </b>
		select strftime('%Y-%m-%d %H:%M','now','localtime') >[Time is: _@1_]
	```
	- 而后就可以在浏览器中，http://127.0.0.1:8080/user?张三 来查询获得结果
	- 使用 ip:port/ 访问根目录, 可获得所有配置的 @page 列表; 如希望自己设置或不希望系统列出 @page 列表，可设置根目录
	```
		@page / 
		echo Welcome My Web Home.
	```
- 6.3 通过 **webinput** 实现 html <form> <input > 输入框操作指令
	- 使用 webinput url 提示内容1(宽度)(预设内容) 提示内容2(宽度)(预设内容) ~提交按钮内容; 例如:
		- webinput /query 姓名(6)() 地址(12)(地址要详细到房号) ~查询
	- 如希望将按钮布局采用竖向排列(每一行一个按钮), 则最后的 ~ 变更为 ^, 例如: 
		- webinput /query 姓名(6)() 地址(12)() ^查询
	- 如希望增加隐藏参数，则在 提示内容前面加上 _ 来表示, 例如: 
		- webinput /query 姓名(6)() 地址(12)() _类型()(123) ~查询
	- 按下提交按钮后, 会调用 url 指向的页面，参数会按顺序传递过去, 用 _#1_ _#2_ 等形式来顺序获取, 隐藏参数也是一样
	- 可将 webinput 放到 select * from table >[ webinput 姓名(6)(_@1_) 地址(12)(_@2_)... ] 实现默认内容填充
- 6.4 完整的 WebServer 演示脚本，可参考 Demo 目录下的 qweb.txt 脚本文件, 可以 python3 Qsqlite.py qweb.txt 运行，而后在浏览器输入 http://127.0.0.1:8080 访问.

### 7. 定时任务服务
- 该功能可根据脚本文件的配置, 定时执行对应脚本，将结果 保存到文件 或 通过邮件发送 出去
- 7.1 **@jobserver** 启动 定时任务服务器 
- 7.2 **@mail [1234567][12:20] [srv:port user pwd] [邮件标题] [mail地址]** 定时发送邮件任务
	- 所有结果以 html 格式发送邮件, 需提供: 邮件服务器信息、邮件标题、收件人列表(多个邮件地址用空格隔开)
- 7.3 **@job [1234567][12:20] [html文件名]** 定时执行任务并将结果输出到 html 文件
- 7.4 以上操作中, 文件名, 邮件标题 可以用 _@Date_ , _@Time_ 替代符，在执行时候，会被替换成当前日期, 时间
	- 例如: [outfile_@Date_-_@Time_.html] 或 邮件标题 [_@Date_日报表]
- 7.5 定时选择
	- 日期选择: [1234567] 表示每周7天(所有日期), [135] 表示 周1/3/5三天
	- [12:20] 表示对应日期的 12:20
	- 如果一天内需要设置多个时间，则可以设置多个 @mail 或 @job 来实现
- 例子:
```sql
	# 启动 Job Server
	@jobserver 

	# 指定 周1 - 周日, 每天 03:30 执行下面的脚本，并且保存到文件 out_日期.html 
	@job [0123456] [03:30] [out__@Date_.html]
	echo '测试服务'
	select 1+2+3

	# 指定 周日, 周三 00:03 执行下面脚本，并且发送邮件到 指定邮箱
	@mail [03] [00:03] [smtp.office365.com:587] [xxx@hotmail.com] [mail pwd] [日志分析 _@Date_ 测试 _@Time_] [xxx@me.com abcd@outlook.com]
	echo mail server 邮件
	select 1+2+3+4+5+6
```
- 7.6 完整的 JobServer 演示脚本，可参考 Demo 目录下的 qjob.txt 脚本文件, 请用编辑器打开该文件, 修改对应的邮件服务器,地址,密码等相关信息后, 用 python3 Qsqlite.py qjob.txt 运行.

### 8. WebServer & JobServer 后台运行
- 如果在 Linux 中后台运行，可以用: Python3 Qsqlite.py scrp.txt >>out.log & 来进行，或者 nohup Python3 Qsqlite.py scrp.txt &
- 如果不重定向输出，则可能会导致后台被中断执行!!

### 9. Python, iPython or Jupyter 
	- 在 Python 程序或 iPython notebook 中, 可以导入 Qsqlite 的库
```python
	# import Qexec
	from Qsqlite import Qexec
	script = '''
		open :memory:
		create table test (id text, name text)
		insert into test values('123','Apple')
		select * from test
	'''
	Qexec(script)
```

## 开发背景
- 2020 春节假期写了一个程序每隔一分钟收集公司在线用户数据保存到一个SQlite数据库；为交互分析这些数据并图形化展示，需要用Python代码来实现，每次新的分析需求还需调整代码，因此动手写一个工具，希望实现自动化；
- 最开始版本只是一个交互式工具，支持基本数据库操作，例如打开数据库、查看数据库结构、执行SQL查询、用Matplotlib绘制查询结果；
- 后来发现有一些操作需要不断地执行，因此增加脚本功能，可以把系列脚本保存到一个文件，而后直接执行这个脚本文件；
- 在使用过程中，不断有些功能无法满足，因此不断补充功能，例如：输出内容自定义、导入/导出csv文件、loop循环功能、内存临时数据库支持、结果输出为html文件、SQLite扩展的正则函数、MySQL支持、Web服务器、定时任务服务器等；

## 版本历史
- 2020/02/16   V0.1  First Version.
- 2020/04/25   V0.5  Add SQLite Ext function and export to HTML.
- 2020/04/28   V0.7  Add MySQL Support, include dump mysql to sqlite.
- 2020/05/14   V0.71 Fix Some MySQL Bug.
- 2020/07/05   V0.72 Fix draw l None data bug.
- 2020/07/15   V0.73 SQliteCopy Change fetchall() to fetchone(), use less memory.
- 2020/09/08   V0.74	
  - Add Qexec function, can using from Qsqlite import Qexec.
  - Add cmd History function l/la/l0/lxx.
- 2020/12/21   V0.75
  - Add MySQL info 1/2/3 Support.
  - Add import readline for Mac/Linux input history.
  - Add MySQL Server:port support.
- 2021/01/06   V0.80 Add WebServer Support. using @webserver @page config.
- 2021/01/28   V0.81 Add sub LOOP/LEND Support.
- 2021/05/30   V0.83 Add JobServer support job & email.
- 2021/09/03   V0.85 Add <form> <input> support for WebServer.
- 2021/10/20   V0.86 Fix a bug in regfind.
- 2022/02/25   V0.87 Add loadjson function.
- 2022/02/28   V0.88 Add draw scatter function.
- 2022/03/08   V0.89 BugFix and add ls cmd and optimize loadcsv/>csv function.

## sqlite 参考资料
- SQlite3 Doc
  - https://docs.python.org/zh-cn/3/library/sqlite3.html
  - https://cloud.tencent.com/developer/section/1367013 (CN)
- SQlite3 System Function Ref
	- https://www.sqlite.org/lang_corefunc.html
- SQlit Ext
  - https://wellsr.com/python/create-scalar-and-aggregate-functions-for-python-sqlite/
  - https://charlesleifer.com/blog/going-fast-with-sqlite-and-python/
- Regex Doc
  - https://segmentfault.com/a/1190000018622193
- matplotlib: (CN)
  - https://zhuanlan.zhihu.com/p/33270402







## 使用技巧

	## 如果需要在 jupyter 或程序中使用，可以用 from Qsqlite import Qexec ；而后 Qexec(cmds) 来调用，而cmds 则可以是一个带换行符的字符串，包括系列的命令


	## 将数据库 A 的某些表，复制到一个新的数据库（已经存在的也可以）：
	- open A -> info 列出A数据库的所有表结构，包括创建表的语句；
	- open B (如果该表不存在，会提示创建)，而后将上面需要的表创建语句复制下来，而后执行；这样就会在B数据库上创建了新的表；
	- open A 切换回A数据库，(!!!请千万记住，用 db 命令来确认是否已经切换到 源数据库 A)
	- copy B tab1 select * from tab1 命令将 A 数据库的 tab1 表内容，复制到 B 数据库 tab1 表 （用 insert 插入的方式）; 如果你只需要插入部分记录，则可以用 where 条件；

	## 利用内存数据库作为临时空间，进行复杂的查询操作（因为有些操作一个SQL语句实现不了，或者用join速度慢）
	- open :memory: 会打开内存数据库，而且这个数据库在程序退出前会一直保留，就算你切换到其它数据库；
	- 一般做法，在 :memory: 数据库创建对应的表作为最终、临时结果保存地；而后切换到其它数据库，将数据结果用 copy :memory: tab1 select ... 来保存到临时表；
	- 而后再回到内存数据库，对数据进行筛选、合并处理，最终用这些数据进行输出、绘图等；
	- 例子：利用内存数据库作为缓存机制，绘制7日均线、昨日数据、当天数据对比图 （绕开了低效率的 left outer join)
		1.先在内存数据库中构建对应的表
		open :memory:
		create table Draw (time text,week real,last real,today real)
		create table Draw01 (time text,t real)
		create table Draw02 (time text,t real)
		2.而后将数据库中 对应数据复制到 内存表中 
		open Miatable.db
		3.构造7天均线
		copy :memory: Draw select substr(gtime,12,5),avg(uCNT),0,0 from Miaload where datetime(gtime) between datetime('now','localtime','start of day','-7 days') and datetime('now','localtime','start of day') group by substr(gtime,12,5)
		4.构造昨天数据
		copy :memory: Draw01 select substr(gtime,12,5) as t,avg(uCNT) from Miaload where datetime(gtime) between datetime('now','localtime','start of day','-1 days') and datetime('now','localtime','start of day') group by substr(gtime,12,5)
		5.构造今天数据
		copy :memory: Draw02 select substr(gtime,12,5) as t,uCnt from Miaload where datetime(gtime) between datetime('now','localtime','start of day') and datetime('now','localtime') group by substr(gtime,12,5)
		6.回到内存数据库
		open :memory:
		7.进行数据合并
		update Draw set last = (select t from Draw01 where Draw.time = Draw01.time)
		update Draw set today = (select t from Draw02 where Draw.time = Draw02.time)
		8.联合绘制
		draw l select * from Draw

	## MySQL 数据库支持
	- 首先设置 MySQL 数据库，用 mysql dbname server user password 来创建一个MySQL数据库连接，例如: mysql test 127.0.0.1 root pwd
	- 如果 MySQL 并非默认端口号，则可以指定 mysql test 127.0.0.1:3308 root pwd 
	- 而后就可以用 open #test# 来打开这个数据库 ；再次切换到其它数据库，切换回来，也只需要这样就可以了；
	- 你可以用 mysql 指令设置多个 MySQL 的数据库，而后用 open 来切换就可以了；
	- 和 SQLite 一样，也支持基本数据库操作、copy / loadcsv (最好先自己创建表，不然自动创建可能导致数据类型不匹配) / >csv 等
	- 利用 info 功能，可以将 MySQL 数据库的表列出，并且自动构建出了对应 SQLite 创建需要的语句；
	- 可以利用info的数据，快速在 SQLite里创建表，用 copy 指令 拷贝数据；也可反过来，将SQlite数据复制到 MySQL 上；
	- 可以利用 dump #mysqldb# sqlitedb 将一个MySQL数据库复制到SQLite，包括所有数据；或者 dump #mysql# :memory: 复制到内存
	- info 0 列出兼容SQLite的创建语句的表结构； info 1 列出所有索引信息 
	- info 2 列出所有 MySQL 表（包括表的记录数、所占空间大小）； info 3 列出 带有注释信息的 表结构 
	- MySQL 一些常用命令
		- show databases   列出数据库服务器上的所有数据库
		- show tables      列出当前数据库的所有表
		- show keys from tb  列出某个表所包含的索引
	- MySQL 性能调优指令
		- explain / show profiles / set profiling = 1 / show profile for query xx

	## 充分利用 loop / lend 循环功能，这个功能解决了很多结果利用一个SQL语句无法实现，结合内存数据库中转，可以实现更强大功能
	- loop 指令后面可以是一个查询语句，或者是一个类似Python一样的列表（模拟SQL查询语句返回结果集）
	- loop select mID, name from tab1 where mTime > 10 (这个查询语句会返回两个结果集 _^1_ -> mID, _^2_ -> name)
	- loop [(123,'name1',1.2),(345,'name2',2.3)] (这个方式可以让我们手动定义循环结果，例如 _^1_ -> 123, _^2_ -> name1, _^3 -> 1.2)
	- loop [(i+1,i+2) for i in range(12)]	**可以利用这样的方式来构建循环（Python语法，因为通过eval解析）
	- loop 中，其实还有一个隐含的参数 _^0_，这是结果集的行号，例如 select 返回的第一行是 1，第二行是2，或者[()]列表返回第一个是1，而后是2；
	- loop / lend 指令之间夹着的指令将会根据 loop 后面的 select 或 列表元素 的结果集多少，执行多次；
	- 例子： 利用直接定义结果列表，每行只有一个结果，总共两行；用echo来显示内容 （技巧: _^_的替换可以在 >[] 里面用）
			loop [(333,),(666,)]
			echo # _^0  --  _^1
			select * from tab1 where name like '%测试_^1_%' and id = _^0_ >[ 查询 %测试_^1_% 的结果：_@1_, _@2_ ]
			lend
	- loop / lend 配合上 :memory: 内存数据库，能够解决很多复杂的查询需求；
	- 例子：按照日期统计两个参数，而后合并到一起显示；（结合 group by / max 来进行纵向合并）
			open :memory:
			create table T (gtime text , c integer, n integer)
			open db1
			loop select substr(mBTime,1,10) from tab1 where mTime > 10 group by substr(mBTime,1,10)
			copy :memory: T select '_^1_',count(*),0 from tab3 where xxx group by xxx
			copy :memory: T select '_^1_',0,count(*) from tab6 where xxx group by xxx
			open :memory:
			select gtime,max(c),max(n) from T group by gtime >[_@1_ 参数1: _@2_, 参数2:_@3_]
	- loop / lend 支持嵌套功能，可以使用嵌套实现复杂功能，例如：
			loop [ (i+1, ) for i in range(9) ]
				echo ==== _^1_ ====
				loop [ (_^1_, i+1, _^1_*(i+1), ) for i in range(9)]
					echo _^1_ * _^2_ = _^3_
				lend
			lend

	## 对于输出结果的处理
	- 默认select查询结果会自动列出，不需要特殊处理，除非你希望格式化输出
	- select 查询的结果，如果需要格式化输出，可以在语句最后加上 >[] 来定义输出格式，例如： select * from tab1 >[- _@0_, 名字：_@1_, 年龄:_@2_, 身高:_@3_ ]；这里 _@0_表示顺序号，_@1_表示返回结果的第一列
	- 或者输出到 csv 文件，可以在 语句后加上： >csv 文件名.csv   (这样查询结果将会保存到指定的csv文件，注意：字段中的英文逗号会替换成中文逗号); 如果希望输出的csv不包含表头信息，则使用 >csv filename.csv 0 来关闭

	## 输出到 html 文件
	- 可以用 html 文件名.html 开启，当需要关闭的时候，用 chtml 来关闭 （这样可以在一个脚本中，一部分屏幕显示，另一部分输出到html文件中，当遇到chtml的时候，会将文件关闭；并且后面的内容输出到屏幕；
	- 可以将某部分输出到一个文件(html file1 ... chtml)，另一部分输出到其它文件(html file2 ... chtml)；
	- 输出到 html 文件，会支持 markdown 的两个主要标记， # / -/* (对于#/##/###...会替换成<h1>...)；对于 -/* 会构造 <ul><li> 列表，对于*会将星号加黑显示，以区别；
	- 输出到 html 文件功能，对于所有的图形操作 (draw) 的图片，会采用内嵌方式嵌入到 html 文件，因此只需要将 html 单一文件拷贝就可以自动包含图片；
	- 充分利用 echo 功能来 美化格式，例如：一个 echo 会直接输出一个空行; echo 后面可以跟一些 html 语句，例如:
```html
	 echo <h1>大标题</h1>  或者 echo <br> 等等 
```
	- 也可以在 html 之后，用 echo 来输出样式，改变显示模式：echo <style type="text/css">ul {list-style: square;} </style>

	## 利用 loadcsv 来将 csv 文件导入到数据库表中
	- loadcsv csv文件名 tab1 ，将会读取csv文件，而后根据csv文件的列数，自动创建名字为 tab1的表（如果表已经存在，则不会创建）；
	- 而后数据将会以 insert 的方式插入到表中；这样你可以将数据不断从不同csv文件导入到同一个表；
	- 如果csv文件第一行是表头，希望过滤掉，则在最后加上参数1，loadcsv file.csv tab1 1
	- 数据库表导出为csv，则使用select * from tb1 >csv 文件名 ；如果希望导出不带表头，则 文件名后加上参数 0

	## 利用 loadjson 将 json 文件导入数据库表中
	- loadjson json文件名 tab1 json_item 将会读取 json 文件, 根据 json 的数据内容，创建表，并且将数据导入；
	- 因为很多JSON文件, 我们需要的数据在某个字段中，因此需要设定 json_item, 从 该 字段 获取数据, 例如:
		- JSON文件:  {'retval':0, 'results':'[{'name':'apple','age':123}, {'name':'ibm','age':234}]'}) 
		- loadjson demo1.json demo1 results   (表示我们只需要 results 的数据写入数据库)

	## 绘制图表功能 (折线图、分布图、箱型图、散点图；并且支持对数坐标)
	- draw l 折线图可以绘制一组或多组数据，如果只有一行数据（select a from tb1），则系统会自动根据结果集数，产生对应的X轴数据(1-N)；如果是多个数据，则第一行数据作为 X 轴标记显示（一般是日期/时间），其它作为 Y 轴 (select x_lable,col1,col2 from tab1)；
	- draw l2 表示希望X轴的数据不是系统产生的0-N的等比例数据；而是直接用select结果第一项；例如：draw l2 select height,weight from tb1
	- draw ll 表示对Y轴进行对数处理 ； ll2 表示进行X-Y轴进行双对数处理；
	- draw h 表示绘制分布图，只取结果集的第一列；draw hx 表示对 分布图的 x轴进行对数处理; draw hy 表示对 分布图的 y轴进行对数处理; draw hl 表示对x-y轴双对数处理
	- draw v 表示绘制小提琴箱型分布图，只取结果集第一列；
	- draw ls 可以将多个数据列，绘制在不同的子图上，并列排放；
	- 多图绘制功能，能够将不同的类型图，通过子图模式，绘制在一个输出图片里面，使用 draw xxx; draw xxx;draw xxx 进行
	- 	draw l select a,b,c from t1; draw hl select a from t2; draw ll select a,b from t3; draw v select a from t4
	- draw s 绘制散点图：
		- 只给Y坐标 draw s select y from table / 只给坐标: draw s select x,y from table / 给坐标和点尺寸: draw s select x,y,size from table / 给坐标、尺寸、颜色: draw s select x,y,size,color from table

	## SQLite自定义函数
	- 1.行字符串累加： csum(列名)，就像SQLite的默认sum()函数，sum()累加每列的值，返回总数；而csum()将每列作为字符串拼接起来；
	-  例如： select mID,csum(nName),count(*) from T group by mID 或者 select csum(nName||'-'||nOrg) ...
	- 2.正则判断功能：regexp(正则表达式,列/字串)  用于判断某个列的内容是否符合正则表达式；返回结果是 布尔类型（True/False)
	-   例如：select * from tab1 where regexp('^[1]([3-9])[0-9]{9}$',mobile) / or = false
	- 3.正则提取功能：regfind(正则表达式,列/字串,n) 用于利用正则从列/字串提取内容, n=1 表示获取第1个结果, 2表示获取第2个
	-  n = 0 表示获取所有结果，结果之间用空格分割； 
	-  例如：select regfind('1(.*?)2','1hello2 1good2',1)    n=1，返回hello，n=2返回good  n=0返回 hello good
	- 4.正则替换功能：regsub(正则表达式,替换串,列/字串)  利用正则匹配，替换字符串
	-  regsub('([\d]{3})','#\1#','Test000-372')  -> Test#000#-#372# 
	- 5.字符串单元去重： destr(列/字串,分隔符) 用于将分隔符连接的字串，分割后，去重元素，而后再组合回去；
	-  例如：select destr('123456 345 789 345',' ') 返回： 123456 345 789
	- 6.身份证有效性检测：idcheck(列/字串,f) 如果身份证有效返回true; (f=0 15/18位都算，f=1只算18位，f=2只算15位)
	- 7.身份证校验位生成： idchecksum(列/字串) 根据17位，生成最后一位校验位
	- 8.旧身份证转换为新的: idconv(列/字串) 将旧的15为身份证，自动转换为18为的（包括校验位计算）
	- 9.幂运算操作：   power(2,3) ，表示计算2^3；power(2,0.5) 计算2的平方根； power(2,1.0/3) 计算2的立方根,注意用1.0，而非1
	- 10. 标准差计算： std(2,3,4,5)，或者用在数据库统计中，例如 select std(mM) from T1 ；计算一组数据的 标准差 ；
	- 11. 列表索引选择：  slist('1,2,3,4,5',2) 返回3，即将字符串用,分割，而后选择第2个元素（0开头），如果索引超过，则返回最后一个元素；可以用负值；例如： slist('1,2,3,4,5',-2) 返回 4；同样，超过范围，返回最前一个值；也可以 slist('apple,ibm',1)
	- 12. 返回拼接字符串首 N 项：ctop('1,2,3,4,5',' ',2) 返回 1,2 ; 当我们用 csum 将结果集聚合成一个字符串，我们只希望获取TopN项，则可以用这个功能，例如: ctop(csum(name||count(*)),' ',10) ，这样就可实现对每个group by 数据，只选取前面10个
	- 13. 返回找到正则的数量: regfn(',','1,2,3,4,5,6') 返回5，表示找到5个逗号
	- 14. 针对同一个传入变量，提供自增计数器，即当输入参数没有变化，每次调用返回值+1，直到输入参数变化，则从1再开始计算；可以用 select cindex('@@_0_@@') 来强制重置计数器；这个功能对于 group by 后选取分组 top N 项 很有价值；例如：
			（!!! 注意：因为 cindex(N) as II ，而后用 where II< 判断，实际上是执行了两次，导致 cindex 执行了多次
			select N,C,Dist,cindex(N) as II from (select N,max(C) as C, ID, count(*) as C1 from (select N, C, substr(USER_ID,1,4) as ID from USERBASE as T,(select substr(USER_NAME,1,1) as N, count(*) as C from USERBASE group by substr(USER_NAME,1,1) having C > 50) as T1 where length(USER_ID)=18 and substr(T.USER_NAME,1,1) = T1.N) group by N,ID order by C desc, C1 desc) as T , IDTYPE as I where T.ID = I.ID and II<21

	## 关于正则表达式
	- 开头^ 结尾$ [^[\d]{3}$] 表示匹配三个数字的内容 '123' ，如果是 ' 123' 或 '123 ' 都不行
	- 匹配任何一个字符 . (例如数字、字母等）；可以用 .* 表示匹配所有东西（包括空串）; .+表示匹配最少一个或任意内容
	- \d 任意数字 \w 任意字符 \s 任意空格、tab、换行符  \b 单词的开头或结尾匹配 
	- 取反 ^ ，例如：n[^e] 这意味着字符n接下来的字符是除了e之外所有的字符; ^\d 表示非数字 ^\w表示大写字符 ^\b 表示非开头结尾
	- 匹配1个或多个 + ；匹配0个或多个 *;  指定区间：{} {6} 6次、{3,} 3次或以上 {3,8} 3-次；
	- 可选匹配(0次或1次) ? ，例如 ab?c 可以匹配 abc，或者ac，即 b可以出现或不出现
	- 分组用 ()，如果不需要提取分组内容，用(?: ) ；例如： re.findall('(?:^| |\*)([2-8][\d]{6})','3234567 8343432') 第一个分组是希望匹配空格或顶头，并且不希望提取内容

	## SQLite的一些小技巧
	- 创建表的时候，默认会自动添加一个 rowid 字段，并且构建以此为 pk 的内部索引
		- 创建表的时候，可以考虑自己设置 pk, 并将 rowid 取消, 这样会降低存储空间，提升查询效率
		- 例如: create table test(id text primary key, name text, year int) without rowid
	- 对数据库存储空间优化（例如删除过表，释放空间）： VACUUM
	- SQlite的join的外连接功能，只支持left outer join （第一个表的要素全出现，其它根据条件，否则为None)
	-  其实很多复杂场景、需求可以用临时表来实现（用 :memory: 数据库的临时表实现）
	-  select date,code1,code2 from T1 left outer join (select date as d1 from T1 where xxx) on date=d1 left outer join (select d3,code2 from T2 where xxx) on date=d3
	- 利用每一个表，系统分配的 rowid 来进行操作，例如删除重复的内容
			delete from Roominfo where rowid not in (select min(rowid) from Roominfo group by mID,mBTime)
	- select last_insert_rowid() 获取最后一次 insert 的最后一个 rowid
	- SQlite 内置了很多有用的函数,例如
		- iif(条件,条件成立,条件不成立), 例如: iif(c='CN', 'r', iif(c='US','b', iif(c='JP','c','def')))
		- coalesce(字段1, 字段2, 字段3 ...) 将返回 第一个不为空的字段，例如 coalesce(t1,t2,t3, 1)
	- 充分利用 SQLite 强大的时间操作函数（如果不加 localtime 则时区不正确）
			select strftime('%Y-%m-%d %H:%M:%S','now','localtime')
			select strftime('%Y-%m-%d 12:00:00', 'now', 'start of month')
			select strftime('%Y-%m-%d %H:%M:%S','now','-7 days', 'weekday 5')
			datetime(gtime) between datetime('now','localtime','start of day','-7 days') and datetime('now','localtime','start of day')
			strftime('%W','2020-03-05') -> 09 表示该日期是本年度的第几周  
				%w 表示星期几(周日为0)    %j 表示1年中的第几天   %s 表示从 1970-1-1日开始的第几秒
			select date()>'2020-03-01' 获取当前日期； select datetime() 获取当前日期时间   select time() 获取当前时间
	- SQLite随机获取数据（随机排序功能 + Limit)
			select * from TEST order by random() limit 2
	- 利用 Explain 来查看 SQLite 的执行策略，例如 explain select mCID from Roominfo where mM > 15
	- 可以用 dinfo on ，将系统的调试信息输出打开，这样在执行 SQL 命令的时候，会输出操作耗时、列信息；

	## WebServer 支持 （单线程)
	- 该功能能够启动一个 Web 服务器，配置对应的路径和参数，让用户可以用浏览器来访问数据
	- 该 WebServer 只支持单线程，只是为了更便利的用 Web 访问数据，而非为性能考虑；
	- 编写一个脚本文件，脚本文件包括 @webserver ip:port 来启动 web 服务器；当脚本中带有 @webserver 后，则被判断为 Web 脚本，程序会保持运行，直到用户用 ctrl + c 退出，或者终止进程；
	- 而后用 @page url 作为每一个具体功能的描述；在该语句下面则是标准的数据库操作脚本
	- url 后面跟随的参数，在脚本里面被解析为 _#1_ _#2_ ... 模式；例如 /user?apple ipad iphone _#1_ 为 apple _#2_ 为ipad, _#3_ 为 iphone ,中间用空格分开；如果没有对应变量，则会使用 _#2_ 或 _#3_ 等替代
	- 例如： @webserver 127.0.0.1:8080	
			# 访问地址: http://127.0.0.1:8080/user?测试用户 
			@page user
			open my.db
			echo ## 查询用户结果
			select * from user where name like '%_#1_%'
			draw l select date,record from urec where name like '%_#1_%'
			# 访问地址: http://127.0.0.1:8080/time 
			@page time
			echo <b> Time </b>
			select strftime('%Y-%m-%d %H:%M','now','localtime') >[Time is: _@1_]			
		而后就可以在浏览器中，用 /user?张三 来查询获得结果；
	- 可以使用多个 @page 来配置多个页面功能；但是每个页面都请加上 open 语句；当使用内存数据库的时候，注意用 drop 删除记录，以避免多个访问对同一内存表的重复插入等问题；
	- 使用 ip:port/ 访问根目录，能够获得所有配置的 url 列表；如果希望自己设置或者不希望系统列出 url 列表，可以自己设置根目录操作： @page / 来设置，例如:
			@page / 
			echo 
	- 提供 html <form> <input > 输入框操作指令 webinput 
		- 使用 webinput url 提示内容1(宽度)(预设内容) 提示内容2(宽度)(预设内容) ~提交按钮内容 ；例如： 
			- webinput /query 姓名(6)() 地址(12)(地址要详细到房号) ~查询   ==> 
			- 如果希望将按钮布局采用竖向排列（每一行一个按钮），则最后的 ~ 变更为 ^，例如：webinput /query 姓名(6)() 地址(12)() ^查询
			- 如果希望带隐藏参数，则在 提示内容前面加上 _ 来表示，而这个时候()里面的值就是传递的值，例如：webinput /query 姓名(6) 地址(12) _类型(123) ~查询
			- 按下对应按钮后，会调用 url 指向的页面，并且参数会按照顺序传递过去，用 _#1_ _#2_ 等形式来按顺序获取，隐藏参数也是一样
			- 可以将 webinput 放到 select * from table >[ webinput 姓名(6)(_@1_) ... ] 来实现默认内容填充

	## 定时 任务 服务
	- 该功能 能够根据脚本文件的配置，定时执行对应的脚本，而后保存到文件，或者直接邮件发送出去；
	- 1. 启动 定时任务服务器 
		- @jobserver
	- 2. 定时发送邮件任务 ，所有结果以 html 格式发送邮件；需要提供：邮件服务器、邮件标题、收件人列表
		- @mail [1234567][12:20] [srv:port user pwd] [邮件标题 _@Date_] mail@hotmail.com mail2@to.com
	- 3. 定时执行任务 (而后将所有输出 以html 格式保存到指定文件)
		- @job [1234567][12:20] [outfile_@Date_ _@Time_.html]
	- 4. 文件名，邮件标题 可以用 _@Date_ , _@Time_ 替代符，在执行时候，会被替换成当前日期，时间
	- 例如：
		@jobserver 

		# 指定 周1-周日，每天 03:30 执行下面的脚本，并且保存到文件 out_日期.html 
		@job [0123456] [03:30] [out__@Date_.html]
		echo '测试服务'
		select 1+2+3

		# 指定 周日，周三 00:03 执行下面脚本，并且发送邮件到 指定邮箱
		@mail [03] [00:03] [smtp.office365.com:587] [xxx@hotmail.com] [mail pwd] [日志分析 _@Date_ 测试 _@Time_] [xxx@me.com abcd@outlook.com]
		echo mail server 邮件
		select 1+2+3+4+5+6
	
	## WebServer & JobServer 后台运行
	- 如果在 Linux 中后台运行，可以用: Python3 Qsqlite.py scrp.txt >>out.log & 来进行，或者 nohup Python3 Qsqlite.py scrp.txt &
	- 如果不重定向输出，这可能会导致后台被中断执行


	





