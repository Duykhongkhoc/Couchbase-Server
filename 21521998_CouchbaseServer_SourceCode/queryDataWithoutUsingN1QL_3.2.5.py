# Truy vấn dữ liệu bằng python SDK không sử dụng N1Ql -> ta sử dụng phương thức get() cho collection
from couchbase.cluster import Cluster 
from couchbase.options import ClusterOptions
from couchbase.cluster import QueryOptions
from couchbase.auth import PasswordAuthenticator
cluster = Cluster('couchbase://26.92.45.245',
ClusterOptions(PasswordAuthenticator('kduy', '123456')))
collection = cluster.bucket('travel-sample').scope('inventory').collection('airport')
result = collection.get('airport_1257')
print(result.content_as[str])
