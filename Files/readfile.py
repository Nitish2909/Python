
f = open("poem.txt" ,"r") 
content = f.read()

if("Twinkle" in content):
    print("The word Twinkle is present in the content ")
else:
     print("The word Twinkle is not present in the content ") 

print(content) 

f.close()