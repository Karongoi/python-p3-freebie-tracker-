from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


company1 = Company(name="TechCorp")
company2 = Company(name="GizmoWorks")


dev1 = Dev(name="Alice", age=28)
dev2 = Dev(name="Bob", age=32)


freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Coffee Mug", value=10, dev=dev2, company=company2)
freebie3 = Freebie(item_name="Sticker Pack", value=5, dev=dev1, company=company2)


session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("Seed data added successfully!")
