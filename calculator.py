def repl():
    print("Type quit to exit")
    print("Enter the expression to be calculated")
    while True:
        try:
            s=input().strip()
            if not s:
                continue
            if s.lower()=="quit":
                print("Calculator terminated")
                break
            ans=eval(s)
            print(ans)
        except:
            print("Error, Please try with a valid expression")
if __name__=="__main__":
    repl()
