from abc import ABC, abstractmethod

# Custom Exception
class AnalysisError(Exception):
    """Custom exception for errors during analysis."""
    pass

# Abstract Base Class
class DataAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        """Analyze the provided data."""
        pass

# Subclass for Text Data Analysis
class TextDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            # Check that data is a dictionary with a 'text' key
            if not isinstance(data, dict):
                raise TypeError("Data should be a dictionary.")
            
            text = data.get('text')
            if not isinstance(text, str):
                raise ValueError("Text should be a string.")
            
            # Dummy analysis: count words
            word_count = len(text.split())
            return "Text analysis result: " + str(word_count) + " words."

        except KeyError as e:
            raise KeyError("Missing expected key: " + str(e))
        except TypeError as e:
            raise TypeError("Type error: " + str(e))
        except ValueError as e:
            raise ValueError("Value error: " + str(e))
        except Exception as e:
            raise AnalysisError("An unexpected error occurred: " + str(e))

# Subclass for Numeric Data Analysis
class NumericDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            # Check that data is a dictionary with a 'values' key
            if not isinstance(data, dict):
                raise TypeError("Data should be a dictionary.")
            
            values = data.get('values')
            if not isinstance(values, list):
                raise ValueError("Values should be a list.")
            
            if not all(isinstance(x, (int, float)) for x in values):
                raise ValueError("All values should be numeric.")
            
            # Dummy analysis: calculate mean
            mean_value = sum(values) / len(values)
            return "Numeric analysis result: Mean value is " + str(round(mean_value, 2)) + "."

        except KeyError as e:
            raise KeyError("Missing expected key: " + str(e))
        except TypeError as e:
            raise TypeError("Type error: " + str(e))
        except ValueError as e:
            raise ValueError("Value error: " + str(e))
        except Exception as e:
            raise AnalysisError("An unexpected error occurred: " + str(e))

# Sample Data
text_data_list = [
    {"text": "Medical equipment requires regular maintenance."},
    {"text": "Medical equipment doesn't require regular maintenance."},
    {"text": 2447253},  # Invalid data
    {}  # Missing 'text' key
]

numeric_data_list = [
    {"values": [7, 9, 3, 4, 1]},
    {"values": "Medical Equipment Failure Prediction"},  # Invalid data
    {"values": [1, "two", 3]}  # Non-numeric value
]

# Instantiate analyzers
text_analyzer = TextDataAnalyzer()
numeric_analyzer = NumericDataAnalyzer()

def display_menu():
    """Display the menu options."""
    print("\n--- Data Analysis Menu ---")
    print("1. Analyze Text Data")
    print("2. Analyze Numeric Data")
    print("3. Exit")

def analyze_text_data():
    """Analyze text data with validation."""
    print("\nAnalyzing Text Data:")
    for data in text_data_list:
        try:
            result = text_analyzer.analyze(data)
            print(result)
        except AnalysisError as e:
            print("Analysis error:", e)
        except Exception as e:
            print("Unexpected error:", e)

def analyze_numeric_data():
    """Analyze numeric data with validation."""
    print("\nAnalyzing Numeric Data:")
    for data in numeric_data_list:
        try:
            result = numeric_analyzer.analyze(data)
            print(result)
        except AnalysisError as e:
            print("Analysis error:", e)
        except Exception as e:
            print("Unexpected error:", e)

def main():
    """Main function to run the menu-driven program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            analyze_text_data()
        elif choice == "2":
            analyze_numeric_data()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
