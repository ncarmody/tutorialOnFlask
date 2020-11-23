from plotly.tools import mpl_to_plotly
from matplotlib import pyplot as plt
import dash
import dash_html_components as html
import dash_core_components as dcc
from function_col import pp, plotly_plot_data
import base64
import pandas as pd
# app= dash.Dash()
# for i in range
bytearray(b'010af2b0009ce0010')
hex_digits = b'01a93b0009e20010'
# pp(bytes(bayer.ravel().tolist()))



pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 30)
pd.set_option('display.expand_frame_repr', True)


#    Use a production WSGI server instead.
#  * Debug mode: off
#  * Running on http://0.0.0.0:8050/ (Press CTRL+C to quit)
#  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
# 167.248.133.53 - - [23/Nov/2020 16:10:37] code 400, message Bad HTTP/0.9 request type ('\x16\x03\x01\x00{\x01\x00\x00w\x03\x03DÇ\x9e}ÑÀË=\x19Dc;\x87M\x07núLÈ#\x8fÔýÿu\x88&èZ!§\x04\x00\x00\x1aÀ/À+À\x11À\x07À\x13À')
# 167.248.133.53 - - [23/Nov/2020 16:10:37] " {  wDÇ}ÑÀË=Dc;MnúLÈ#Ôýÿu&èZ!§  À/À+ÀÀÀÀ      ÀÀ" HTTPStatus.BAD_REQUEST -
# 167.248.133.53 - - [23/Nov/2020 16:10:39] "GET / HTTP/1.1" 404 -
# 167.248.133.53 - - [23/Nov/2020 16:10:39] "GET / HTTP/1.1" 404 -
df = pd.read_csv("C:/Program Files/rd-usb/2020-11-22.csv", encoding='latin')
pickled_b64 = ('\x16\x03\x01\x00\x00w\x03\x03DÇ\x9e')
pp(base64.b64decode(pickled_b64.decode()))

dataFordf = pickled_b64.decode('utf-8')
raise Exception
dictlist = pickle.loads(base64.b64decode(dataFordf.encode()))
print('huerePingu')
pp(dictlist, sc='dictlist')
df_dictlist = pd.DataFrame(dictlist, columns=self.df.columns)

if self.df.shape[0]>0:

	self.df = self.df.append([df_dictlist], ignore_index=True)
bytearray.fromhex("\x01\x00\x00w\x03\x03DÇ\x9e".decode('utf-8'))
pp(df)
# " {  wDÇ}ÑÀË=Dc;MnúLÈ#Ôýÿu&èZ!§  À/À+ÀÀÀÀ      ÀÀ" HTTPStatus.BAD_REQUEST -


# # def hexcon(x):
# # 	for i in bytearray.fromhex(x):
# # 		try:
# # 			zahl+=i
# # 		except:
# # 			zahl = i
# # 		print(zahl)

# # # [hexcon(x) for x in 010af2b0009ce0010]


# # hex_digits = 0x010af2b0009ce0010
# # hex_digits = 0x01b9db0009ec0010
# # pp(hex_digits)

# # pp([12+13+62])
# # hex_digits = hex_digits.decode('utf-8')
# # # hex_digits = hex_digits.encode()
# # # # hex_digits = "1A2B"
# # a_bytearray = bytearray.fromhex(hex_digits)

# # for byte in a_bytearray:
# #      print(byte)
# # # 1 197 13, 0 9 226,0 16
# # # 16 0 226, 9 0 13, 197, 1
# # a_bytearray = bytearray.fromhex(hex_digits)
# # print(a_bytearray)
# # # b = 0

# # # print((a_bytearray[0]+a_bytearray[1]+a_bytearray[2])/100)
# # # print((a_bytearray[3]+a_bytearray[4]+a_bytearray[5])/100)
# # toBeDecoded = hex_digits
# # pp(hex(hex_digits))
# # for bytes in bytearray.fromhex("01a93b0009e20010"):
# # 	print(bytes)
# # 	try:
# # 		z+=bytes

# # def invertKey(key): return {key_i for key_i in key.reverse()}
# # f = pd.to_datetime("2020-11-22T14:07:26.485739Z",infer_datetime_format=True)
# # pp(f)
# # pp(f.dt.year)
# dataDict = {'distance':0.0, 'temperature': 0.0,'humidity': 0.0, 'time': ""}
# pp(list(dataDict.keys()))

# deveui
# 0xEF, 0x2F, 0x00, 0x00, 0x00, 0x00, 0x7A, 0xBE

# appeui
# 0xED, 0x22, 0x00, 0x00, 0x00, 0x00, 0x7A, 0xBE
# l = {'eui': ['BE','7A','00','00','00','00','2F','EF'], 'appeui': ['BE','7A','00','00','00','00','22','ED']}

