class Controller:
    def __init__(kP, kI, kD, kG, kS):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.kG = kG
        self.kS = kS
        self.previous_time = time.ticks_us()
        self.i = 0
        self.max_i = 0
    
    def PID(self, desired_state, current_state):
        current_time = time.ticks_us()
        current_error = desired_state - current_state

        p = self.kP * current_error

        i += self.kI * (current_error * (current_time - self.previous_time))
        if i > self.max_i:
            i = max_i
        elif i < -max_i:
            i = -max_i
        
        try:
            previous_error = self.previous_error
        except:
            self.previous_error = current_error
            previous_error = self.previous_error

        d = self.kD * (current_error - previous_error) / (current_time - self.previous_time)

        self.previous_error = current_error
        self.previous_time = current_time

        return p + i + d
    
    def f(self, current_state):
        return self.kS + self.kG
    
    def output(self, desired_state, current_state):
        return PID(desired_state, current_state) + f(current_state)
        

    
