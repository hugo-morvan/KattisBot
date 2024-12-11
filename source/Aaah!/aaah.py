def main():
    # Read the input strings
    jon_aah = input()
    doctor_aah = input()

    # Check if Jon Marius can go to the doctor
    if len(jon_aah) >= len(doctor_aah):
        print("go")
    else:
        print("no")

if __name__ == "__main__":
    main()