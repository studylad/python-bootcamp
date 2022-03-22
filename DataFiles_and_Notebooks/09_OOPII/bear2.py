import datetime
class Bear:
    logfile_name = "bear.log"
    bear_num     = 0
    def __init__(self,name):
        self.name = name
        print(f" made a bear called {name}")
        self.logf  = open(Bear.logfile_name,"a")
        Bear.bear_num += 1
        self.created = datetime.datetime.now()
        self.my_num = Bear.bear_num
        self.logf.write("[%s] created bear #%i named %s\n" % \
                        (datetime.datetime.now(),Bear.bear_num,self.name))
        self.logf.flush()
    
    def growl(self,nbeep=5):
        print("\a"*nbeep)

    def __del__(self):
        print(f"Bang! {self.name} is no longer.")
        self.logf.write("[%s] deleted bear #%i named %s\n" % \
                        (datetime.datetime.now(),self.my_num,self.name))
        self.logf.flush()
        # decrement the number of bears in the population
        Bear.bear_num -= 1
        # dont really need to close because Python will do the garbage collection
        #  for us. but it cannot hurt to be graceful here.
        self.logf.close()

    def __str__(self):
        age = datetime.datetime.now() - self.created
        return " name = %s bear (age %s) number = %i (population %i)" % \
                (self.name, age, self.my_num,Bear.bear_num)