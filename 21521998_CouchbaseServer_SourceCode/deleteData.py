from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator

# Thiết lập thông tin kết nối
cluster = Cluster('couchbase://26.92.45.245')
authenticator = PasswordAuthenticator('kduy', '123456')  
cluster.authenticate(authenticator)
bucket = cluster.bucket('newBucket')
scope = bucket.scope('student-collection')
collection = scope.collection('student-collection')  

# Xóa tài liệu
document_id = 'id3'
collection.remove(document_id)
