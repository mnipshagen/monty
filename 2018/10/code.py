if __name__ == '__main__':
    import datetime

    today = datetime.date.today()
    print(today)
    print(repr(today))

    now = datetime.datetime.now()
    print(now)
    print(repr(now))


    from datetime import date


    bday = date(1993, 11, 24)
    print(bday.weekday())
    print(bday.isoweekday())


    from datetime import datetime, timedelta


    now = datetime.now() + timedelta(days=9)
    print(now)
    print(now.strftime('%a, %d. %b %Y'))
    print(now.strftime('%c'))
    print(now.strftime('%Z %X %f %j'))


    from datetime import datetime


    parsed = datetime.strptime(
        'Wed Jun 13 14:47:12 2018',
        '%a %b %d %H:%M:%S %Y'
    )
    print(parsed.isoformat())


    from datetime import datetime


    # datetime.time does not allow math, so we use datetime
    a = datetime(2018, 6, 13, 14, 35)
    b = datetime(2018, 6, 13, 17, 22)

    print(b - a)


    from datetime import datetime


    a, b = datetime(2000, 2, 28, 23, 59), datetime(2000, 3, 1)
    c, d = datetime(2100, 2, 28, 23, 59), datetime(2100, 3, 1)

    print((b - a).days)  # leap year
    print((d - c).days)  # no leap year



    from datetime import datetime, timedelta


    now = datetime(2018,6,13,15,12,37)
    now = datetime.now()
    days137 = timedelta(days=137)

    print(now + days137)


    from datetime import datetime


    now = datetime.now()
    print(now.strftime('%c'))
    print(now.strftime('%a %b %#d %H:%M:%S %Y'))


    from datetime import datetime
    import locale


    locale.setlocale(locale.LC_ALL, 'de-DE')
    now = datetime.now() + timedelta(days=7,hours=9)
    print(now.strftime('%c'))
    print(now.strftime('%a %b %d %H:%M:%S %Y'))


    from datetime import datetime

    someday = datetime(2016,11,28,18,29,37)
    print(someday.strftime('%Y-%m-%dT%H:%M:%S'))
    print(someday.isoformat())


    from datetime import datetime


    a = datetime(2000, 2, 28, 23, 59)
    b = datetime(2000, 3, 1)
    print(type((b - a)))


    import math
    from datetime import datetime, timedelta


    begin = datetime(2018, 4, 3)
    end = datetime(2018, 7, 7)
    print(math.ceil((end - begin) / timedelta(weeks=1)))
    print(math.ceil((end - begin) / timedelta(weeks=2)))


    import parsedatetime as pdt


    cal = pdt.Calendar()
    time_struct, parse_status = cal.parse("hello")
    print(time_struct)
    print(parse_status)



    import calendar


    calendar.prmonth(2018, 6)
    print("\n", calendar.monthcalendar(2018, 6))


    import time


    print(time.time())
    #time.sleep(2)
    print("I was delayed by 2 seconds!")




    import random
    import time


    size = 10000
    seq = random.sample(range(10000000000), k=size)
    start = time.time()
    seq.sort()
    end = time.time()
    print(f"It took {end - start: .3f} seconds to sort {size} numbers.")



    import random
    import time


    def avg_performance(func, trials=100):
        results = []
        for i in range(trials):
            start = time.time()
            func()
            end = time.time()
            results.append(end-start)
        
        return sum(results) / trials

    #print(f"Average of: {avg:.3f}s over {trials} trials.")




    import timeit


    size = 100
    seq = random.sample(range(10000000000), k=size)
    print(timeit.timeit(seq.sort))


def func():
    "~".join(str(n) for n in range(100))