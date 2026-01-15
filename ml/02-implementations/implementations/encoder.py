class CustomLabelEncoder:
    """
    A custom label encoder for categorical data, mimicking the functionality
    of sklearn's LabelEncoder.

    To code a label encoder from scratch, you need to implement a class that learns a mapping from unique categorical string values to numerical integers 
    and uses that mapping to transform data.
    This involves two main methods: fit to learn the mapping and transform to apply it. 
    The structure is similar to scikit-learn's LabelEncoder. 
    """
    
    def __init__(self):
        # Dictionary to store the mapping from category string to integer
        self.classes_ = {}
        # Counter for the next integer to assign
        self._next_label = 0

    def fit(self, y):
        """
        Fits the encoder to the unique values in the provided data.

        Args:
            y (list or pandas.Series): The categorical data to fit on.
        """
        # Ensure the input data is a set of unique values for efficient processing
        unique_values = set(y)
        for value in sorted(unique_values):
            if value not in self.classes_:
                self.classes_[value] = self._next_label
                self._next_label += 1
        return self

    def transform(self, y):
        """
        Transforms the input data into integer labels using the fitted mapping.

        Args:
            y (list or pandas.Series): The categorical data to transform.

        Returns:
            list: The transformed integer labels.
        """
        transformed_data = []
        for value in y:
            if value in self.classes_:
                transformed_data.append(self.classes_[value])
            else:
                # Handle unseen values, you might raise an error or assign a specific value
                raise ValueError(f"Unseen label '{value}' during transform")
        return transformed_data

    def fit_transform(self, y):
        """
        Fits the encoder and then transforms the data.

        Args:
            y (list or pandas.Series): The categorical data to fit and transform.

        Returns:
            list: The transformed integer labels.
        """
        self.fit(y)
        return self.transform(y)


# --- Example Usage ---

# 1. Create sample data
data = ['red', 'blue', 'green', 'blue', 'red', 'red', 'green', 'yellow']

# 2. Instantiate the custom encoder
encoder = CustomLabelEncoder()

# 3. Fit and transform the data
encoded_labels = encoder.fit_transform(data)

print(f"Original Data: {data}")
print(f"Encoded Labels: {encoded_labels}")
print(f"Learned Classes: {encoder.classes_}")

# 4. Transform new data (must contain only seen classes)
new_data = ['blue', 'yellow', 'red']
new_encoded = encoder.transform(new_data)
print(f"New Data: {new_data}")
print(f"Transformed New Data: {new_encoded}")
