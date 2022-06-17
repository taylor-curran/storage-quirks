from prefect import flow

@flow(name="Storage Quirk")
def my_favorite_function():
    print("This function doesn't do much")
    return 42

if __name__ == "__main__":
    my_favorite_function()