# events-generator
Generator for events on a shopping website

## Requirements:
* python3
* internet connection (to retrieve [randomly generated customers list](https://randomuser.me))

## Usage:
```python
python3 event_generator.py N
```
where N is in the range [1, 5000]

## Output example:
```javascript
{
  'shopper': {
    'name': 'Mahé Francois',
    'city': 'Poitiers',
    'id': '1NNaN55090834 17'
  },
  'product': {
    'name': 'LG Q7 BLUE DS',
    'sku': 'LMQ610EMW.AHUNBL'
  },
  'timestamp': '2019-07-10T04:58:19.002756',
  'event': 'SHOPPER_REMOVED_PRODUCT_FROM_CART'
}
```
