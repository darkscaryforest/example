import traceback
print "hello world"

while True:
    try:
        x = int(input("Please enter a number: "))
    except Exception as e:
        print e.message
        print e.args
        exc = traceback.format_exc()
        print exc
