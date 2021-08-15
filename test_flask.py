from unittest import TestCase
from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adopt_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class GETRoutesTestCase(TestCase):
    def setUp(self):
        Pet.query.delete()

        #Create sample entry
        pet = Pet(name="Blue", species="cat", photo_url="http://test.test/test.jpg", notes="asdfogindfo")
        db.session.add(pet)
        db.session.commit()

        self.pet_id = pet.id

    def tearDown(self):
        db.session.rollback()

    def test_home_view(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            pet = Pet.query.get(self.pet_id)

            self.assertEqual(res.status_code, 200)
            self.assertIn(pet.name.casefold(), html.casefold())
            self.assertIn(pet.species.casefold(), html.casefold())
            self.assertIn(pet.photo_url.casefold(), html.casefold())
    
    def test_add_pet_view(self):
        with app.test_client() as client:
            res = client.get('/add')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<form', html)
            self.assertIn('Submit</button>', html)

    def test_details_view(self):
        with app.test_client() as client:
            res = client.get(f'/{self.pet_id}')
            html = res.get_data(as_text=True)
            pet = Pet.query.get(self.pet_id)

            self.assertEqual(res.status_code, 200)
            self.assertIn(pet.name.casefold(), html.casefold())
            self.assertIn(pet.species.casefold(), html.casefold())
            self.assertIn(pet.notes.casefold(), html.casefold())
            self.assertIn(pet.photo_url.casefold(), html.casefold())
            self.assertIn('<form', html)
            self.assertIn('Save Changes</button>', html)
            self.assertIn('name="photo_url"', html)

            # Test invalid url, missing pet
            Pet.query.delete()
            db.session.commit()

            res = client.get(f'/{self.pet_id}')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 404)
    

class POSTRoutesTestCase(TestCase):

    def setUp(self):
        Pet.query.delete()

    def tearDown(self):
        db.session.rollback()

    
    def test_add_pet_POST(self):
        with app.test_client() as client:
            data = {
                'name' : 'Rocket',
                'species' : 'RACOON',
                'age' : 10,
                'photo_url' : 'http://test.test/test.jpg',
                'notes' : 'Hello World'
            }

            res = client.post('/add', data=data, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(data['name'].casefold(), html.casefold())
            self.assertIn(data['species'].casefold(), html.casefold())
            self.assertIn(data['photo_url'].casefold(), html.casefold())

            self.assertTrue(Pet.query.filter_by(name = 'Rocket').all())
    

    def test_invalid_add_pet_POST(self):
        with app.test_client() as client:
            data = {
                'species' : 'RACOON',
                'age' : 10,
                'photo_url' : 'ksndfsstst.jpg',
                'notes' : 'Hello World'
            }
            res = client.post('/add', data=data, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<form', html.casefold())
            self.assertIn('valid url', html.casefold())


    def test_edit_pet_POST(self):
        with app.test_client() as client:
            pet = Pet(name="Blue", species="cat", photo_url="http://test.test/test.jpg", notes="asdfogindfo")
            db.session.add(pet)
            db.session.commit()

            data = {'photo_url' : 'http://test.test/new.png'}
            res = client.post(f'/{pet.id}', data=data, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(data['photo_url'].casefold(), html.casefold())

            pet = Pet.query.filter_by(name='Blue').first()
            self.assertEqual(pet.photo_url, data['photo_url'])
    
    def test_invalid_edit_pet_POST(self):
        with app.test_client() as client:
            pet = Pet(name="Blue", species="cat", photo_url="http://test.test/test.jpg", notes="asdfogindfo")
            db.session.add(pet)
            db.session.commit()

            data = {'photo_url' : 'asnsfngs'}
            res = client.post(f'/{pet.id}', data=data, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('valid url', html.casefold())
            
            pet = Pet.query.filter_by(name='Blue').first()
            self.assertNotEqual(pet.photo_url, data['photo_url'])