# for l_i in l:
# 	pp(l_i)
# 	# pp(['BE','7A','00','00','00','00','2F','EF'].reverse())
# 	# pp(['BE','7A','00','00','00','00','2F','EF'].__reversed__())
# 	pp(l[l_i].reverse())
# 	pp(l[l_i])
# 	# pp([l_i, invertKey(l[l_i])])
# v = {"cmd":"gw","seqno":103915,"EUI":"FFFFFFFFFFFFFFFA","ts":1606054046489,"fcnt":2,"port":1,"freq":868500000,"toa":56,"dr":"SF7 BW125 4/5","ack":false,"gws":[{"rssi":-71,"snr":10,"ts":1606054046489,"tmms":null,"time":"2020-11-22T14:07:26.485739Z","gweui":"647FDAFFFF007AFB","ant":0,"lat":47.40912537932723,"lon":8.549648523330688}],"sessionKeyId":null,"bat":255,"data":"01bbd70009d80010"}
# v = request.get_jason()
# v = v['data']
# v = 0x01bbd70009d80010
# pp(v)
# v.encode('utf-8')
# raise Exception

# def rshift(val, n): return (val % 0x100000000) >> n


# # toBeDecoded = bytearray.fromhex("01a93b0009e20010")
# # toBeDecoded = bytearray.fromhex("01bbd70009d80010")

# # toBeDecoded = 0x01bbd70009d80010
# pp(toBeDecoded)
# for b in toBeDecoded:
# 	print(b)
# i = 0

# dd = (rshift((toBeDecoded[i]<<16),0) + rshift((toBeDecoded[i+1]<<8),0) + toBeDecoded[i+2])/100
# pp(dd)
# i += 3
# dd = (rshift((toBeDecoded[i]<<16),0) + rshift((toBeDecoded[i+1]<<8), 0) + toBeDecoded[i+2])/100
# pp(dd)
# i += 3
# dd = (rshift((toBeDecoded[i]<<16), 0) + rshift((toBeDecoded[i+1]<<8), 0))/100
# pp(dd)
# raise Exception

# for byte in a_bytearray:
# 	b+= byte
# 	print(byte)
# 	print(b)
# import pickle
# raise Exception
# # pickled_b64 = request.get_data(as_text=False)
# pickled_b64 = d

# dataFordf = pickled_b64.decode('utf-8')
# pp(dataFordf)

# dictlist = dataFordf.encode()
# pp(dictlist)
# dictlist = base64.b64decode(b'01af2b0009ce0010')
# pp(dictlist)
# dictlist = pickle.loads(b'01af2b0009ce0010')
# pp(dictlist)
# raise Exception

# dictlist = base64.b64decode(dataFordf.encode())
# pp(dictlist)
# raise Exception
# dictlist = pickle.loads(base64.b64decode(dataFordf.encode()))

# # dictlist = pickle.loads(base64.b64decode(dataFordf.encode()))
# print('huerePingu')
# pp(dictlist, sc='dictlist')
# df_dictlist = pd.DataFrame(dictlist, columns=self.df.columns)



# def PayloadDecoder(toBeDecoded):
# 	r = base64.b64decode(toBeDecoded)
# 	pp(r)

# 	decoded = {}
# 	i = 0
# 	decoded['distance'] = (((toBeDecoded[i]<<16)>>0) + ((toBeDecoded[i+1]<<8)>>0) + toBeDecoded[i+2])/100
# 	i+=3
# 	decoded['humidity'] = (((toBeDecoded[i]<<16)>>0) + ((toBeDecoded[i+1]<<8)>>0) + toBeDecoded[i+2])/100
# 	i+=3
# 	decoded['temperature'] = (((toBeDecoded[i]<<16)>>0) + ((toBeDecoded[i+1]<<8)>>0) + toBeDecoded[i+2])/100
# 	i+=3
# 	return decoded

f = {}
f['und'] = 3
f['hallo'] = 'hallo'
pp(f)

pp(PayloadDecoder(d))
raise Exception
# fig= plt.figure()
# ax= fig.add_subplot(111)
fig, (ax1,ax2)=plt.subplots(2)
# pp(dir(ax2))
# pp(dir(ax2.legend()))

ax1.plot(range(10), [i**2 for i in range(10)])
ax1.grid(True)
ax2.plot(range(5), [i for i in range(5)])
# fig.legend
# ax2.legend('hello')
if ax1.get_legend():
	print('there')
ax1.legend()

# pp(dir(ax1.get_legend()))

if ax1.get_legend():
	print('there2')
show_colorbar = True


plotly_fig = plotly_plot_data(fig)



# plotly_fig.update_layout(showlegend=True)

pp(plotly_fig )

plotly_fig.show()


# app.layout= html.Div([
#     dcc.Graph(id= 'matplotlib-graph', figure=plotly_fig)

# ])




# app.run_server(debug =False, port=8010, host='localhost')