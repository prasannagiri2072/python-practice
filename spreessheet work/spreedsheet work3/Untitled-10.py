#Given a list slice it into a 3 equal chunks and reverse each list
#For Example: sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#Expected Outcome:
#Original list  [11, 45, 8, 23, 14, 12, 78, 45, 89]
#Chunk  1 [11, 45, 8]
#After reversing it  [8, 45, 11]
#Chunk  2 [23, 14, 12]
#After reversing it  [12, 14, 23]
#Chunk  3 [78, 45, 89]
#After reversing it  [89, 45, 78]

samplelist = [11, 45, 8, 23, 14, 12, 78, 45, 89]
a = samplelist[:3]
a.reverse()
b = samplelist[3:6]
b.reverse()
c = samplelist[6:9]
c.reverse()
print(a,"\n",b,"\n",c)
