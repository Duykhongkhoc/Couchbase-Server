from couchbase.cluster import Cluster
from couchbase.options import QueryOptions;
from couchbase.options import ClusterOptions;
from couchbase.auth import PasswordAuthenticator;

cluster = Cluster('couchbase://26.92.45.245', ClusterOptions(PasswordAuthenticator('kduy','123456')))

# Get data from cluster by using N1QL, noet that we can only use query() in level cluster 
print("Get data from cluster by using N1QL")
result = cluster.query("SELECT * FROM `travel-sample`.inventory.airport LIMIT 10")

for row in result:
    print(row)

# Get data from cluster without using N1QL
print("\nGet data from cluster without using N1QL")
collection = cluster.bucket('travel-sample').scope('inventory').collection('airport')
result = collection.get('airport_1254')

print(result.content_as[str])