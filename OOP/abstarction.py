# abstarction: it means hidden
# you can't make object of abstract class 

# besicaly methoad have two type
    # 1. abstract methoad : it have no code
    # 2. concract methoad : it have code
    
from abc import ABC , abstractmethod # here abc means abstrat base class

class bankApp(ABC):
    def database(self):
        print('conet to database')
    
    @abstractmethod
    def secqurity(self):
        pass
    
    
    
class mobileApp(bankApp):
    def Mobile_login(self):
        print('log in in to mobile')
    
    def secqurity(self):
        print('mobile app secquurity')    
    
        
mob=mobileApp()
mob.database()
mob.secqurity()
