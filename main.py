from snowflake.snowpark.session import Session
from util.transformers import transform_data

session: Session = Session.builder.getOrCreate()

df = session.table('information_schema.packages')

df2 = transform_data(df)

df2.write.mode('overwrite').saveAsTable('packages_test')
