# Run Frontend 

cd frontend 
npm install
npm run dev

# Run Backend 

cd backend
python manage.py runserver

# Requirements

django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.2.0
djangorestframework-simplejwt==5.2.2
django-storages==1.13.2
boto3==1.28.62  # AWS S3
python-decouple
transformers==4.50.1
torch==2.5.1
spacy==3.7.2
opencv-python==4.8.1.78
deepface==0.0.79
google-cloud-speech==2.21.0  # Speech-to-Text
python-multipart>=0.0.6
sentencepiece>=0.1.99
celery==5.3.1
redis==4.6.0
psycopg2==2.9.7
pip install transformers>=4.40.1 accelerate>=0.29.1