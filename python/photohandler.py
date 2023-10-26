import PIL.Image
import os
import subprocess


month = ["_Gennaio", "_Febbraio", "_Marzo", "_Aprile", "_Maggio", "_Giugno", "_Luglio", "_Agosto", "_Settembre", "_Ottobre", "_Novembre", "_Dicembre"]

files = os.listdir("downloads/")
for f in files:
	try:
		if (f[3] == "-" or f[3] == "_"): dataf = f[4:]
		else: dataf = f[3:]
		data = [[],[],[]]
		data[0] = dataf[0:4]  # IMG20230121182058
		data[1] = dataf[4:6]
		data[2] = dataf[6:8]
		remotefolder = "photos/" + data[0] + "/" + data[1] + month[int(data[1])-1] + "/" + data[0] + data[1] + data[2].split(" ")[0] + "/"
		process = subprocess.Popen("/usr/bin/mkdir -p " + remotefolder, shell=True, stdout=subprocess.PIPE)
		print(f + " scaricato in " + remotefolder)
		process.wait()
		process = subprocess.Popen("/usr/bin/mv photos/" + f + " " + remotefolder, shell=True, stdout=subprocess.PIPE)
		process.wait()
	except Exception as e:
		print(e)
		print(f + " in attesa")
		pass
