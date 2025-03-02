import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Dataset
file_path = "C:\\Users\\chandrashekar\\Desktop\\Madhavi\\women dataset.csv"  # Ensure the file is in your PyCharm project folder
df = pd.read_csv(file_path)

# Step 3: Clean Data (Remove Missing Reviews)
df = df.dropna(subset=['Review Text'])

# Step 4: Define Sentiment Analysis Function
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # -1 to 1 scale
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Step 5: Apply Sentiment Analysis
df["Sentiment"] = df["Review Text"].apply(get_sentiment)

# Step 6: Print Sentiment Distribution
print("Sentiment Distribution (%):")
print(df["Sentiment"].value_counts(normalize=True) * 100)

# Step 7: Save Processed Data for Power BI/Excel
df.to_csv("Sentiment_Analysis_Results.csv", index=False)
print("Processed data saved successfully!")

# Step 8: Data Visualization
plt.figure(figsize=(8,5))
sns.countplot(x=df["Sentiment"], palette="coolwarm")
plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.show()
