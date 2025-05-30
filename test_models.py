import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

DATABASE_URL = "sqlite:///:memory:"  # in-memory DB for testing

class TestModels(unittest.TestCase):
    def setUp(self):
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

        # Seed some test data
        self.dev = Dev(name="Alice", age=30)
        self.company = Company(name="TestCo")
        self.session.add_all([self.dev, self.company])
        self.session.commit()

        self.freebie1 = Freebie(item_name="Mug", value=10, dev=self.dev, company=self.company)
        self.freebie2 = Freebie(item_name="Notebook", value=5, dev=self.dev, company=self.company)
        self.session.add_all([self.freebie1, self.freebie2])
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_get_freebies_by_dev(self):
        freebies = Dev.get_freebies(self.session, self.dev.id)
        self.assertEqual(len(freebies), 2)
        self.assertEqual(freebies[0].item_name, "Mug")

    def test_get_freebies_by_company(self):
        freebies = Company.get_freebies(self.session, self.company.id)
        self.assertEqual(len(freebies), 2)
        self.assertEqual(freebies[1].item_name, "Notebook")

if __name__ == "__main__":
    unittest.main()
