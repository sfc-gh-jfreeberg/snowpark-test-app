from snowflake.snowpark import DataFrame

def transform_data(df: DataFrame) -> DataFrame:
    transformed_data = df.withColumnRenamed("package_name", "packages_new")
    return transformed_data