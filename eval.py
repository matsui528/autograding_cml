import subprocess

def run(cmd):
    out = subprocess.run(cmd, shell=True, capture_output=True)
    out = out.stdout.decode('UTF-8')
    return out

if __name__ == '__main__':
    print("## Run `gcc main.c`")
    print(run("gcc main.c"))

    print("## Run `./main.c 3 5`")
    result = run("./a.out 3 5")
    result = result.rstrip()  # delete the final new line
    print(result)
    
    print("## Judge")
    if result == "15":
        print("ok!")
    else:
        print(f"{result} is not 15. something wrong")
    