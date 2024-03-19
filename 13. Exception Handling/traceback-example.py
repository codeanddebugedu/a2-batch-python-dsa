import traceback

try:
    print("Done")
    print("Done")
    print("Done")
    print("Done")
    print(5 / 0)
    print("Done")
    print("Done")
    print("Done")
except Exception as e:
    print(type(e).__name__)
    print(e)
    traceback.print_exc()
    print("-----")
