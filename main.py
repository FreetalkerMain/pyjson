import json

#creat dic val
dic={"key1":"data","key2":"val2"}
print(dic)

#creat json file in dic data
with open("data.json","w")as f:json.dump(dic,f)
  
#read json file in data.json file
with open("data.json","r")as f:indata=json.load(f)
print(indata)

