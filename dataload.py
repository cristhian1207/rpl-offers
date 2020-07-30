import sys
sys.path.insert(0, 'utils/')
sys.path.insert(0, 'dao/')
sys.path.insert(0, 'database/')

from CreateOffers import CreateOffers
from CreateProducts import CreateProducts

createProducts = CreateProducts()
createProducts.createParentRows()
createProducts.createChildRows()
createProducts.saveToDabase()
childRows = createProducts.getChildRows()

createOffers = CreateOffers(childRows)
createOffers.createOffers()

print('Proceso terminado!')