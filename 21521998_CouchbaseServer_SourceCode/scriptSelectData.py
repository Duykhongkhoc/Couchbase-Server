
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException

cluster = Cluster.connect(
    "couchbase://26.92.45.245",
    ClusterOptions(PasswordAuthenticator("kduy", "123456")))
bucket = cluster.bucket("travel-sample")
collection = bucket.default_collection()

collection2 = cluster.bucket("testBucket").default_scope().collection("testCollection")
try:
    # chỉ có thể dùng .query() ở mức cluster
    result = cluster.query(
        "SELECT * FROM `travel-sample`.inventory.airport LIMIT 10", QueryOptions(metrics=True))
    for row in result.rows():
        print(f"Found row: {row}")

    print(f"Report execution time: {result.metadata().metrics().execution_time()}")

except CouchbaseException as ex:
    import traceback
    traceback.print_exc()