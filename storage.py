from google.cloud import storage

def upload(bucket_name, img_name, img_file):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(img_name)
    blob.upload_from_file(img_file)
    return f'uploaded {bucket_name}/${img_name}'

