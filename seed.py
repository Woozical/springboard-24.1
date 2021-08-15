from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pets = [
    Pet(name="Stevie Chicks", species="chicken", photo_url='https://backyardchickenproject.com/wp-content/uploads/2021/01/Untitled-design-11-copy-5-1-678x1024.png'),
    Pet(name="Blue", species="cat", photo_url='http://www.catbreedselector.com/wp-content/uploads/2016/06/Serrade-Petit-Cat-Photo.jpg'),
    Pet(name="Red", species="dog", photo_url='https://i.pinimg.com/originals/a0/f6/31/a0f631717848e4d07f63f40534312a9e.jpg'),
    Pet(name="Bubblina", species="fish", photo_url='https://cdn0.wideopenpets.com/wp-content/uploads/2016/03/file0001224419617.jpg'),
    Pet(name="Tammy", species="cat", photo_url='https://millennialmagazine.com/wp-content/uploads/2014/07/tabby-kitten-jody-trappe-photography.jpg'),
    Pet(name="Sushi", species="pig", photo_url='http://lifewithaminipig.com/wp-content/uploads/2015/06/cropped-Oscar-Looking-Pretty-5.2015-e1439214704702.jpg'),
    Pet(name="Scout", species="dog"),
    Pet(name="Piggie", species="dog", photo_url='https://c2.staticflickr.com/4/3194/2618232245_20fb4d996b_b.jpg'),
    Pet(name="Carrot Face", species="rabbit", photo_url='https://3.bp.blogspot.com/-cdQ12OuupI4/V9hJYMBr0zI/AAAAAAAAB_M/JRwekHUq4kQq-5X1IuzXs0EV6IBE1-MZQCLcB/s1600/rabbit-microchip-insurance.jpg'),
    Pet(name="Jerry", species="mouse"),
    Pet(name="Rocket", species="racoon"),
    Pet(name="Mango", species="fish", photo_url='https://mywaterearth.com/wp-content/uploads/2020/12/261946-1600x1030-take-care-new-goldfish-properly-1-950x612.jpg'),
    Pet(name="Tom", species="cat")
]

db.session.add_all(Pets)
db.session.commit()
