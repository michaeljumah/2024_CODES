"""lets make our own consol"""
import cmd

class MyCmd(cmd.Cmd):
    prompt = '>>>'
    
    def do_greatings(self, arg):
        print ("hello Denver, ")
        
    def do_intro(self, arg):
        print ("I am your Personal Assistant")
        
    
    def do_sum(self, arg):
        #@staticmethod
        def sum(*args):
            s = 0
            for i in args:
                s = s + i
            print (s)
        return sum(1,2,3,4,3,5,7,8,7,3,2)
        
    def do_EOF(self, arg):
        return True
    
    def do_exit(self, arg):
        return True
    
if __name__ == '__main__':
    MyCmd().cmdloop()