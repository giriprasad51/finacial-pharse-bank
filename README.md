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

### Fine Turing
    https://www.kaggle.com/code/giriprasad512/financial-1

    financial-training.ipynb

### Loss function
    Predict - GroundTruth

    positive - negative    less     100
    negative - positive    less     100
    neutral - negative     less      100 client who holds stock will 

    neutral - positive     0         40     no loss just for company growth
    positive - neutral     0         10	client who buys wont loss 
    negative - neutral     0         10	client just sell the stock

    positive - positive  more       -10
    negative - negative  more       -10
    neutral - neutral    more       -10

    acc1 = (positive-positive + negative-negative + neutral-neutral)/(positive-positive + negative-negative + neutral-neutral + positive-negative + negative-positive + neutral-negative + neutral-positive)

    precision = TP/(TP+FP)
    Recall = TP/(TP+FN)
    f1 score = 2*PR/(P+R)

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

### Screenshots
<table>
<tr>
    <td><img src="Screenshot (68).png" alt="Image 1" width="200"/></td>
    <td><img src="Screenshot (69).png" alt="Image 2" width="200"/></td>
</tr>
</table>