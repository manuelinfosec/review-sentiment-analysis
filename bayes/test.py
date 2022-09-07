from train import getwords, poswords, negwords 


testset= open('test_set.csv', 'r')
testset.readline()           

output = open("prediction_file.csv", 'w')

for line in testset:
    linesplit = line.split()
    testwords= getwords(linesplit)
    totpos, totneg= 0.0, 0.0
    for word in testwords:
        word.lower()
        
        a= poswords.get(word,0.0) + 1.0
        b= negwords.get(word,0.0) + 1.0  
             
        totpos+= a/(a+b)
        totneg+= b/(a+b) 
        
    if totneg>totpos: 
        output.write("1," + line )
     
    if totneg<totpos: 
        output.write("0," + line ) 
        
    if totneg==totpos:
        output.write("1," + line)
testset.close()
output.close()

