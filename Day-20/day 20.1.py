print("3. sys MODULE")
import sys
print("Python Version:", sys.version)
print("Module search paths (first 3):")
for p in sys.path[:3]:
    print(" →", p)
print("4. platform MODULE")
import platform
print("OS:", platform.system())
print("Release:", platform.release())
print("Processor:", platform.processor())
