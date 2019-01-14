import socket
import csv
import time

def datascale (val):
	scale=val[4:6];
	if scale == "00" : return 1;
	if scale == "01" : return 10;
	if scale == "02" : return 100;
	if scale == "03" : return 100;
	if scale == "04" : return 0.1;
	if scale == "05" : return 0.01;
	if scale == "06" : return 0.001;

#udp_ip = "192.168.137.49"
udp_ip = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

while True:
	data, addr = sock.recvfrom(1024)
	print data
	print addr
	print "datalength: " 
	print len(data)
	#sensorstart=50;
	ss=50;
	ts=time.strftime("%x %X", time.localtime());
	print (ts)
	
	datarow=[None]*16;
	datarow[0]=ts;
	for i in range (5):
		freq = data[ss+(8*2*i):ss+(8*2*i)+8];
		acc = data[ss+(8*2*i)+8:ss+(8*2*i)+16];
        	scalef = datascale (freq);
		scalea = datascale (acc)
		tempf = freq[0:0+4];
		tempa = acc[0:0+4];
        	freq = int (tempf,16);
        	freq = freq*scalef;
		acc = int (tempa,16);
		acc = acc*scalea;
        	print "freq",i+1,"=",freq;
		print "acc",i+1,"=",acc;
		datarow[(2*i)+1]=freq;
		datarow[(2*i)+2]=acc;
	
	rmsval = data[ss+80:ss+80+8];
	scalerms = datascale (rmsval);
	temprms = rmsval[0:0+4];
	rmsval = int (temprms,16);
	rmsval = rmsval*scalerms;
	print "RMS Acc","=",rmsval;
	datarow[11]=rmsval;

	kurtosis = data[ss+80+8:ss+80+16];
	scalek = datascale (kurtosis);
	tempkurtosis = kurtosis[0:0+4];
	kurtosis = int (tempkurtosis,16);
	kurtosis = kurtosis*scalek;
	print "Kurtosis","=",kurtosis;
	datarow[12]=kurtosis;
	
	stemp = data[ss+80+16:ss+80+24];
	scales = datascale (stemp);
	tempstemp = stemp[0:0+4];
	stemp = int (tempstemp,16);
	stemp = stemp*scales;
	print "Surface temp","=",stemp;
	datarow[13]=stemp;
	
	rssi = data[28:28+1];
	rssi = int (rssi,16);
	rssi = rssi - 107;
	print "RSSI","=",rssi;
	datarow[14]=rssi;
	
	nodeid = data[8:8+4];
	print "Node ID","=",nodeid;
	datarow[15]=nodeid;
		
	logfile = open('log.csv',"a");
	writer = csv.writer(logfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE);
	writer.writerow(datarow);
	logfile.close();
