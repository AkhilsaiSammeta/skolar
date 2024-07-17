
# Assignment 6: Using Libraries and Collaboration in Google Colab

## 1. Install a Python Library

In your Google Colab notebook, install a Python library of your choice. For this example, we'll use `Pandas`. You can install it by running the following code in a new code cell:

```python
!pip install pandas
```
2. Demonstrate Usage of the Installed Library
After installing the library, you can demonstrate its usage by performing a basic operation. Here’s an example using Pandas to create a simple DataFrame and display it:

```python
import pandas as pd
```
# Create a DataFrame
```
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
```
# Display the DataFrame

```
print(df)
```
Output:
```markdown
      Name  Age         City
0    Alice   24     New York
1      Bob   27  Los Angeles
2  Charlie   22      Chicago
```
This code creates a DataFrame with names, ages, and cities, and then prints it.

3. Collaborate on Your Colab Notebook
To collaborate on your Colab notebook:

# Invite a Classmate or Friend:
Click the "Share" button in the upper right corner of the Colab notebook.
Enter the email address of the person you want to invite to collaborate.
Set their permissions to "Editor" if you want them to be able to make changes.
Click "Send" to invite them.
Example email address to invite: exampleclassmate@gmail.com

# Collaborate:
Work with your collaborator on a simple Python code project or data analysis task within the notebook.
4. Save and Share Your Colab Notebook
Save to Google Drive:
Google Colab automatically saves your notebook to your Google Drive in a folder named "Colab Notebooks".
Share with Instructor or Peer:
Click the "Share" button in the upper right corner of the Colab notebook.
Under the "Get Link" section, change the access permissions to "Anyone with the link" or invite specific people by entering their email addresses.
Set the desired permissions (e.g., "Viewer" or "Commenter").
Copy the shareable link and provide it to your instructor or peer.
# Conclusion:
By following these steps, you can install and use Python libraries in Google Colab, collaborate with others on your notebook, and share your work effectively. This demonstrates the power and flexibility of Google Colab for collaborative data analysis and coding projects.
