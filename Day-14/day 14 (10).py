print("19. LOCAL VARIABLES & SCOPE")
x = 100                               # Global
def Test():
    x = 50                            # Local
    print("Inside function:", x)
Test()
print("Outside function:", x)
