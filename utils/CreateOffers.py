import random
import utils
from datetime import date, timedelta, datetime

startOfferId = 90000
minShippinPrice = 0
minShippinPriceAdd = 0
minShippinZone = 201020
minShippinType = 'fship'
priceAditionalInfo = None
description = ''
stateCode = 11
professional = True
premium = False
logisticClasses = ['MP', 'P']
active = [True, False]
favoriteRank = None
channels = 'INIT'
deleted = False
currencyIsoCode = 'PEN'
allowQuoteRequests = None
priceRanges = None

class CreateOffers(object):
  def __init__(self, childRows):
    self.fieldnames = ['offer-id','product-sku','min-shipping-price','min-shipping-price-additional','min-shipping-zone','min-shipping-type','price','total-price','price-additional-info','quantity','description','state-code','shop-id','shop-name','professional','premium','logistic-class','active','favorite-rank','channels','deleted','origin-price','discount-start-date','discount-end-date','available-start-date','available-end-date','discount-price','currency-iso-code','discount-ranges','leadtime-to-ship','allow-quote-requests','price-ranges']
    self.childRows = childRows
    self.offerRows = []

  def createOffers(self):
    offerId = startOfferId
    currentDate = date.today()

    for child in self.childRows:
      offerId += 1
      
      hasDiscount = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
      discountStartDate = None
      discountEndDate = None
      randomDays = random.randint(1, 60)
      discountPrice = 0
      discountRanges = None
      if hasDiscount:
        discountStartDate = currentDate - timedelta(days=randomDays)
        discountEndDate = currentDate + timedelta(days=randomDays)
        
        discountStartDate = datetime.strftime(discountStartDate, '%y-%m-%d') + 'T05:00:00Z'
        discountEndDate = datetime.strftime(discountEndDate, '%y-%m-%d') + 'T05:00:00Z'
        discountPrice = child['PRICE']
        discountRanges = f'1|{discountPrice}.00'

      hasAvailableDate = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) > 1
      availableStartDate = None
      availableEndDate = None
      leadTimeToShip = None
      if hasAvailableDate:
        availableStartDate = currentDate - timedelta(days=randomDays)
        availableEndDate = currentDate + timedelta(days=randomDays)

        availableStartDate = datetime.strftime(availableStartDate, '%y-%m-%d') + 'T05:00:00Z'
        availableEndDate = datetime.strftime(availableEndDate, '%y-%m-%d') + 'T05:00:00Z'
        leadTimeToShip = True

      shopId = child['SELLER_ID']
      row = {
        'offer-id': offerId,
        'product-sku': child['PRODUCT_SKU'],
        'min-shipping-price': minShippinPrice,
        'min-shipping-price-additional': minShippinPriceAdd,
        'min-shipping-zone': minShippinZone,
        'min-shipping-type': minShippinType,
        'price': child['PRICE'],
        'total-price': child['PRICE'],
        'price-additional-info': priceAditionalInfo,
        'quantity': random.randint(1, 50),
        'description': description,
        'state-code': stateCode,
        'shop-id': shopId,
        'shop-name': f'Tienda TEST {shopId}',
        'professional': professional,
        'premium': premium,
        'logistic-class': random.choice(logisticClasses),
        'active': random.choice(active),
        'favorite-rank': favoriteRank,
        'channels': channels,
        'deleted': deleted,
        'origin-price': child['ORIGIN_PRICE'],
        'discount-start-date': discountStartDate,
        'discount-end-date': discountEndDate,
        'available-start-date': availableStartDate,
        'available-end-date': availableEndDate,
        'discount-price': discountPrice,
        'currency-iso-code': currencyIsoCode,
        'discount-ranges': discountRanges,
        'leadtime-to-ship': leadTimeToShip,
        'allow-quote-requests': allowQuoteRequests,
        'price-ranges': priceRanges
      }
      self.offerRows.append(row)
    utils.writeCsv('data.csv', self.offerRows, self.fieldnames)