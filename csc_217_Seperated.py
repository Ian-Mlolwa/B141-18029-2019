def csc_217_attendance(file1, file2):
	filenames = [file1, file2]
	unique_name = set()
	with open('CSC_217_attendance_ week1.txt', 'r') as infile:
		with open('CSC_217_IT.txt', 'w', 'CSC_217_Computer.txt', 'w') as outfiles:
			for file in filenames:
				for student_name in open(file):
					if student_name not in unique_names:
						outfile.write(student_name)
						unique_names.add(student_name)
						return outfiles