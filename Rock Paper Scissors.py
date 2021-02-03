user_1=str(input("give an input: "))
user_2=str(input("give an input: "))
a=["rock","scissors","paper"]
if user_1==user_2:
        print("restart the game")
    

elif user_1=="rock" and user_2 =="scissors" :
     print("user_1 won the match")
    
elif user_1=="scissors" and user_2=="paper":
       print("user_1 won the match")
elif user_1=="paper" and user_2=="rock":
        print("user_1 won the match")
else :
        print("user_2 won the match")
    