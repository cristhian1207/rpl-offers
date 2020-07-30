import random
import utils
from ProductDao import ProductDao

file_id = 61924
variant_id = 'E740{}-NEGRO'
seller_ids = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
category_code = 'yolo'
brand = 'CMCL'
sync = 0
parent_status = 'E'
child_Status = 'M'
sku = 'PMP9000000{}'

class CreateProducts(object):
  def __init__(self):
    self.parent_rows = []
    self.child_rows = []
    self.fieldnames = ['FILE_ID','VARIANT_ID','VARIANT_CORR','PARTNUMBER','NAME' ,'LONGDESCRIPTION','CATEGORY_CODE','BRAND','STATUS','PRICE','ORIGIN_PRICE','SYNC','SELLER_ID','PRODUCT_SKU','PRODUCT_SKU_PARENT']

  def createParentRows(self):
    sellerIdIndex = 0
    for i in range(10000, 20000):
      curr_variant = variant_id.format(i)
      price = random.randint(30, 250)
      product_sku = sku.format(i)
      if i < 18000:
        sellerIdIndex = 0
      elif sellerIdIndex == 0:
        sellerIdIndex += 1
      elif i%200==0:
        sellerIdIndex += 1
      seller_id = seller_ids[sellerIdIndex]
      row = {
        'FILE_ID': file_id,
        'VARIANT_ID': curr_variant,
        'VARIANT_CORR': 0,
        'PARTNUMBER': f'{seller_id}|{curr_variant}',
        'NAME': curr_variant,
        'LONGDESCRIPTION': curr_variant,
        'CATEGORY_CODE': category_code,
        'BRAND': brand,
        'STATUS': parent_status,
        'PRICE': price,
        'ORIGIN_PRICE': price + 5,
        'SYNC': sync,
        'SELLER_ID': seller_id,
        'PRODUCT_SKU': product_sku,
        'PRODUCT_SKU_PARENT': None
      }
      self.parent_rows.append(row)

  def createChildRows(self):
    for parent in self.parent_rows:
      curr_variant = parent['VARIANT_ID']
      parent_sku = parent['PRODUCT_SKU']
      for i in range(1, 6):
        partnumber = f'{curr_variant}-{i}'
        product_sku = f'{parent_sku}-{i}'
        row = {
          'FILE_ID': file_id,
          'VARIANT_ID': curr_variant,
          'VARIANT_CORR': i,
          'PARTNUMBER': partnumber,
          'NAME': curr_variant,
          'LONGDESCRIPTION': curr_variant,
          'CATEGORY_CODE': category_code,
          'BRAND': brand,
          'STATUS': child_Status,
          'PRICE': parent['PRICE'],
          'ORIGIN_PRICE': parent['ORIGIN_PRICE'],
          'SYNC': sync,
          'SELLER_ID': parent['SELLER_ID'],
          'PRODUCT_SKU': product_sku,
          'PRODUCT_SKU_PARENT': parent_sku
        }
        self.child_rows.append(row)

  def getChildRows(self):
    return self.child_rows

  def saveToDabase(self):
    # utils.writeCsv('parent.csv', self.parent_rows, self.fieldnames)
    # utils.writeCsv('child.csv', self.child_rows, self.fieldnames)
    productDao = ProductDao()
    productDao.insertMany(self.parent_rows)
    productDao.insertMany(self.child_rows)