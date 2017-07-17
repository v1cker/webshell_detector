#!/usr/bin/env python

max_file_size = 102400 * 3

rule_hit = {}

file_match_rule = {}

tencent_webshell_rule_jsp = (('str_pattern', 0, 1001, '\\bJFolder|\\bwebshell|\\bvonloesch\\.de|reDuh\\.jsp|QQ:179189585|JSP\\s*\xe9\x8f\x82\xe5\x9b\xa6\xe6\xac\xa2\xe7\xbb\xa0\xef\xbc\x84\xe6\x82\x8a\xe9\x8d\xa3\xe2\x96\x85\\bJSPSpy|\\bKJ021320', 0), ('exec_cmd', 1, 3001, '(?:(?:java\\.lang\\.)?Runtime)?\\s*(\\w+)\\s*=\\s*(?:java\\.lang\\.)?Runtime\\.getRuntime\\(\\)[\\s\\S]*\\1\\.exec\\(.*?\\)', 0), ('exec_cmd2', 1, 3002, 'new\\s*(java\\.io\\.)?ProcessBuilder\\(.*?\\)', 0), ('browse_file', 1, 5001, '(\\.(listFiles|list|listRoots)\\s*\\(.+\\.(readLine|read)\\s*\\(.+\\.write\\s*\\()|(\\.(readLine|read)\\s*\\(.+\\.write\\s*\\(.+\\.(listFiles|list|listRoots)\\s*\\()', 1), ('create_file', 0, 5002, 'new\\s*(java\\.io\\.)?(FileOutputStream|PrintWriter|FileWriter|RandomAccessFile)\\(.*?\\)', 0), ('upload_file', 0, 5003, 'new\\s*((java\\.io\\.)?ServletFileUpload|(com\\.jspsmart\\.upload\\.)?SmartUpload)\\(\\)', 0), ('net_socket', 0, 7001, 'new\\s*(java\\.net\\.)?ServerSocket\\(.*?\\)', 0), ('net_socket2', 0, 7002, 'new\\s*(java\\.net\\.)?Socket\\(.*?\\)', 0), ('net_socket3', 0, 7003, 'new\\s*(java\\.net\\.)?InetSocketAddress\\(.*?\\)', 0), ('http_connect', 0, 7004, '(\\w+)\\s*=\\s*new\\s*(java\\.net\\.)?URL\\(.*?\\)[\\s\\S]*\\1\\.openConnection\\(\\)', 0), ('java_command', 0, 12101, 'Runtime\\.getRuntime\\(\\)\\.exec', 0), ('java_unicode', 0, 12102, '(\\\\u00\\w\\w){3,}', 0), ('java_class_invoke', 0, 12103, '\\.getMethod\\(.*?\\.invoke', 0), ('java_class_invoke2', 0, 12104, '(?:(?:java\\.lang\\.reflect\\.)?Method)?\\s*(\\w+)\\s*=\\s*.*\\.getMethod\\([\\s\\S]*\\1\\.invoke\\(.*?\\)', 0), ('java_url_loader', 0, 12105, 'java\\.net\\.URLClassLoader', 0), ('sql_connect', 0, 12301, '(java\\.sql\\.)?DriverManager\\.(getConnection|registerDriver)\\(.*?\\)', 0), ('sql_query', 0, 12302, '(ResultSet)?\\s*\\w+\\s*=\\s*\\w+\\.executeQuery\\(.*?\\)', 0), ('jdbc_drivers', 0, 12303, 'COM\\.ibm\\.db2\\.jdbc\\.app\\.DB2Driver|COM\\.ibm\\.db2\\.jdbc\\.DB2XADataSource|COM\\.ibm\\.db2\\.jdbc\\.net\\.DB2Driver|com\\.informix\\.jdbc\\.IfxDriver|com\\.informix\\.jdbcx\\.IfxXADataSource|org\\.apache\\.derby\\.jdbc\\.ClientDriver|com\\.microsoft\\.sqlserver\\.jdbc\\.SQLServerDriver|com\\.microsoft\\.jdbc\\.sqlserver\\.SQLServerDriver|com\\.mysql\\.jdbc\\.Driver|org\\.gjt\\.mm\\.mysql\\.Driver|oracle\\.jdbc\\.driver\\.OracleDriver|oracle\\.jdbc\\.xa\\.client\\.OracleXADataSource|oracle\\.jdbc\\.driver\\.OracleDriver|oracle\\.jdbc\\.xa\\.client\\.OracleXADataSource|com\\.tongweb\\.jdbc\\.OracleDriverWrapper|org\\.postgresql\\.Driver|com\\.sybase\\.jdbc\\.SybDriver|com\\.sybase\\.jdbc2\\.jdbc\\.SybXADataSource|org\\.hsqldb\\.jdbcDriver|com\\.sybase\\.jdbc3\\.jdbc\\.SybDriver|com\\.kingbase\\.Driver|dm\\.jdbc\\.driver\\.DmDriver', 0))

