from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="Tech Corp")
company2 = Company(name="Gadget Inc")
session.add_all([company1, company2])
session.commit()

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])
session.commit()

freebie1 = Freebie(item_name="T-shirt", dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker", dev=dev2, company=company2)
session.add_all([freebie1, freebie2])
session.commit()

freebies = session.query(Freebie).all()
for f in freebies:
    print(f"{f.item_name} given to {f.dev.name} by {f.company.name}")
