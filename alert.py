import talib 

ring_buffer = []
buffer_size = 15 

i = 0 
j = buffer_size
# 5 6 7 8 9
# 5 6 7 8

if i < buffer_size:
    ring_buffer[i] = x
else:
    ring_buffer[i] = x
    ring_buffer[j] = x

if i == buffer_size-1:
    i+=1
    j+=1
else:
    i = 0
    j = buffer_size

current = ring_buffer[i:j]
slope = ta.LINEAR_REG(current)
if slope * 180 + curr_price <= entryprice:
    twilio.send_msg("approaching crossover")
    