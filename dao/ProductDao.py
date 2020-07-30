from DatabaseConnection import DatabaseConnection
import datetime

class ProductDao(object):

  def __init__(self):
    self.databaseConnection = DatabaseConnection()

  def getMaxProductId(self):
    lastProductId = 0
    
    connection = self.databaseConnection.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(PRODUCTS_ID) FROM CON_PRODUCTS')
    for row in cursor:
      lastProductId = row[0]
    return lastProductId


  def insertMany(self, products):
    connection = self.databaseConnection.getConnection()
    cursor = connection.cursor()
    data = []
    lastProductId = self.getMaxProductId()
    curretDatetime = datetime.datetime.now()
    for product in products:
      lastProductId += 1
      record = (
        lastProductId,
        product['FILE_ID'],
        product['VARIANT_ID'],
        product['VARIANT_CORR'],
        product['PARTNUMBER'],
        product['NAME'],
        product['LONGDESCRIPTION'],
        product['CATEGORY_CODE'],
        product['BRAND'],
        product['STATUS'],
        product['PRICE'],
        product['ORIGIN_PRICE'],
        product['SYNC'],
        product['SELLER_ID'],
        product['PRODUCT_SKU'],
        product['PRODUCT_SKU_PARENT'],
        curretDatetime,
        curretDatetime
      )
      data.append(record)

    cursor.executemany("""
      INSERT INTO CON_PRODUCTS (PRODUCTS_ID, FILE_ID, VARIANT_ID, VARIANT_CORR, PARTNUMBER, NAME , LONGDESCRIPTION, CATEGORY_CODE, BRAND, STATUS, PRICE, ORIGIN_PRICE, SYNC, SELLER_ID, PRODUCT_SKU, PRODUCT_SKU_PARENT, CREATE_DATE, LAST_DATE)
      VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18)""", data)
    connection.commit()
    cursor.close()
    connection.close()