def write_log(query, file='command_history.log.txt'):
  """As input, the function receives query and then writes it to a file that stores the log history.
  """
  import datetime as DT
  offset = DT.timedelta(hours=3)
  time = DT.datetime.now(DT.timezone(offset))
  time_format = "%d-%m-%Y %H:%M:%S"
  t_send = f"{time:{time_format}}"
  t_send = str(t_send)
  f = open(file, mode='a', errors='ignore')
  f.write(f"{query}; [{t_send}] \n \n")
  f.close()