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
    {"text": 12345},  # Invalid data
    {}  # Missing 'text' key
]

numeric_data_list = [
    {"values": [1, 2, 3, 4, 5]},
    {"values": "not a list"},  # Invalid data
    {"values": [1, "two", 3]}  # Non-numeric value
]

# Instantiate analyzers
analyzers = [
    TextDataAnalyzer(),
    NumericDataAnalyzer()
]

# Process text data
print("Text Data Analysis:")
for analyzer in analyzers:
    if isinstance(analyzer, TextDataAnalyzer):
        for data in text_data_list:
            try:
                result = analyzer.analyze(data)
                print(result)
            except AnalysisError as e:
                print("Analysis error:", e)
            except Exception as e:
                print("Unexpected error:", e)

# Process numeric data
print("\nNumeric Data Analysis:")
for analyzer in analyzers:
    if isinstance(analyzer, NumericDataAnalyzer):
        for data in numeric_data_list:
            try:
                result = analyzer.analyze(data)
                print(result)
            except AnalysisError as e:
                print("Analysis error:", e)
            except Exception as e:
                print("Unexpected error:", e)