tencent_webshell_rule_php = (('common_webshell1', 0, 10101, '(?i)[\\r\\n;/\\*]+\\s*\\b(include|require)(_once)?\\b[\\s\\(]*[\'"][^\\n\'"]{1,100}((\\.(jpg|png|txt|jpeg|log|tmp|db|cache)|\\_(tmp|log))|((http|https|file|php|data|ftp)\\://.{0,25}))[\'"][\\s\\)]*[\\r\\n;/\\*]+', 0), ('common_webshell2', 0, 10102, '(?i)(?<!->)\\b(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\b[/*\\s]*\\(+[/*\\s]*((\\$_(GET|POST|REQUEST|COOKIE).{0,25})|(base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]*(\\$_(GET|POST|REQUEST|COOKIE).{0,25}))', 0), ('common_webshell3', 0, 10103, '(?i)\\$\\s*(\\w+)\\s*=[\\s\\(\\{]*(\\$_(GET|POST|REQUEST|COOKIE).{0,25});[\\s\\S]{0,200}(?<!\\>)\\b(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\b[/*\\s]*\\(+[\\s"/*]*(\\$\\s*\\1|((base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\("]*\\$\\s*\\1))', 0), ('common_webshell4', 0, 10104, '(?i)(preg_replace|preg_filter)[/*\\s]*\\(+[/*\\s]*((\\$_(GET|POST|REQUEST|COOKIE).{0,25})|[^,]{0,250}chr[\\s\\(](101|0x65|0145|\\d+)[^,]{0,25}\\s*|[\'"]\\s*(([^\\s])[^,]{0,20}\\7[\'"]*|[\\(\\}\\[].{0,20}[\\(\\}\\]])\\w*e\\w*[\'"])\\s*,([^\\),]*(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)|((\\$_(GET|POST|REQUEST|COOKIE).{0,25})))', 0), ('common_webshell5', 0, 10105, '(?i)\\$\\s*(\\w+)\\s*=\\s*((\\$_(GET|POST|REQUEST|COOKIE).{0,25})|[^;]*chr[\\s\\(]*(101|0x65|0145|\\d+)|[\'"](/[^/]*/|\\|[^\\|]*\\||\\\\\'[^\']*\')\\w{0,5}e\\w{0,5}[\'"])[\\s\\S]{0,1000}(preg_replace|preg_filter)[/*\\s]*\\([/*\\s]*\\$\\s*\\1.{0,30}(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)', 0), ('common_webshell6', 0, 10106, '(?i)\\$\\s*(\\w+)\\s*=\\s*(\\$_(GET|POST|REQUEST|COOKIE).{0,25})[\\s\\S]{0,1000}(preg_replace|preg_filter)[/*\\s]*\\(+[/*\\s]*((\\$_(GET|POST|REQUEST|COOKIE).{0,25})|[^,]{0,250}chr[\\s\\(](101|0x65|0145|\\d+)[^,]{0,25}\\s*|[\'"]\\s*(([^\\s])[^,]{0,20}\\10|[\\(\\}\\[].{0,20}[\\(\\}\\]])\\w*e\\w*[\'"])\\s*,([^\\)]*(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)|\\s*\\$\\1)', 0), ('common_webshell7', 0, 10107, '(?i)(array_map|call_user_func|call_user_func_array|new\\s*ReflectionFunction|register_shutdown_function|register_tick_function|new\\s*ArrayObject[\\s\\S]*->u[ak]sort)\\s*\\(+\\s*([\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec|[^\'"]*\\\\x).{0,200}|(\\$_(GET|POST|REQUEST|COOKIE)\\[[^,;\\)]{0,250},[^;\\),]{0,50}\\$[^;\\),]{0,50}\\)))', 0), ('common_webshell8', 0, 10108, '(?i)\\$\\s*(\\w+)\\s*=[\\s\\(\\{]*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|[\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec))[\\s\\S]{0,200}(?<!\\>)\\b(array_map|call_user_func|call_user_func_array|new\\s*ReflectionFunction|register_shutdown_function|register_tick_function|new\\s*ArrayObject[\\s\\S]*->u[ak]sort)\\b\\s*\\(+\\s*(\\$\\s*\\1|((base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]*\\$\\s*\\1))[^,;]*,[^;\\)]{0,50}\\$[^;\\)]{0,50}\\)', 0), ('common_webshell9', 0, 10109, '(?i)((array_filter|array_reduce|array_diff_ukey|array_udiff|array_walk|uasort|uksort|usort|new\\s*SQLite3[\\s\\S]*->\\s*createFunction)\\s*\\(+\\s*.{1,100}|PDO::FETCH_FUNC\\s*),\\s*([\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\s*[\'"]|(base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]+.{1,25}|(\\$_(GET|POST|REQUEST|COOKIE).{0,25}))\\s*\\)', 0), ('common_webshell10', 0, 10110, '(?i)\\$\\s*(\\w+)\\s*=[\\s\\(\\{]*((\\$_(GET|POST|REQUEST|COOKIE).{0,25})|[\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec|[^,;]*?\\\\x|[^,;]*?[\'"]\\s*\\.\\s*[\'"]))[\\s\\S]{0,1000}(?<!\\>)((array_filter|array_reduce|array_diff_ukey|array_udiff|array_walk|uasort|uksort|usort|new\\s*SQLite3[\\s\\S]*->\\s*createFunction)\\s*\\(+[^,]*\\$[^,]*|PDO::FETCH_FUNC\\s*),\\s*(\\$\\s*\\1\\s*\\)|((base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]*\\$\\s*\\1))', 0), ('common_webshell11', 0, 10111, '(?i)\\$(\\w*)\\s*=\\s*\\bcreate_function\\b\\s*\\(+\\s*[^;\\n\\r\\)]{1,100},\\s*([\'"]\\s*[^;\\n\\r\\)]{0,100}(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|poc_open|pcntl_exec).{1,600}\\s*[\'"]|[^,]{0,100}(\\$_(GET|POST|REQUEST|COOKIE|SERVER).{1,})|[^,\\n\\r\\)]{0,100}file_get_contents.{1,})\\s*\\)[\\s\\S]+\\$\\1\\s*\\([^\\)]*\\)', 0), ('common_webshell12', 0, 10112, '(?i)\\$(\\w*)\\s*=\\s*\\bcreate_function\\b\\s*\\([^;]*;[\\s\\S]*\\$\\1\\s*\\([^\\)]*([\'"]\\s*[^;\\n\\r\\)]{0,100}(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|poc_open|pcntl_exec).{1,600}\\s*[\'"]|[^;\\n\\r]{0,100}(\\$_(GET|POST|REQUEST|COOKIE|SERVER).{1,})|[^;\\n\\r\\)]{0,100}file_get_contents.{1,})', 0), ('common_webshell13', 0, 10113, '(?i)\\$\\s*(\\w+)\\s*=[\\s\\(\\{]*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|[\'"]\\s*.{0,100}(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec).{1,100}\\s*[\'"]|file_get_contents)[\\s\\S]{0,200}create_function\\s*\\(+[^,]{1,100},[\'"\\s]*(\\$\\s*\\1[\'"\\s]*\\)|((base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]*\\$\\s*\\1))', 0), ('common_webshell14', 0, 10114, '(?i)\\$\\s*(\\w+)\\s*=\\s*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|[\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\s*[\'"]|(base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)\\s*\\()[\\s\\S]{0,200}(?<![:>\\s])\\s*\\$\\1\\s*\\(+[^\\)]*(\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})', 0), ('common_webshell15', 0, 10115, '(?i)sqlite_create_function\\s*\\([\\s\\S]{0,200}(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)|(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)[\\s\\S]{0,200}sqlite_create_function\\s*\\(', 0), ('common_webshell25', 0, 10116, '(?i)\\b(filter_var|filter_var_array)\\b\\s*\\(.*FILTER_CALLBACK[^;]*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec))', 0), ('common_webshell16', 0, 10117, '(?i)\\$\\s*(\\w+)\\s*=\\s*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|[\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\s*[\'"]|(base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)\\s*\\()[\\s\\S]{0,200}\\b(filter_var|filter_var_array)\\b\\s*\\(.*FILTER_CALLBACK[^;]*\\$\\1', 0), ('common_webshell17', 0, 10118, '(?i)\\b(mb_ereg_replace|mb_eregi_replace)\\b\\s*\\((.*,){3}\\s*([\'"][^,"\'\\)]*e[^,"\'\\)]*[\'"]|.*(\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25}).*|chr\\s*\\(\\s*101|chr\\s*\\(\\s*0x65|chr\\s*\\(\\s*0145)\\s*\\)', 0), ('common_webshell25', 0, 10119, '(?i)\\$\\s*(\\w+)\\s*=\\s*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{3,25})|[\'"][^;]*e|[^;]*chr[\\s\\(]*(101|0x65|0145))[\\s\\S]{0,200}\\b(mb_ereg_replace|mb_eregi_replace)\\b\\s*\\((.*,){3}\\s*\\$\\1', 0), ('common_webshell18', 0, 10120, '(?i)array_walk(_recursive)?\\s*\\([^;,]*,\\s*([\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec|preg_replace)\\s*[\'"]|(\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25}))', 0), ('common_webshell19', 0, 10121, '(?i)\\$\\s*(\\w+)\\s*=\\s*((\\$_(GET|POST|REQUEST|COOKIE|SERVER).{0,25})|[\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec|preg_replace))[\\s\\S]{0,200}array_walk(_recursive)?\\s*\\([^;,]*,\\s*(\\$\\s*\\1|((base64_decode|gzinflate|gzuncompress|gzdecode|str_rot13)[\\s\\(]*\\$\\s*\\1))', 0), ('common_webshell20', 0, 10122, '(?i)\\b(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec|include)\\b\\s*\\(\\s*(file_get_contents\\s*\\(\\s*)?[\'"]php://input', 0), ('common_webshell21', 0, 10123, '^(\\xff\\xd8|\\x89\\x50|GIF89a|GIF87a|BM|\\x00\\x00\\x01\\x00\\x01)[\\s\\S]*<\\?\\s*php', 0), ('common_webshell22', 0, 10124, "\\$(\\w)=\\$[a-zA-Z]\\('',\\$\\w\\);\\$\\1\\(\\);", 0), ('common_webshell23', 0, 10125, "(?i)\\$(\\w+)\\s*=\\s*str_replace\\s*\\([\\s\\S]*\\$(\\w+)\\s*=\\s*\\$(\\w+)(([\\s\\S]{0,255})|(\\s*\\(\\'\\',\\s*(\\$(\\w+)\\s*\\(\\s*)+))\\$\\1\\s*\\([\\s\\S]{0,100};?\\s*\\$\\2\\(?\\s*\\)", 0), ('common_webshell24', 0, 10126, '(?i)ob_start\\s*\\(+\\s*([\'"]\\s*(eval|assert|ass\\\\x65rt|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec).{0,20}|[\'"]\\s*\\w+[\\s\\S]{1,50}phpinfo\\s*\\(\\s*\\))', 0), ('common_webshell25', 0, 10127, '\\b(assert|eval|system|exec|shell_exec|passthru|popen|proc_open|pcntl_exec)\\b\\s*\\(((\\$_SERVER|\\$_ENV|getenv|\\$GLOBALS)\\s*[\\[\\(]\\s*[\'"]+(REQUEST_URI|QUERY_STRING|HTTP_[\\w_]+|REMOTE_[\\w_])[\'"\\s]+\\s*[\\]\\)]|php://input|exif_read_data\\s*\\()', 0), ('common_webshell24', 0, 10128, 'eval\\("\\?>"\\.|gzinflate\\(base64_decode\\(|eval\\(base64_decode\\(|cat\\s*/etc/passwd|Safe_Mode\\s*Bypass', 0), ('common_webshell25', 0, 10129, '\\$_\\[\\$_|\\${"_P"\\.|a(.)s\\1s\\1e\\1r\\1t|\'e\'\\.\'v\'\\.\'a\'\\.\'l|687474703a2f2f626c616b696e2e64756170702e636f6d2f7631|python_eval\\("import os\\\\nos.system\\(|\\$bind_pl\\s*=\\s*"IyEvdXNyL2Jpbi9lbnYgcGV|phpsocks5_encrypt\\s*\\(|eNrs/Vmv41iWJgq+ZwH1H7wdAWRksypJihRF3kQ0mvMsihTnuoUA53meeVG/valj5mbuHpF9b6P7se', 0), ('common_webshell25', 0, 10130, 'preg_replace\\s*\\(\\s*[\'"][^;]*e[^;]*[\'"],([^;]{0,30}\\\\x|[^;\\)]{200,300})|\\$back_connect="IyEvdXNyL2Jpbi9wZXJsDQp1c2UgU2|define\\(\'gzip\',function_exists\\("ob_gzhandler"\\)|chr\\(112\\)\\.chr\\(97\\)\\.chr\\(115\\)\\.chr\\(115\\)|687474703a2f2f377368656c', 0), ('common_webshell24', 0, 10131, 'ini_get\\s*\\(\\s*"disable_functions"\\s*\\)|\\d\\s*=>\\s*array\\s*\\(\\s*[\'"]\\s*pipe\\s*[\'"]|gzuncompress\\(base64_decode\\(|crypt\\(\\$_SERVER\\[\'HTTP_H0ST\'\\],\\d+\\)==|if\\(file_exists\\(\\$settings\\[\'STOPFILE\'\\]\\)\\)', 0), ('common_webshell25', 0, 10132, '\\$nofuncs=\'no\\s*exec\\s*functions|udf\\.dll|\\$b374k|POWER-BY\\s*WWW.XXDDOS.COM|<title>Safes\\s*Mode\\s*Shell</title>|Siyanur\\.PHP\\s*</font>|c999shexit\\(\\)|\\$c99sh_|c99_sess_put\\(|Coded\\s*by\\s*cyb3r|cyb3r_getupdate\\(|coded\\s*by\\s*tjomi4|john\\.barker446@gmail\\.com|eval\\("\\\\\\$x=gzin"|eval\\("\\?>"\\.gzinflate\\(base64_decode\\(|eval\\(gzinflate\\(base64_decode\\(|eval\\(gzuncompress\\(base64_decode\\(|eval\\(gzinflate\\(str_rot13\\(base64_decode\\(|function_exists\\("zigetwar_buff_prepare"\\)|dQ99shell|r57shell|c99shell|lama\'s\'hell\\s*v|Carbylamine\\s*PHP\\s*Encoder|Safe\\s*Mode\\s*Shell|\\$dI3h=\\${\'_REQUEST\'};|new\\s*COM\\("IIS://localhost/w3svc"\\)|n57http-based\\[\\s*-\\]terminal|Dosya\\s*Olu|errorlog\\("BACKEND:\\s*startReDuh,|form\\s*name=sh311Form|PHPJackal<br>|Reddragonfly\'s\\s*WebShell|\\("system"==\\$seletefunc\\)\\?system\\(\\$shellcmd\\)|eNrsvGmT40iSKPZ5xmz|CrystalShell\\s*v\\.|Special\\s*99\\s*Shell|Simple\\s*PHP\\s*Mysql\\s*client|\'_de\'\\.\'code\'|phpsocks5_encrypt\\(|define\\(\'PHPSHELL_VERSION\',|ZXZhbCgkX1BPU1RbMV0p|\\$__H_H\\(\\$__C_C', 0), ('common_webshell25', 0, 10133, 'PD9waHANCiRzX3ZlciA9ICIxLjAiOw0KJHNfdGl0bGUgPSAiWG5vbnltb3V4IFNoZWxsIC|GFnyF4lgiGXW2N7BNyL5EEyQA42LdZtao2S9f|IyEvdXNyL2Jpbi9wZXJsDQokU0hFTEw9Ii9iaW4vYmFzaCAtaSI7|setcookie\\("N3tsh_surl"\\);|function\\s*Tihuan_Auto|\\$_COOKIE\\[\'b374k\'\\]|function_exists\\("k1r4_sess_put"\\)|http://www.7jyewu.cn/|scookie\\(\'phpspypass|PHVayv.php\\?duzkaydet=|phpRemoteView</a>|define\\(\'envlpass\',|KingDefacer_getupdate\\(|relative2absolute\\(|Host:\\s*old.zone-h.org|<h3>PHPKonsole</h3>|\\$_SESSION\\[\'hassubdirs\'\\]\\[\\$treeroot\\]|strtolower\\(\\$cmd\\)\\s*==\\s*"canirun"|\\$shell\\s*=\\s*\'uname\\s*-a;\\s*w;\\s*id;|Avrasya\\s*Veri\\s*ve\\s*NetWork|<h1>Linux Shells</h1>|\\$MyShellVersion\\s*=\\s*"MyShell|<a\\s*href="http://ihacklog.com/"|setcookie\\(\\s*"mysql_web_admin_username"\\s*\\)|<title>PHP\\s*Shell\\s*[^\\n\\r]*</title>|\\$OOO000000=urldecode|1MSSYowqjzlVVAwAoHHFXzQ5Lc|\'xiaoqiwangluo\'|EqQC1FhyXxpEi7l2g\\+yNjW62S|\\$_uU\\(83\\)\\.\\$_uU\\(84\\)|7kyJ7kSKioDTWVWeRB3TiciL1UjcmRiLn4SKiAETs90cuZlTz5mROtHWHdWfRt0ZupmVRNTU2Y2MVZkT8|<title>\\s*ARS\\s*Terminator\\s*Shell</title>|base64_decode\\("R0lGODdhEgASAKEAAO7u7gAAAJmZmQAAACwAAA|\\\\x50\\\\x4b\\\\x03\\\\x04\\\\x0a\\\\x00\\\\x00\\\\x00\\\\x00|\'<title>W3D\\s*Shell|\\$back_connect="IyEvdXNyL2Jpbi9wZXJsD', 0), ('common_webshell30', 0, 10135, '\\$(\\w+)[\\s]*\\=[\\s]*\\$_(?:POST|GET|REQUEST|COOKIE|SERVER).{0,25}[\\s\\S]*(?<!\\>)\\$(?:\\1\\(\\s*\\$_(?:POST|GET|REQUEST|COOKIE|SERVER).{0,25}\\s*\\)|(\\w+)\\s*\\=\\s*\\$_(?:POST|GET|REQUEST|COOKIE|SERVER).{0,25}[\\s\\S]*(?<!\\>)\\$(\\1\\(\\s*\\$\\2|\\2\\(\\s*\\$\\1)\\s*\\)|_(?:POST|GET|REQUEST|COOKIE|SERVER).{0,25}\\(\\s*\\$\\1\\s*\\))|\\$_(?:POST|GET|REQUEST|COOKIE|SERVER)\\[([\'"]\\w+[\'"]|\\d+)\\]\\(\\s*\\$_(?:POST|GET|REQUEST|COOKIE|SERVER)\\[([\'"]\\w+[\'"]|\\d+)\\]\\s*\\)', 0))
ali_webshell_rule_jsp = [[{'data': 'allowTypes=newString[]{"jpg","jpeg","gif","ico","bmp","png"}\n\n', 'type': '2'}, {'data': 'Util.null2String(request.getParameter("dir"));', 'type': '2'}, {'data': 'saveFile.substring(0,saveFile.indexOf(', 'type': '2'}, {'data': 'newFileOutputStream(fileName);', 'type': '2'}], [{'data': 'request.getRequestURI(', 'type': '2'}, {'data': '.getBytes(', 'type': '2'}, {'data': '.getServletContext().getRealPath(', 'type': '2'}, {'data': 'FileReader(', 'type': '2'}, {'data': 'FileWriter(', 'type': '2'}, {'data': '.replaceAll(', 'type': '2'}, {'data': '.queryHashtable(', 'type': '2'}, {'data': '.listFiles(', 'type': '2'}, {'data': '.getFilePointer(', 'type': '2'}, {'data': '.delete(', 'type': '2'}, {'data': 'RandomAccessFile(', 'type': '2'}, {'data': 'System.out.println(', 'type': '2'}], [{'data': 'HttpServletRequest', 'type': '2'}, {'data': '.getBytes(REQUEST_CHARSET)', 'type': '2'}, {'data': '.getConnection(', 'type': '2'}, {'data': '.isClosed(', 'type': '2'}, {'data': '.url.equals(', 'type': '2'}, {'data': 'InputStreamReader(', 'type': '2'}, {'data': 'OutputStreamWriter(', 'type': '2'}, {'data': '.write(', 'type': '2'}, {'data': '.flush(', 'type': '2'}, {'data': '.toLowerCase().endsWith(', 'type': '2'}, {'data': 'JarFile(', 'type': '2'}, {'data': 'ZipFile(', 'type': '2'}, {'data': 'EnterFile(', 'type': '2'}, {'data': '.setAbsolutePath(', 'type': '2'}, {'data': '.getMetaData(', 'type': '2'}, {'data': '.getColumnName(', 'type': '2'}, {'data': 'formatNumber(', 'type': '2'}, {'data': '.getInterfaces().length', 'type': '2'}, {'data': 'response.getOutputStream(', 'type': '2'}], [{'data': 'response.setCharacterEncoding(', 'type': '2'}, {'data': 'StringBuffer(', 'type': '2'}, {'data': 'request.getParameter(', 'type': '2'}, {'data': 'request.getSession().getServletContext().getRealPath("/")\n\n', 'type': '2'}, {'data': '.equals(', 'type': '2'}, {'data': '.append(', 'type': '2'}, {'data': '.substring(', 'type': '2'}, {'data': 'BufferedReader(', 'type': '2'}, {'data': 'InputStreamReader(', 'type': '2'}, {'data': 'FileInputStream(newFile(', 'type': '2'}, {'data': '.replaceAll("\\\\","/")', 'type': '2'}, {'data': '.toString()', 'type': '2'}], [{'data': 'HttpServletRequestWrapper', 'type': '2'}, {'data': '.getParameter(', 'type': '2'}, {'data': '.getBytes(REQUEST_CHARSET)', 'type': '2'}, {'data': '=DriverManager.getConnection(', 'type': '2'}, {'data': '.createStatement(', 'type': '2'}, {'data': '.execute(', 'type': '2'}, {'data': '.getResultSet(', 'type': '2'}, {'data': '.getUpdateCount(', 'type': '2'}, {'data': 'BufferedReader(', 'type': '2'}, {'data': 'InputStreamReader(', 'type': '2'}, {'data': '.name.equals(', 'type': '2'}, {'data': '.replace(', 'type': '2'}, {'data': '.getCmd().equals(', 'type': '2'}, {'data': '.write(', 'type': '2'}, {'data': '.ol.setCmd(', 'type': '2'}, {'data': '.htmlEncode(', 'type': '2'}, {'data': 'formatNumber(', 'type': '2'}, {'data': '.setMaximumFractionDigits(', 'type': '2'}, {'data': '.getInstance(', 'type': '2'}, {'data': '.readLine(', 'type': '2'}], [{'data': ').newInstance(', 'type': '2'}, {'data': 'DriverManager.getConnection(', 'type': '2'}, {'data': '.setCatalog(', 'type': '2'}, {'data': 'File.listRoots(', 'type': '2'}, {'data': '.listFiles(', 'type': '2'}, {'data': '.lastModified(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': '.getName(', 'type': '2'}, {'data': '.append(', 'type': '2'}, {'data': '.delete(', 'type': '2'}, {'data': '.getOutputStream(', 'type': '2'}, {'data': 'FileInputStream(', 'type': '2'}, {'data': '.createNewFile(', 'type': '2'}, {'data': 'SimpleDateFormat(', 'type': '2'}, {'data': '(HttpURLConnection)', 'type': '2'}, {'data': '.getMetaData().getTables(', 'type': '2'}, {'data': '.createStatement(', 'type': '2'}, {'data': '.executeQuery(', 'type': '2'}, {'data': 'Runtime.getRuntime().exec(', 'type': '2'}, {'data': '.getInputStream(', 'type': '2'}], [{'data': 'DateFormat.getDateTimeInstance()', 'type': '2'}, {'data': 'System.currentTimeMillis()', 'type': '2'}, {'data': 'convertFileSize(', 'type': '2'}, {'data': 'System.arraycopy(', 'type': '2'}, {'data': 'newHashtable(', 'type': '2'}, {'data': 'System.getProperty(', 'type': '2'}, {'data': 'IllegalArgumentException', 'type': '2'}, {'data': '.startsWith(', 'type': '2'}, {'data': 'IllegalArgumentException(', 'type': '2'}, {'data': '.nextToken(', 'type': '2'}, {'data': '.nextToken().trim().equalsIgnoreCase(', 'type': '2'}, {'data': 'FileOutputStream(', 'type': '2'}, {'data': '.separatorChar', 'type': '2'}, {'data': 'URLDecoder.decode(', 'type': '2'}, {'data': '.append(conv2Html(', 'type': '2'}, {'data': '.getCanonicalPath().startsWith(', 'type': '2'}, {'data': '.getAbsolutePath()', 'type': '2'}, {'data': '.getParameterValues(', 'type': '2'}, {'data': '.getAbsolutePath(', 'type': '2'}, {'data': 'FileOutputStream(', 'type': '2'}, {'data': 'GZIPInputStream(', 'type': '2'}, {'data': 'application.getRealPath(request.getRequestURI())).getParent\n\n()', 'type': '2'}], [{'data': 'isNotEmpty(getSystemEncoding())', 'type': '2'}, {'data': '.printStackTrace(newPrintWriter(', 'type': '2'}, {'data': 'getSystemEncoding(', 'type': '2'}, {'data': 'ByteArrayOutputStream(', 'type': '2'}, {'data': '.delete()', 'type': '2'}, {'data': 'exec(', 'type': '2'}, {'data': 'isNotEmpty(request.getParameter(', 'type': '2'}, {'data': '.getBytes(', 'type': '2'}, {'data': 'BufferedOutputStream(response.getOutputStream())\n\n', 'type': '2'}, {'data': '.pushBody()', 'type': '2'}], [{'data': 'Class.forName(', 'type': '2'}, {'data': 'DriverManager.getConnection(', 'type': '2'}, {'data': 'SimpleDateFormat(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': 'HttpServletResponse', 'type': '2'}, {'data': 'BufferedInputStream(newFileInputStream(', 'type': '2'}, {'data': 'File(', 'type': '2'}, {'data': '.mkdir(', 'type': '2'}, {'data': '.listFiles(', 'type': '2'}, {'data': '.setLastModified(', 'type': '2'}, {'data': 'File(application.getRealPath(request.getRequestURI\n\n())).getParent()', 'type': '2'}, {'data': '.getErrorStream(', 'type': '2'}], [{'data': 'Runtime.getRuntime()', 'type': '2'}, {'data': 'InputStreamReader(', 'type': '2'}, {'data': 'Charset.forName(', 'type': '2'}, {'data': 'File(', 'type': '2'}, {'data': 'getParent(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': '.list()', 'type': '2'}, {'data': '.lastIndexOf(', 'type': '2'}, {'data': '.substring(', 'type': '2'}, {'data': '.write(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': '[request.getContentLength()]', 'type': '2'}, {'data': 'JshellConfigException', 'type': '2'}, {'data': '(String)session.getAttribute(', 'type': '2'}, {'data': 'session.removeAttribute(', 'type': '2'}, {'data': 'response.sendRedirect(request.getRequestURI())', 'type': '2'}, {'data': 'System.getProperty(', 'type': '2'}, {'data': 'request.getRealPath(request.getServletPath())', 'type': '2'}], [{'data': 'initPageData(request,session);', 'type': '2'}, {'data': 'if(request.getParameter(', 'type': '2'}, {'data': 'DataBaseType.equalsIgnoreCase(', 'type': '2'}, {'data': 'DriverManager.getConnection(', 'type': '2'}, {'data': '.prepareStatement(', 'type': '2'}, {'data': '.printStackTrace()', 'type': '2'}, {'data': 'session.setAttribute(', 'type': '2'}, {'data': '.equals(request.getParameter(', 'type': '2'}, {'data': 'setConnection(request,session);', 'type': '2'}, {'data': 'executQuery(connection,SHOWDATEBASES);', 'type': '2'}, {'data': '(HttpServletRequest', 'type': '2'}, {'data': 'executQuery(', 'type': '2'}, {'data': '.getColumnName(', 'type': '2'}, {'data': '.getMetaData(', 'type': '2'}, {'data': 'session.setAttribute(', 'type': '2'}], [{'data': 'IllegalArgumentException(', 'type': '2'}, {'data': 'boundary.trim().length()', 'type': '2'}, {'data': 'Hashtable(', 'type': '2'}, {'data': 'StringTokenizer(', 'type': '2'}, {'data': '.nextToken(', 'type': '2'}, {'data': '.lastIndexOf(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': 'ZipEntry(', 'type': '2'}, {'data': 'BufferedInputStream(newFileInputStream(', 'type': '2'}, {'data': '.getAbsolutePath()=conv2Html(', 'type': '2'}, {'data': 'response.setContentType(', 'type': '2'}, {'data': 'conv2Html(request.getParameter(', 'type': '2'}, {'data': '.getName(', 'type': '2'}, {'data': ').createNewFile(', 'type': '2'}], [{'data': 'File(', 'type': '2'}, {'data': 'PrintWriter(', 'type': '2'}, {'data': '.println(', 'type': '2'}, {'data': '.exists(', 'type': '2'}, {'data': '.length(', 'type': '2'}, {'data': 'request.getRequestURI()', 'type': '2'}, {'data': 'response.sendRedirect(', 'type': '2'}, {'data': 'request.getRealPath(request.getServletPath())', 'type': '2'}], [{'data': 'extendsJPanelimplementsRunnable', 'type': '2'}, {'data': 'JScrollPanescrollPane', 'type': '2'}, {'data': 'Color(', 'type': '2'}, {'data': '.getSystemState(', 'type': '2'}, {'data': 'PySystemState', 'type': '2'}, {'data': 'BorderLayout()', 'type': '2'}, {'data': 'Java2DTextWindow(', 'type': '2'}, {'data': '.setBackground(', 'type': '2'}, {'data': '.setViewportView(', 'type': '2'}, {'data': 'DefaultConsoleImpl(', 'type': '2'}, {'data': '.setTextAttributes(', 'type': '2'}, {'data': 'TextAttributes(', 'type': '2'}, {'data': 'setTextAttributes(', 'type': '2'}, {'data': '.printStackTrace()', 'type': '2'}, {'data': 'PySystemState.initialize(System.getProperties()', 'type': '2'}], [{'data': 'Hashtable()', 'type': '2'}, {'data': '.put(', 'type': '2'}, {'data': 'System.currentTimeMillis();', 'type': '2'}, {'data': 'convertFileSize(', 'type': '2'}, {'data': 'System.arraycopy(', 'type': '2'}, {'data': 'System.getProperty(', 'type': '2'}, {'data': 'IllegalArgumentException', 'type': '2'}, {'data': 'StringTokenizer(', 'type': '2'}, {'data': '.countTokens(', 'type': '2'}, {'data': '.nextToken(', 'type': '2'}, {'data': '.nextToken().trim().equalsIgnoreCase(', 'type': '2'}], [{'data': 'System.currentTimeMillis()', 'type': '2'}, {'data': 'System.getProperties();', 'type': '2'}, {'data': '.hasMoreElements(', 'type': '2'}, {'data': '.indexOf(', 'type': '2'}, {'data': '.put(', 'type': '2'}, {'data': 'Random().nextInt(', 'type': '2'}, {'data': 'request.getQueryString().indexOf(', 'type': '2'}, {'data': '(float)Runtime.getRuntime().freeMemory()', 'type': '2'}, {'data': '(float)Runtime.getRuntime().totalMemory()', 'type': '2'}, {'data': '.htShowMsg.get(', 'type': '2'}, {'data': '.htShowMsg.get(', 'type': '2'}], [{'data': 'StreamConnectorextendsThread', 'type': '2'}, {'data': 'OutputStream', 'type': '2'}, {'data': 'BufferedReader(newInputStreamReader(', 'type': '2'}, {'data': '.read(', 'type': '2'}, {'data': '.write(', 'type': '2'}, {'data': '.flush()', 'type': '2'}, {'data': '.start()', 'type': '2'}, {'data': '.getInputStream()', 'type': '2'}, {'data': 'request.getParameter(', 'type': '2'}, {'data': 'Socket(', 'type': '2'}], [{'data': 'convertpath(application.getrealpath(""));', 'type': '2'}, {'data': 'application.getrealpath(request.getrequesturi())\n\n', 'type': '2'}, {'data': '.getParent();session.setMaxInactiveInterval()', 'type': '2'}, {'data': 'StringencodeGbUnicode(', 'type': '2'}, {'data': 'newFile(', 'type': '2'}, {'data': '.isHidden()', 'type': '2'}, {'data': 'newSimpleDateFormat(', 'type': '2'}, {'data': 'out.print("");out.print("");out.print("");out.print\n\n("");out.print("");out.print("");', 'type': '2'}], [{'data': '.getBytes(REQUEST_CHARSET),PAGE_CHARSET);', 'type': '2'}, {'data': 'DriverManager.getConnection', 'type': '2'}, {'data': 'DriverManager.getConnection(', 'type': '2'}, {'data': '.getUpdateCount()', 'type': '2'}, {'data': 'newBufferedReader(newInputStreamReader', 'type': '2'}, {'data': 'SHELL_NAME=request.getServletPath();', 'type': '2'}], [{'data': 'request.getRequestURI()', 'type': '2'}, {'data': '.getServletContext().getRealPath(', 'type': '2'}, {'data': 'newPrintWriter(', 'type': '2'}, {'data': 'System.out.println(', 'type': '2'}, {'data': '.hasMoreElements()', 'type': '2'}, {'data': '(float)Runtime.getRuntime().totalMemory()', 'type': '2'}], [{'data': 'newFile(request.getParameter(""))', 'type': '2'}, {'data': '.isDirectory()', 'type': '2'}, {'data': '.listFiles();for(', 'type': '2'}, {'data': '.isDirectory(', 'type': '2'}, {'data': '[].canRead()==true', 'type': '2'}, {'data': 'response.getOutputStream()', 'type': '2'}, {'data': '.read();', 'type': '2'}, {'data': '.printStackTrace(', 'type': '2'}], [{'data': 'request.getParameter("")', 'type': '2'}, {'data': '=request.getRealPath(request.getServletPath())', 'type': '2'}, {'data': 'newFile(', 'type': '2'}, {'data': 'newPrintWriter(', 'type': '2'}, {'data': '.length()>', 'type': '2'}, {'data': 'out.println("");out.println("");out.println("")', 'type': '2'}], [{'data': 'if(request.getParameter("")=null)', 'type': '2'}, {'data': 'newString(request.getParameter("").getBytes\n\n(""),"");', 'type': '2'}, {'data': 'newFileOutputStream(', 'type': '2'}, {'data': 'request.getServerName()', 'type': '2'}, {'data': '.print(request.getRealPath(request.getServletPath()))\n\n', 'type': '2'}], [{'data': 'folderReplace(application.getRealPath(""));', 'type': '2'}, {'data': 'request.getRequestURI();if(session.getAttribute("")==null)\n\n', 'type': '2'}, {'data': 'response.sendRedirect(URL)', 'type': '2'}, {'data': 'out.print("");out.print("");out.print("")', 'type': '2'}, {'data': '.lookInfo()', 'type': '2'}, {'data': 'DriverManager.getConnection', 'type': '2'}], [{'data': 'Class.forName(', 'type': '2'}, {'data': '=DriverManager.getConnection(', 'type': '2'}, {'data': '.getMetaData();', 'type': '2'}, {'data': 'newArrayList<String>();', 'type': '2'}, {'data': '.createStatement();for(', 'type': '2'}, {'data': 'newOutputStreamWriter(newFileOutputStream(', 'type': '2'}, {'data': '.getColumnCount()', 'type': '2'}, {'data': '.setStatus();', 'type': '2'}], [{'data': 'DriverManager.getConnection', 'type': '2'}, {'data': '.createStatement(', 'type': '2'}, {'data': '.executeQuery(', 'type': '2'}, {'data': '.getMetaData(', 'type': '2'}, {'data': 'response.setStatus()', 'type': '2'}, {'data': 'newOutputStreamWriter(newFileOutputStream(', 'type': '2'}], [{'data': 'DriverManager.getConnection', 'type': '2'}, {'data': '.prepareStatement(', 'type': '2'}, {'data': '.executeQuery(', 'type': '2'}, {'data': 'ArrayList<String>', 'type': '2'}, {'data': 'newArrayList<String>();while(rs.next())', 'type': '2'}, {'data': 'newOutputStreamWriter(newFileOutputStream(', 'type': '2'}, {'data': '.prepareStatement(', 'type': '2'}, {'data': '.executeQuery()', 'type': '2'}, {'data': '.getColumnCount(', 'type': '2'}, {'data': '.printStackTrace(', 'type': '2'}], [{'data': '.hasMoreElements()){String', 'type': '2'}, {'data': 'request.getHeader(', 'type': '2'}, {'data': '.setProperty((', 'type': '2'}, {'data': ').toLowerCase()', 'type': '2'}, {'data': '.equalsIgnoreCase(', 'type': '2'}, {'data': 'request.getInputStream()', 'type': '2'}, {'data': '.delete()', 'type': '2'}, {'data': '.read())', 'type': '2'}], [{'data': 'request.getRequestURI()', 'type': '2'}, {'data': 'application.getRealPath(', 'type': '2'}, {'data': 'newFile', 'type': '2'}, {'data': 'newPrintWriter(', 'type': '2'}, {'data': '.exists(', 'type': '2'}, {'data': '.length()>)', 'type': '2'}, {'data': '.printStackTrace()', 'type': '2'}], [{'data': 'Runtime.getRuntime().freeMemory();', 'type': '2'}, {'data': 'request.getRequestURI()', 'type': '2'}, {'data': '.remove(', 'type': '2'}, {'data': '.get(', 'type': '2'}, {'data': 'System.arraycopy(', 'type': '2'}, {'data': 'ServletInputStream', 'type': '2'}, {'data': 'IllegalArgumentException', 'type': '2'}, {'data': '.listFiles()', 'type': '2'}, {'data': 'newBufferedReader(newInputStreamReader(newFileInputStream\n\n(', 'type': '2'}, {'data': 'newBufferedWriter(newOutputStreamWriter(newFileOutputStream\n\n(', 'type': '2'}, {'data': '.mkdirs())', 'type': '2'}, {'data': '[].isDirectory())', 'type': '2'}], [{'data': 'publicclasscmdservletextendshttpservlet\n\n{publicvoid', 'type': '2'}, {'data': '.getWriter()', 'type': '2'}, {'data': 'runtime.getruntime().exec(""\\+req.getparameter\n\n(""));', 'type': '2'}, {'data': 'ewDataInputStream(', 'type': '2'}, {'data': '.print((char)', 'type': '2'}], [{'data': 'publicclassListServletextendsHttpServlet\n\n{publicvoid', 'type': '2'}, {'data': '.getWriter()', 'type': '2'}, {'data': 'if(req.getParameter("")==null)', 'type': '2'}, {'data': 'newFile(', 'type': '2'}, {'data': '.isDirectory()){', 'type': '2'}, {'data': '.listFiles();for(int', 'type': '2'}, {'data': '[].isDirectory()){', 'type': '2'}, {'data': '[].isFile())', 'type': '2'}, {'data': 'newFileInputStream(', 'type': '2'}], [{'data': 'publicclassUpServletextendsHttpServlet{', 'type': '2'}, {'data': '.setContentType(', 'type': '2'}, {'data': '.getWriter()', 'type': '2'}, {'data': 'out.print("");out.print("");out.print("");', 'type': '2'}, {'data': 'newDataInputStream(', 'type': '2'}, {'data': 'newFile(', 'type': '2'}, {'data': '.getContentLength()', 'type': '2'}, {'data': '.read();', 'type': '2'}, {'data': '.write((char)', 'type': '2'}], [{'data': 'javax.servlet.http.HttpServletRequest', 'type': '2'}, {'data': 'com.caucho.jsp.QPageContext', 'type': '2'}, {'data': 'pageContext.getSession();', 'type': '2'}, {'data': 'pageContext.getServletContext();', 'type': '2'}, {'data': 'com.caucho.util.CauchoSystem.getResinHome();', 'type': '2'}, {'data': 'com.caucho.java.LineMap(', 'type': '2'}, {'data': 'com.caucho.vfs.Depend(mergePath.lookup(', 'type': '2'}], [{'data': '(String)session.getAttribute(', 'type': '2'}, {'data': 'newFile(System.getProperty\n\n("")).getCanonicalPath', 'type': '2'}, {'data': 'newInputStreamReader(out)', 'type': '2'}, {'data': '.getCanonicalPath()', 'type': '2'}, {'data': '.append(escape(f.getName()));', 'type': '2'}, {'data': ';StringfullyQualifiedExecutable=null;for\n\n(StringpathDir:pathDirs)', 'type': '2'}], [{'data': 'ByteArrayOutputStream(', 'type': '2'}, {'data': 'publicByteArrayOutputStreamgetProgOutput(', 'type': '2'}, {'data': 'CopyThread', 'type': '2'}, {'data': '.getErrorStream()', 'type': '2'}, {'data': 'BufferedWriter(newOutputStreamWriter(', 'type': '2'}, {'data': 'session.getAttribute(', 'type': '2'}, {'data': '.equalsIgnoreCase(function)', 'type': '2'}, {'data': 'request.getParameter(', 'type': '2'}, {'data': 'MessageDigest.getInstance(', 'type': '2'}, {'data': '.equalsIgnoreCase(', 'type': '2'}], [{'data': 'if(request.getParameter("', 'type': '2'}, {'data': '")!=null)(newjava.io.FileOutputStream\n\n(application.getRealPath("/")+request.getParameter("', 'type': '2'}, {'data': '"))).write(request.getParameter("', 'type': '2'}, {'data': '").getBytes())', 'type': '2'}], [{'data': '=Runtime.getRuntime().exec("cmd.exe', 'type': '2'}, {'data': 'Stringcmd=request.getParameter("cmd");', 'type': '2'}, {'data': 'newBufferedReader(newInputStreamReader(', 'type': '2'}], [{'data': 'Runtime.getRuntime()', 'type': '2'}, {'data': '.*\\.exec\\(.*request\\.getParameter', 'type': '1'}], [{'data': '.*FileOutputStream\\(.*request\\.getParameter', 'type': '1'}], [{'data': 'Runtime.getRuntime().exec(', 'type': '2'}], [{'data': 'Runtime.getRuntime()', 'type': '2'}, {'data': '.exec(', 'type': '2'}], [{'data': 'ExeShellResultshellResult=newExeShellResult();', 'type': '2'}, {'data': 'ExeShellCmd.exec(', 'type': '2'}], [{'data': 'newInstance();', 'type': '2'}, {'data': 'DriverManager.getConnection(', 'type': '2'}, {'data': '.createStatement(', 'type': '2'}, {'data': '.executeQuery(', 'type': '2'}], [{'data': 'Stringresult=processCmd(cmd);', 'type': '2'}]]