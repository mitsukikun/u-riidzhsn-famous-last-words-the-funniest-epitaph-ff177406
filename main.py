import os

LINE = "Tell my wife I was right. Tell my boss I was wrong. Tell the doctor I was early."

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
