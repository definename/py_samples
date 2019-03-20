import time

epoch_origin = time.time()
print("\tTime since epoch_origin: {}".format(epoch_origin))
print("Local time from epoch_origin: {}".format(time.ctime(epoch_origin)))

st_local = time.localtime(epoch_origin)
epoch_regenerate = time.mktime(st_local)
print("\tTime since epoch_regenerate, with seconds resolution: {}".format(epoch_regenerate))

print("Local datetime with direct access: {}/{}/{} {}:{}:{}".format(
    st_local.tm_year,
    st_local.tm_mon,
    st_local.tm_mday,
    st_local.tm_hour,
    st_local.tm_min,
    st_local.tm_sec))

st_utc = time.gmtime(epoch_origin)
print("UTC datetime with direct access: {}/{}/{} {}:{}:{}".format(
    st_utc.tm_year,
    st_utc.tm_mon,
    st_utc.tm_mday,
    st_utc.tm_hour,
    st_utc.tm_min,
    st_utc.tm_sec))

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime(time.time())
print(time.strftime(fmt, t))

fmt2 = "%Y-%m-%d"
st_parsed = time.strptime("2019-03-21", fmt2)
print("Parsed struct_time with direct access: {}/{}/{}".format(
    st_parsed.tm_year,
    st_parsed.tm_mon,
    st_parsed.tm_mday))
