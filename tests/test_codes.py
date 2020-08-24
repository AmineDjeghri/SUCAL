import ics
import timeit
from ics import Event, Calendar

# c = ics.Calendar()
# e = ics.Event()

# e.name = "My cool event"
# e.begin = '2014-01-01 00:00:00'
# c.events.add(e)
# print(c.events)

# with open('tests/my.ics', 'w') as f:
#     f.writelines(c)

# c = Calendar()
# e = Event()

# e.begin = '2014-01-01 00:00:00'
# for i in range(10000):
#     e.name = "My cool event"+str(i)
#     c.events.add(e)


# with open('tests/my.ics','w') as f:
#     f.write(str(c)) 



a=timeit.default_timer()
with open('tests/my.ics') as f:
    Calendar(str(f.read())).events
b=timeit.default_timer()
print(b-a)