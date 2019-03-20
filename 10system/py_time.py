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