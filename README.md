# finacial-pharse-bank

### Set up
    conda create -n env2 python=3.11
    conda activate env2
    conda install pytorch==2.1.2 cpuonly -c pytorch


    git clone https://github.com/giriprasad51/finacial-pharse-bank.git

    cd finacial-pharse-bank
    pip install ./requirements.txt

### Start application
    python app.py



### Request

`POST /thing/`

    curl -X POST http://127.0.0.1:5000/api/data \
     -H "Content-Type: application/json" \
     -d '{
           "article": "According to the company 's updated strategy for the years 2009-2012, Basware targets a long-term net sales growth in the range of 20% -40% with an operating profit margin of 10% -20% of net sales"
         }'


### Response

    127.0.0.1 - - [02/Aug/2024 17:28:09] "POST /api/data HTTP/1.1" 201 -
    ['negative']

    {
        "message": "Data received successfully",
        "received_data": [
            "negative"
        ]
    }