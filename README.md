# VectorDBCostSavingInspector

This is a CLI tool designed to estimate how much money you can save on stale vectors database. The current version support Pinecone usage inspection based on vector's last access timestamp. 

If your vector database is not Pinecone, we will estimate saving based on your vector database use cases. 

If your Pinecone database does not have meta data about last access timestamp, we will estimate saving based on your vector database use cases. But we strongly suggest you add one. 

## Setup
1. Install python package

```
python3 -m pip install vector-db-cost-inspector
```
2. Environment Variables 

Create a .env file(or export them in terminal) with:

```
PINECONE_API_KEY="your-pinecone-key"
PINECONE_INDEX_NAME="your-index-name"
```

**Note:** This inspection tool only run in your machine. The Pinecone API key is only read by the inspection tool and won't be uploaded to cloud. We guarantee we don't have access to your Pinecone API key. This is a open source python tool. You can check our code if you want anytime.  

If you prefer not to inspect your vector database, we can approxicate cost saving based on the number of vectors and how the vectors are used. 
### Prerequisites

- A Pinecone Index.
- Vectors in Pinecone MUST have a metadata field named created_at (Unix timestamp) for the time-based logic to work.

## Usage

### Run the inspection

```
vector-inspect
```
