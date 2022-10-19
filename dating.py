# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 18, 2022
# This program checks if the users age is in between 25 and 40
# then tells them if they could date the grandparents grandchild


def main():
    # gets users age
    user_age_str = input("What is your age? ")

    # adds extra line
    print("")

    try:
        # cats the input into an integer
        user_age_int = int(user_age_str)

        # checks if the user is the correct age
        if user_age_int >= 25 and user_age_int <= 40:
            print("You can date their grandchild")
        else:
            print("you cannot date their grandchild")

    # catches any errors with the input
    except:
        print("you entered an invalid age")


if __name__ == "__main__":
    main()
