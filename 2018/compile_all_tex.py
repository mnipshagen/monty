import os 
import subprocess


def main():
    current = os.getcwd()
    rootfiles = sorted(os.listdir())

    for dir in rootfiles:
        if not os.path.isdir(dir):
            continue

        path = os.path.join(current, dir)
        os.chdir(path)
        print(f"********\nWorking on {path}:\n********")

        for fh in os.listdir():
            if not fh.endswith(".tex"):
                continue
            proc = subprocess.Popen(["latexmk", "-quiet", "-c"])
            proc.communicate()
            for _ in range(3):
                proc = subprocess.Popen(["latexmk", "-quiet", "-pdf", fh])
                proc.communicate()
            proc = subprocess.Popen(["latexmk", "-quiet", "-c"])
            proc.communicate()

        os.chdir(current)


if __name__ == "__main__":
    main()
