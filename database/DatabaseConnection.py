import cx_Oracle

class DatabaseConnection():
  def __init__(self):
    cx_Oracle.init_oracle_client(lib_dir="/Users/cristhian/instantclient_19_3")
    
  def getConnection(self):
    host = 'db-mirakl-connector-neutral.c8o8ro33kkhk.us-west-2.rds.amazonaws.com'
    port = '1521'
    database = 'ORCL'
    user = 'mirakl_adm'
    password = 'Ripley.123$%'

    dsn = cx_Oracle.makedsn(host, port, service_name=database)
    self.connection = cx_Oracle.connect(user, password, dsn, encoding='UTF-8')
    return self.connection

  def commit(self):
    self.connection.commit()

  def rollback(self):
    self.connection.rollback()

  def close(self):
    self.connection.close()