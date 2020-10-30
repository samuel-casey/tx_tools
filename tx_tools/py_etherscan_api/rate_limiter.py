import time

def rate_limiter(func):
    '''
    This is a decorator which delays each api call by 0.2 seconds, which makes
    it impossible to exceed the 5 calls per second limit of etherscan's API.
    In practice, this is an overcompensation.
    '''
    def rate_limiter_wrapper(*args, **kwargs):
        time.sleep(0.2)
        return func(*args, **kwargs)

    return rate_limiter_wrapper
