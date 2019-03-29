NOTE:

1) If splunk service isn't running (or it is not configured) this container will crash.
2) WARNING "splunk_python_1  | WARNING: no logs are available with the 'splunk' log driver"
    --this is means it works!
    --it means that no logs are being stored in the container they are getting sent to splunk
    --but docker logs {container_name} will not work,  and you wont see any output in foreground.