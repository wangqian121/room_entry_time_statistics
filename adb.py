import subprocess

def run():
    ps = subprocess.Popen('adb logcat', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    with open("adb.txt", 'a+') as f:
        f.seek(0)
        f.truncate()
    for line in ps.stdout:
        if "onBufferingUpdate".encode() in line:
            print(line)
            with open("adb.txt", 'a+') as f:
                f.write(line.decode("utf-8"))

if __name__ == '__main__':
    run()
