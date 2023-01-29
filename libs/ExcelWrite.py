def WriteText():
    with open('logfile.csv', 'at') as f:
        try:
            f.write('Hola mundo')
            f.write('\n')
        except OSError:
            print("Disk full?")
        
def ReadDocument():
    with open('logfile.csv', 'rt') as f:
        values= f.read()
    return values

'''
def main():
    #WriteText()
    print(ReadDocument())
    
if __name__== '__main__':
    main()
'''
