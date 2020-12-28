filenames = ['CSC_217_attendance_ week1_end.txt', 'CSC_217_attendance_ week1_30.txt']
with open('CSC_217_attendance_week1.txt', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			for line in infile:
				outfile.write(line)