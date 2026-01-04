import pandas as pd

def rearrange_products_table(products: pd.DataFrame):
    # products.set_index(keys='product_id', inplace=True)
    products = products.melt(id_vars='product_id', var_name='store', value_name='price')
    products = products.dropna(how='any', subset=['price']).sort_values(by=['product_id','store'])
    return products

# test df
products = pd.DataFrame({
    'product_id':[0,1],
    'store1':[95,70],
    'store2':[100, None],
    'store3':[105,80]
})

result = rearrange_products_table(products)
print(result)