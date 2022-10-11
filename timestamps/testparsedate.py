
from parsedate import parsedate

def testparsedate(date, expectedfile, expecteddate):
    print( "Test parse: sample: " + date )
    print( "Test parse: expect: " + expectedfile )
    print( "Test parse: expect: " + expecteddate )

    res = parsedate(date)
    if not res:
        print("Test case returned nothing, fail")
        return False

    actualfile = res[0]
    actualdate = res[1]

    print( "Test parse: actual: " + actualfile )
    print( "Test parse: actual: " + actualdate )
    if actualfile != expectedfile:
        print("Test case differs, fail")
        return False
    if actualdate != expecteddate:
        print("Test case differs, fail")
        return False

    print("Test case passed, success")
    return True

# 
# BSD ls -alT
# 
# -rw-r--r--  1 john  john     191 Mar 14 08:17:02 1997 I3d
testparsedate(
    "-rw-r--r--  1 john  john     191 Mar 14 08:17:02 1997 I3d", 
    "I3d", 
    "9703140817.02"
)

# 
# BSD ls -al
# 
# -rw-r--r--    1 john  staff     513 Apr 24  1998 3dcircle.xpm
testparsedate(
    "-rw-r--r--    1 john  staff     513 Apr 24  1998 3dcircle.xpm", 
    "3dcircle.xpm", 
    "9804240000.00"
)

# 
# Linux ls -al --full-time
# 
# -rw-r--r-- 1 root john    513 2021-04-04 23:10:15.450201000 -0700 3dcircle.xpm
testparsedate(
    "-rw-r--r-- 1 root john    513 2021-04-04 23:10:15.450201000 -0700 3dcircle.xpm", 
    "3dcircle.xpm", 
    "2104042310.15"
)

# 
# Linux ls -al --full-time
# 
# drwxr-xr-x 3 john john 4096 1998-09-29 04:16              -0700 Mail
testparsedate(
    "drwxr-xr-x 3 john john 4096 1998-09-29 04:16              -0700 Mail", 
    "Mail", 
    "9809290416.00"
)

# 
# Linux ls -al
# 
# This should be the same as the BSD ls -al above
# 
# -rw-r--r-- 1 root john    513 Apr  4  2021 3dcircle.xpm
testparsedate(
    "-rw-r--r-- 1 root john    513 Apr  4  2021 3dcircle.xpm", 
    "3dcircle.xpm", 
    "2104040000.00"
)

# 
# 
# -rw-r--r--   1 john  wheel  4016 18 Oct 18:35:39 2002 dtperf
testparsedate(
    "-rw-r--r--   1 john  wheel  4016 18 Oct 18:35:39 2002 dtperf", 
    "dtperf", 
    "0210181835.39"
)

# 
# 
# -rw-r--r--   1 john  wheel  4016 18 Okt 18:35:39 2002 dtperf
# testparsedate(
#     "-rw-r--r--   1 john  wheel  4016 18 Okt 18:35:39 2002 dtperf", 
#     "dtperf", 
#     "0210181835.39"
# )
