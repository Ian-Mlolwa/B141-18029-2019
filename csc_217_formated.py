def csc_217_formated(CSC_217_IT):
    filename = (CSC_217_IT)
    unique_names=set()

    with open('CSC_217_IT.txt','a')as outfile:

        for file in filename:

            for student_name in open(filename):


                 student_name = {'admission_number', 'name'}
                 print(student_name)
                 if student_name not in unique_names:
                     outfile.write('student_name')
                     unique_names.add('student_name')

    return outfile
csc_217_formated('CSC_217_IT.txt')