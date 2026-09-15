print("6. REAL-WORLD EXAMPLE - LOGGING SYSTEM")
def log_activity(activity):
    with open("log.txt", "a") as log_file:
        log_file.write(activity + "\n")
log_activity("User logged in.")
log_activity("User uploaded a file.")
print("Activities logged in log.txt")