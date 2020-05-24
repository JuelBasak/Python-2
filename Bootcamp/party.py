from time import sleep

def get_bool(prompt):
    try:
        return {"true":True,"false":False}[input(prompt).lower()]
    except KeyError:
        print "Only enter true or false..."
        
print "Please get ready for the party. I'll be back..."

sleep(18)
print "I'm back :)"


