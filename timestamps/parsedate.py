
import sys
import re

# from dateutil import parser
from datetime import datetime

def parsedate(timestamp):

    year = None
    month = None
    day = None
    hour = 0
    minute = 0
    second = 0
    file = None
    dt = None

    # 
    # BSD ls -alT
    # 
    # -rw-r--r--  1 john  john     191 Mar 14 08:17:02 1997 I3d
    # ^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s([a-zA-Z]+)\s+(\d+)\s+(\d{2}):(\d{2}):(\d{2})\s+(\d{4})\s+(.+)$
    # [('-rw-r--r--', '1', 'john', 'john', '191', 'Mar', '14', '08', '17', '02', '1997', 'I3d')]
    r1 = re.findall(
        r"^([drwxs-]+)\s+(\d+)\s+([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{2}):(\d{2}):(\d{2})\s+(\d{4})\s+(.+)$",
        timestamp
    )
    if r1:
        # print(r1)
        # print(r1[0])
        # print(len(r1))
        # print(len(r1[0]))
        year = r1[0][10]
        month = r1[0][5]
        day = r1[0][6]
        hour = r1[0][7]
        minute = r1[0][8]
        second = r1[0][9]
        file = r1[0][11]

        if year and month and day:
            # dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
            # dt = parser.parse("{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second))
            # datetime(year, month, day, hour, minute, second, microsecond)
            dt = datetime.strptime(
                "{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second), 
                "%b %d %Y %H:%M:%S"
            )

    # 
    # BSD ls -al
    # 
    # -rw-r--r--    1 john  staff     513 Apr 24  1998 3dcircle.xpm
    # ^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s([a-zA-Z]+)\s+(\d+)\s+(\d{4})\s+(.+)$
    # [('-rw-r--r--', '1', 'john', 'staff', '513', 'Apr', '24', '1998', '3dcircle.xpm')]
    r2 = re.findall(
        r"^([drwxs-]+)\s+(\d+)\s+([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{4})\s+(.+)$",
        timestamp
    )
    if r2:
        # print(r2)
        # print(r2[0])
        # print(len(r2))
        # print(len(r2[0]))
        year = r2[0][7]
        month = r2[0][5]
        day = r2[0][6]
        hour = 0
        minute = 0
        second = 0
        file = r2[0][8]

        if year and month and day:
            # dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
            # dt = parser.parse("{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second))
            # datetime(year, month, day, hour, minute, second, microsecond)
            dt = datetime.strptime(
                "{} {} {}".format(month, day, year), 
                "%b %d %Y"
            )

    # print(year)
    # print(month)
    # print(day)
    # print(hour)
    # print(minute)
    # print(second)

    # 
    # Linux ls -al --full-time
    # 
    # -rw-r--r-- 1 root john    513 2021-04-04 23:10:15.450201000 -0700 3dcircle.xpm
    # ^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):((\d{2}))\.(\d{2})\d+\s+([+-])(\d{4})\s+(.+)$
    r3 = re.findall(
        r"^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):((\d{2}))\.(\d{2})\d+\s+([+-])(\d{4})\s+(.+)$",
        timestamp
    )
    if r3:
        # print(r3)
        # print(r3[0])
        # print(len(r3))
        # print(len(r3[0]))
        year = r3[0][5]
        month = r3[0][6]
        day = r3[0][7]
        hour = r3[0][8]
        minute = r3[0][9]
        second = r3[0][10]
        file = r3[0][15]

        if year and month and day:
            # dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
            # dt = parser.parse("{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second))
            # datetime(year, month, day, hour, minute, second, microsecond)
            dt = datetime.strptime(
                "{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second), 
                "%m %d %Y %H:%M:%S"
            )

    # 
    # Linux ls -al --full-time
    # 
    # drwxr-xr-x 3 john john 4096 1998-09-29 04:16              -0700 Mail
    # ^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})\s+([+-])(\d{4})\s+(.+)$
    r4 = re.findall(
        r"^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})\s+([+-])(\d{4})\s+(.+)$",
        timestamp
    )
    if r4:
        # print(r4)
        # print(r4[0])
        # print(len(r4))
        # print(len(r4[0]))
        year = r4[0][5]
        month = r4[0][6]
        day = r4[0][7]
        hour = r4[0][8]
        minute = r4[0][9]
        # second = r4[0][10]
        file = r4[0][12]

        if year and month and day:
            # dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
            # dt = parser.parse("{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second))
            # datetime(year, month, day, hour, minute, second, microsecond)
            dt = datetime.strptime(
                "{} {} {} {}:{}".format(month, day, year, hour, minute), 
                "%m %d %Y %H:%M"
            )

    # 
    # Linux ls -al
    # 
    # This should be the same as the BSD ls -al above
    # 
    # -rw-r--r-- 1 root john    513 Apr  4  2021 3dcircle.xpm

    # 
    # Other
    # 
    # -rw-r--r--   1 john  wheel  4016 18 Okt 18:35:39 2002 dtperf
    # ^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d+)\s+([a-zA-Z]+)\s+(\d{2}):(\d{2}):(\d{2})\s+(\d{4})\s+(.+)$
    r5 = re.findall(
        r"^([drwxs-]+)\s+(\d+)\s([a-zA-Z]+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d+)\s+([a-zA-Z]+)\s+(\d{2}):(\d{2}):(\d{2})\s+(\d{4})\s+(.+)$",
        timestamp
    )
    if r5:
        # print(r5)
        # print(r5[0])
        # print(len(r5))
        # print(len(r5[0]))
        year = r5[0][10]
        month = r5[0][6]
        day = r5[0][5]
        hour = r5[0][7]
        minute = r5[0][8]
        second = r5[0][9]
        file = r5[0][11]

        if year and month and day:
            # dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
            # dt = parser.parse("{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second))
            # datetime(year, month, day, hour, minute, second, microsecond)
            dt = datetime.strptime(
                "{} {} {} {}:{}:{}".format(month, day, year, hour, minute, second), 
                "%b %d %Y %H:%M:%S"
            )

    if dt and file:
        # print(dt.year, dt.month, dt.day,dt.hour, dt.minute, dt.second)
        # print( dt.strftime('%y%m%d%H%M.%S') )
        if dt:
            return ( file, dt.strftime('%y%m%d%H%M.%S') )

    return None
