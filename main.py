from posixpath import dirname
from time import localtime, time
from bitcoinaddress import Wallet, wallet
from math import pow
import os
from Crypto.Random.random import randrange
from balance_check import *
from directory import *

#puzzle_number_to_solve:
n=64

#Do you want this program to store all private keys?
StoreAllPrivateKeys=True
CheckBalanceMode=False
#enter the public key you aim to crack:
pubtofind='16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN'

a=int(pow(2,n-1))
b=int(pow(2,n))
total_count=b-a
start_time=time()

range_var=range(a,b)

#Crypto.Random.random.shuffle(range_var)

lt=localtime()
datetime_var=f'{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}_{lt.tm_hour}:{lt.tm_min}:{lt.tm_sec}';

basepath = os.path.dirname(__file__)

try:
    txt_file_path=latest_txt_pathfinder(basepath)
    output_file = open(txt_file_path,  "a",1)
    print("Previous text file was founded at: \n"+txt_file_path)
except:
    output_file = open(basepath+"/"+"output_"+str(datetime_var)+".txt","w",1)
    output_file.write("estimated time: "+str(total_count/300)+"s\n")
    output_file.write("total addresses: "+str(total_count)+" ["+str(a)+":"+str(b)+" ]"+"\n\n")




for i in range(a,b):
    
    temp=int(randrange(0, total_count))
    #if(repeated==-1):
        #continue
    i=range_var[temp]
    #print(range_var[temp])
    #repeated[temp]=-1
    
    
    hex_var=str(hex(i))[2::]
    l=len(hex_var)
    hex_var= (64-l)*'0' + hex_var

    wallet = Wallet(hex_var)
    pubfinded = wallet.address.mainnet.pubaddr1c


    if(pubfinded==pubtofind or StoreAllPrivateKeys==True):
        
        if(CheckBalanceMode==True):
            print(check_balance(str(pubfinded)));
        #print('Private_key:',hex_var)
        #output_file.write("- - - "*10+"\n")
        #output_file.write("#"+str(i)+" -> ")
        output_file.write(str([hex_var, pubfinded])+"\n")
        #output_file.write("   in   "+str(time()-start_time)+"s"+"\n"+"- - - "*10+"\n")
        
    if(i%1000==0):
        #j+=1000
        #print(i,j)
        #speed=int(1000 / (time()-start_time))
        #print(speed)
        #start_time=time() 
        #print(int(total_count/speed), sep="",end="s remaining\n")        
        #total_count=total_count-1000
        #print(total_count,"\n")
        output_file.write("#"+str(i)+"\n")


output_file.write("-.-."*10+"\n"+"TOTAL TIME: "+str(time()-start_time)+"s"+"\n")
output_file.write("TOTAL addresses checked: "+str(b-a)+"\n")

output_file.close

        










        

        
    




