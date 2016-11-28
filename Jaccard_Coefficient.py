"""
File Name : Jaccard_coef.py

Inputs : Doc1.txt Doc2.txt

Output : Value of Jaccard similarity coefficient

Implemented By : Sanket Kakad

Reference : https://en.wikipedia.org/wiki/Jaccard_index

"""

def main():
  Count = 0;
  Doc1 = "Potato";
  Doc2 = "Potatos"
  Doc1_D = {}
  Doc2_D = {}
  DocR_D = {}
  
  n = 1;
  Doc1_L =[Doc1[i:i+2] for i in range(0, len(Doc1)-1, n)]
  Doc2_L =[Doc2[i:i+2] for i in range(0, len(Doc2)-1, n)] 
  for word in Doc1_L:
    word_s = word.lower()
    Doc1_D[word_s] = 1
    DocR_D[word_s] = 1

  for line in Doc2_L:
        for word in line.split():
          word_s = word.lower()
          Doc2_D[word_s] = 1
          DocR_D[word_s] = 1
          
  Doc1_Set = set(Doc1_D)
  Doc2_Set = set(Doc2_D)
  #print(Doc1_Set)
  #print(Doc1_D)
  for w in Doc1_Set:
    for w1 in Doc2_Set:
      if w==w1:
        #print("hi")
        Count = Count+1
    
  print ("Bigrams for Str 1 is "+ str(Doc1_L) +" And Bigrams for Str 2 is "+ str(Doc2_L))        
  print ("Intersection of Document :" + str((Count) )+ "\n" + "Union of Doc :" + str(len(DocR_D)))
  print ("Jaccard similarity coefficient = " +str(Count/len(DocR_D)))
  
  
main()


""" 
OUTPUT :

C:\Personal\Mtech\1st\I\IR\Jaccard_Similarity_Coefficient>python  Jaccard_coef.py
Intersection of Document :2
Union of Doc :5
Jaccard similarity coefficient = 0.4


"""