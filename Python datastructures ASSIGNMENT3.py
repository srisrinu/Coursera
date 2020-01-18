'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt '''
fname=input("Enter filename:")

try:
    fh=open(fname)
except:
    print("There is no such file in the directory!")
    quit()
count=0
s=0
for line in fh:
    line=line.rstrip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    count+=1
    pos=line.find(':')
    s+=float(line[pos+1:])
print("Average spam confidence:",s/count)    
    
    
