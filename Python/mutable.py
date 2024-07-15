class MutableData:
    def __init__(self, data):
        self._data = data

    def update(self, key, value):
        self._data[key] = value
        return self._data

    def remove(self, key):
        if key in self._data:
            del self._data[key]
        return self._data

    def get(self, key):
        return self._data.get(key, None)

    def get_all(self):
        return self._data

# Example usage
data_store = MutableData({'name': 'John', 'age': 28})

# Update data
updated_data = data_store.update('age', 30)
print("Updated data:", updated_data)

# Get single data
name = data_store.get('name')
print("Name:", name)

# Remove data
removed_data = data_store.remove('email')  # This key does not exist
print("Data after removal attempt:", removed_data)

# Get all data
all_data = data_store.get_all()
print("All data:", all_data)
