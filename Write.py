with open('Test.txt', 'r') as reader: # different way to pen and close files without close() method
    scan = reader.readlines()
    a = reversed(scan)
    with open('Test.txt', 'w') as writer:
        for i in a:
            writer.write(i)



