class Time(object):
    
    def __init__(self):
        pass
        
    @staticmethod
    def millis_to_string(millis):
        result = ''
        
        secs = int(millis) / 1000
        mins = secs / 60
        left_secs = secs - mins * 60
        
        if left_secs < 10:
            result = "%d:0%d" % (mins, left_secs)
        else:
            result = "%d:%d" % (mins, left_secs)
        
        return result
        