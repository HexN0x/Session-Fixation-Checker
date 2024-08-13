from colorama import Fore, Style, init
init()


def Session(a, b, c):
  
    if a == b == c:
        return True
    else:
        return False

def main():
    
    input_a = input("Before Login:- ")
    input_b = input("After Login:- ")
    input_c = input("After Logout:- ")
    
  

    if Session(input_a, input_b, input_c):
        print(f"{Fore.RED}Vulnerable to Session fixation! Report Kar lodu")
	
    else:
        print(f"{Fore.GREEN}No Match .")
	

if __name__ == "__main__":
    main()
