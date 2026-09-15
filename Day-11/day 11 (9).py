print("14. for LOOP WITH else") # else runs only if the loop completes without break
notifications = [1, 0, 0, 0]     # 1 = Unread, 0 = Read
for notification in notifications:
    if notification == 1:
        print("You have unread notifications!")
        break
else:
    print("All caught up!")      # Runs because no break occurred
print("15. while LOOP WITH else")
correct_otp = "7890"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    entered_otp = input("Enter OTP: ")
    if entered_otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")
        attempts += 1
else:
    print("OTP expired. Request a new one.")





