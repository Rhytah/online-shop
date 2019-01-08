# online-shop
prototype for an online shop api

```
views
````

## End Points
|           End Point                                 |            Functionality                   |
|   -----------------------------------------------   | -----------------------------------------  |
|     POST /creditcard                                |             add credit card data           |
|     GET  /creditcard                                |            fetch all credit card data      |
|     GET  /creditcard/int:cardnumber                 |           fetch specific credit card data  |
|     PUT  /creditcard/int:cardnumber                 | update credit card data                    |
|     DELETE /creditcard/int:cardnumber                | delete credit card data                   |


```
data fields

{
    "cardnumber":264521 ,
    "expirydate":"30/12/2019",
    "servicecode":3154654 ,
    "issuingbank":"some bank",
    "issuingagency":"state agency"
}
```