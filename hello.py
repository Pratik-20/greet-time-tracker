# create_progress_file.py

def create_progress_file():
    filename = "progress.txt"
    lines = [
        "Step 1: Initializing the process",
        "Step 2: Downloading data",
        "Step 3: Processing data",
        "Step 4: Finalizing",
    ]

    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"Progress file '{filename}' created successfully!")

if __name__ == "__main__":
    create_progress_file()
