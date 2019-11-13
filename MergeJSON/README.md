# JSON MERGE

## Problem Statement
Write a program that can merge a series of files containing JSON array of Objects
into a single file containing one JSON object.

### OS Supported
Windows, Linux, Mac

## Excecution Time 0.003025 with Dictionary of Dictionaries O(n^2)

![Imgur](https://i.imgur.com/RqaOKcz.png)

## Algorithmic Complexity

### Best Case -> with normal simple dictionaries -> <b>O(n)</b>
### Best Case -> with same keys and different values (List of values) -> <b>O(n*k)</b> where k is the number of items in d2 values of same key in d1.
### Worst Case -> <b>O(n^2)</b> where it contains dictionary of dictionaries.

### The algorithmic complexity depends on the types of JSON files passed. 
### If the files contain values like <b>dictionary of dictionaries</b> a recursive function is called.
### If the files contain values like str, float or int then it is appended into a list.
### If the files contain values like list then the dictionary value list is extended to the existing value list.

### For example if there are two JSON files such as <b>d1.json</b> and <b>d2.json</b> .

~~~
d1 = {
  "employee": {
    "value": "1"
  }
}
~~~
~~~
d2 = {
  "employee": {
    "value": "2"
  },
  "values": [
    {
      "v": "1"
    },
    {
      "b": "2"
    }
  ]
}
~~~

### Output File merge.json

~~~
{
  "employee": {
    "value": [
      "1",
      "2"
    ]
  },
  "values": [
    {
      "v": "1"
    },
    {
      "b": "2"
    }
  ]
}
~~~

