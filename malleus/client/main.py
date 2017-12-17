from service.call_service import CallService
import time
call_service = CallService("west")

call_service.write(500)

# print(time.time())
call_service.read(500)
# print(time.time())