# captured_images.py
import os

class CapturedImages:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path  # Path to the data file
        self.photo_names = []  # List to store photo names
        self.photo_encodings = []  # List to store photo encodings

        # Load existing data when the class is initialized
        self._load_from_file()

# load data from the file
# return = self.photo_names, self.photo_encodings

    def get_loaded_data(self):
        """
        Return the loaded photo_names and photo_encodings.
        """
        return self.photo_names, self.photo_encodings



# add user function
#input : name , encoding of the user photo 

    def add_image(self, name, encoding):
        """
        Add a new image name and encoding to the lists.
        """
        self.photo_names.append(name)
        self.photo_encodings.append(encoding)
        self._save_to_file()  # Save the updated data to a file


#remove function by name
#input : name 
# return 1 if user removed , return 0 if user not found
    def remove_image(self, name):
        """
        Remove a customer by their name.
        """
        name = name.lower()  # Convert the input name to lowercase for case-insensitive comparison
        self.photo_names = [n.lower() for n in self.photo_names]  # Convert all names to lowercase

        try:
            # Find the index of the name to remove
            index = self.photo_names.index(name)
            
            # Remove the name and encoding at the found index
            self.photo_names.pop(index)
            self.photo_encodings.pop(index)
            
            # Save the updated lists to the file
            self._save_to_file()
            
            return 1
        except ValueError:
            # Handle the case where the name is not found
            return 0

    def _save_to_file(self):
        """
        Save the current state of photo_names and photo_encodings to a file.
        """
        with open(self.data_file_path, "w") as file:
            file.write(f"photo_names = {self.photo_names}\n")
            file.write(f"photo_encodings = {self.photo_encodings}\n")

    def _load_from_file(self):
        """
        Load the photo_names and photo_encodings from the file.
        If the file doesn't exist, initialize empty lists.
        """
        if os.path.exists(self.data_file_path):
            with open(self.data_file_path, "r") as file:
                # Read the file content
                exec(file.read(), globals())
                self.photo_names = photo_names
                self.photo_encodings = photo_encodings
        else:
            return 0