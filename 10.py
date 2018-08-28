#Q1.Read n Lines of a File
f=open('file1.txt','r')
new=f.read()
print(new)
f.close()
print()

#Q2.Count the Frequency of Words in a File

f=open("file1.txt",'r')
data=f.read()
words=data.split()
dict={}
for i in words:
    dict[i]=words.count(i)
print(dict)
print()

#Q3.Copy the Contents of a File to Another File

f=open("file1.txt",'r')
g=open("file2.txt",'w')
for i in f:
    g.write(i)
f.close()
g.close()
print()

#Q4.Combine each line from first file with the corresponding line in second file

lst1=[]
lst2=[]
s=str()
with open('file1.txt','r') as f1:
    with open('file2.txt','r') as f2:
       lst1+=f1.readlines()
       lst2+=f2.readlines()
       for i,j in zip(lst1,lst2):
           print(i)
           print(j)
           s+=i+j
with open('file3.txt','w') as f3:
      f3.write(s)
#Q5.Read a File and Sort it to Another File
with open('file4.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('file4.txt','r') as f:
   data=f.readlines()
  # print(data)
   for no in data:
      l=no.split()
   l.sort()

with open('file5.txt','w') as f:
   for i in l:         
      f.write("%s "%(i))
