import twilio_helper as th

msg_str = ""
f = open("msg.txt")

for s in f.readlines():
    msg_str += s

th.send_msg(msg_str)
