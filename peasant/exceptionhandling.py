try:#basic block
    
    age = int(input("enter your age"))
    if age>18:
        print("you can vote")
    else:
        print("you cannot vote")
except:# if block have an runtime error it s runs
    print("sorry please type numbers only")
    
finally:# if try block runs its also runs ,if except block runs it's also runs
    print("sample")
#we can use finally or else ,we cannot use both
#if try block runs successfully ,it runs otherwise it dont run
else:
    print("try block runs succefully")
# it used in the software testing
