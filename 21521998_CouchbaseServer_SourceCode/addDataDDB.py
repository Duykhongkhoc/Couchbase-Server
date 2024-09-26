from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator

# Thông tin kết nối Couchbase
cluster_address = "couchbase://26.92.45.245"
bucket_name = "newBucket"
scope_name = "art-school-scope"
collection_name = "student-collection"
username = "kduy"
password = "123456"

# Kết nối đến cluster
cluster = Cluster(cluster_address, ClusterOptions(
    PasswordAuthenticator(username, password)
))

# Mở kết nối đến bucket
bucket = cluster.bucket(bucket_name)
collection = bucket.scope(scope_name).collection(collection_name)

# Dữ liệu document bạn muốn thêm
document_key = "id3"
document_data = {
    "name": "kduy",
    "data-of-birth": "04-02-2003",
}

# Thêm document vào collection
collection.upsert(document_key, document_data)
