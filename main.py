from strength_checker import check_strength
from dictionary_generator import generate_dictionary
from hash_analyzer import generate_hashes
from bruteforce_simulator import estimate_bruteforce
from report_generator import generate_report

while True:
    print("\n===== PASSWORD SECURITY AUDIT SUITE =====")
    print("1. Password Strength Analysis")
    print("2. Dictionary Generator")
    print("3. Hash Generator")
    print("4. Brute Force Estimator")
    print("5. Generate Audit Report")
    print("6. Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        print(check_strength(input("Enter password: ")))
    elif choice=="2":
        print(generate_dictionary(input("Name: "), input("Year: ")))
    elif choice=="3":
        print(generate_hashes(input("Password: ")))
    elif choice=="4":
        estimate_bruteforce(int(input("Length: ")))
    elif choice=="5":
        generate_report(input("Password: "))
    elif choice=="6":
        break
