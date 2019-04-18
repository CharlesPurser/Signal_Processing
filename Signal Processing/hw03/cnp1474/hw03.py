# Purser, Charles N.
# cnp1474
# 2019-02-12

import numpy as np
import csv

class hw03() : 

#pulse function
  pulse0 = np.ones( 10 )
  pulse0 = pulse0/np.linalg.norm(pulse0)
  pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
  pulse1 = pulse1/np.linalg.norm(pulse1)
  
#lists
  num = []
  bits = []
  ten = []
  binary = []
  message = []

#file reader
  with open('data-communications.csv') as csvfile : 
    read = csv.reader( csvfile )
    for i in read : 
      for j in i : 
        num.append( float(j) )
#split into chunks of 10  
    for i in range( 0, len(num), 10 ) :
      ten.append( num[i:i+10] ) 
#delete noise and convert to binary  
    for i in ten : 
      d0 = np.dot( i, pulse0 )
      d1 = np.dot( i, pulse1 )
      c0 = np.abs( (d0/((np.linalg.norm(i)*np.linalg.norm(pulse0)))) )
      c1 = np.abs( (d1/((np.linalg.norm(i)*np.linalg.norm(pulse1)))) )
      if(c0>c1) :
        bits.append(0)
      else : 
        bits.append(1)
 
#split into chunks of 8
    for i in range( 0, len(bits), 8 ) : 
      binary.append( str(bits[i:i+8]) )

#convert to list of binary numbers
    for i in binary :
      temp = ''
      for j in i :
        if (j == '[' or j == ']' or j == ','or j == ' ') :
          k = 1
        else :
          temp = temp + j
      message.append(temp)
    char = ''
    for i in message :
      char = char + chr(int(i, 2))
    print(char)  










