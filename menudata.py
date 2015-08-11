from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import datetime

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

#add first restaurant to db
#myFirstRestaurant = Restaurant(name = "Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()
# session.query(Restaurant).all()

#add cheese pizza to menu
# cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with natural ingredients and love", course = "Entree", price = "8.99", restaurant = myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()


#query for all veg burgers in db
veg = session.query(MenuItem).filter_by(name = 'Veggie Burger')

#update price of veg burgers
for burgers in veg:
    if burgers.price != "$2.99":
        burgers.price = "$2.99"
        session.add(burgers)
        session.commit()

for burgers in veg:
    print burgers.id
    print burgers.price
    print burgers.restaurant.name
    print "\n"

