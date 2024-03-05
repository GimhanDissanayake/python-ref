import time

def tictoc(func):
  def wrapper(*args, **kwargs):
    t1 = time.time()
    func(**args, **kwargs)
    t2 = time.time() - t1
    print(f'Took {t2} sconds'
          f'to complete {func.__name__} function')
  return wrapper

@tictoc    
def do_this():
  time.sleep(1.2)

@tictoc
def do_that():
  time.sleep(1.6)

do_that()
do_this()
print('Done')