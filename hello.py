#import datetime

def main():
    # Your existing code here (e.g., print("Hello, World!"))
    print("Opened Code") 
    # Get the current date and time
    #now = datetime.datetime.now()
    print("Running Code")
    # Write to the text file
    with open("output.txt", "a") as file:
        file.write(f"Hello, World!") 
        #file.write(f"Hello, World! ({now:%Y-%m-%d %H:%M:%S})\n")
    print("Finished Code")
    print("Finished Code")
    print("Finished Code")
    print("Finished Code...!")
if __name__ == "__main__":
    main()
