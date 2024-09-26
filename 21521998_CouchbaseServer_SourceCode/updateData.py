from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator

# Thông tin kết nối Couchbase
cluster_address = "couchbase://26.92.45.245"
bucket_name = "travel-sample"
scope_name = "inventory"
collection_name = "landmark"
username = "kduy"
password = "123456"

# Kết nối đến cluster
cluster = Cluster(cluster_address, ClusterOptions(
    PasswordAuthenticator(username, password)
))

# Mở kết nối đến bucket
bucket = cluster.bucket(bucket_name)
collection = bucket.scope(scope_name).collection(collection_name)

# Dữ liệu cập nhật
document_key = "landmark_10090"
name_value = "Squiggly Bridge"

# Thực hiện câu lệnh N1QL UPDATE
query = f'UPDATE landmark USE KEYS "{document_key}" SET name = "{name_value}"'
result = cluster.query(query)
