import multiprocessing


class WorkerInfo(object):
    def __init__(self,func,args):
        self._func = func
        self._func_args = args
    def func(self):
        return self._func
    def args(self):
        return self._func_args
def is_tuple_or_list(el):
    try:
        if isinstance(el, tuple) or isinstance(el, list):
            return True
    except TypeError:
        return False
def wrap_tuples(el):
        if is_tuple_or_list(el):
            return tuple(el)
        else:
            l=[]
            l.append(el)
            return tuple(l)
def worker(worker_info):
    try:
        func=worker_info.func()
        args=wrap_tuples(worker_info.args())
        func(*args)
    except Exception as e:
        print("worker run error,{}".format(e))
    
    
def multi_worker(pool_size,worker_infos):
    pool = multiprocessing.Pool(processes=pool_size)
    pool.map(worker,worker_infos)
    pool.close()
    pool.join()
