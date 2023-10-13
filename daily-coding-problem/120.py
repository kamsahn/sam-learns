"""
Implement the singleton pattern with a twist. 

First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance 
and in every odd call of getInstance(), return the second instance.
"""

"""
make a class
class has public methods storeInstance(), getInstance()
class has internal counter to determine which instance to return
"""

class Storage:
  def __init__(this):
    this.count = 0
    this.store = {
      "first": None,
      "second": None
    }
  
  def store_instance(this, first: any, second: any) -> bool:
    if (first is not None and second is not None):
      this.store["first"] = first
      this.store["second"] = second
      this.reset()
      return True
    else:
      return False
    
  def which_instance(this):
    return "first" if this.count % 2 == 1 else "second"
  
  def reset(this):
    this.count = 0
        
  def inc(this):
    this.count = this.count + 1
  
  def get_instance(this):
    this.inc() # start count at 1
    key = this.which_instance()
    return this.store[key]
  
storage = Storage()
storage.store_instance("apple", "banana")
for i in range(6):
  print(storage.get_instance())
